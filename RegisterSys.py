import datetime

def display_menu():
    print("\n" + "="*50)
    print("UNIVERSITY STUDY REGISTER SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. Search Student")
    print("3. Search Course")
    print("4. Add Course Completion")
    print("5. Show Student's Record")
    print("6. Exit")
    print("="*50)

def read_courses():
    """Read and return courses data from courses.txt"""
    courses = []
    with open('courses.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(',')
                course_code = parts[0]
                course_name = parts[1]
                credits = int(parts[2])
                teachers = parts[3:]
                courses.append({
                    'code': course_code,
                    'name': course_name,
                    'credits': credits,
                    'teachers': teachers
                })
    return courses

def read_students():
    """Read and return students data from students.txt"""
    students = []
    with open('students.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(',')
                student_id = int(parts[0])
                last_name = parts[1]
                first_name = parts[2]
                second_name = parts[3]
                email = parts[4]
                start_year = int(parts[5])
                program = parts[6]
                students.append({
                    'id': student_id,
                    'last_name': last_name,
                    'first_name': first_name,
                    'second_name': second_name,
                    'email': email,
                    'start_year': start_year,
                    'program': program
                })
    return students

def read_passed():
    """Read and return passed courses data from passed.txt"""
    passed = []
    with open('passed.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(',')
                course_code = parts[0]
                student_id = int(parts[1])
                date = parts[2]
                grade = int(parts[3])
                passed.append({
                    'course_code': course_code,
                    'student_id': student_id,
                    'date': date,
                    'grade': grade
                })
    return passed

def write_students(students):
    """Write students data to students.txt"""
    with open('students.txt', 'w') as file:
        for student in students:
            line = f"{student['id']},{student['last_name']},{student['first_name']},{student['second_name']},{student['email']},{student['start_year']},{student['program']}\n"
            file.write(line)

def write_passed(passed):
    """Write passed courses data to passed.txt"""
    with open('passed.txt', 'w') as file:
        for record in passed:
            line = f"{record['course_code']},{record['student_id']},{record['date']},{record['grade']}\n"
            file.write(line)

def add_student():
    """Add a new student to the system"""
    print("\n=== Add New Student ===")
    students = read_students()
    
    # Get student ID
    while True:
        try:
            student_id = int(input("Enter student ID: "))
            # Check if ID already exists
            if any(s['id'] == student_id for s in students):
                print("Error: Student ID already exists!")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer for student ID")
    
    # Get student information
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    second_name = input("Enter second name (press Enter if none): ")
    email = input("Enter email: ")
    
    while True:
        try:
            start_year = int(input("Enter starting year: "))
            break
        except ValueError:
            print("Error: Please enter a valid year")
    
    # Get program
    valid_programs = ['CE', 'EE', 'ET', 'ME', 'SE']
    while True:
        program = input("Enter program (CE/EE/ET/ME/SE): ").upper()
        if program in valid_programs:
            break
        print(f"Error: Program must be one of {', '.join(valid_programs)}")
    
    # Add new student
    students.append({
        'id': student_id,
        'last_name': last_name,
        'first_name': first_name,
        'second_name': second_name,
        'email': email,
        'start_year': start_year,
        'program': program
    })
    
    write_students(students)
    print(f"\nStudent {first_name} {last_name} (ID: {student_id}) added successfully!")

def search_student():
    """Search for a student by ID or name"""
    print("\n=== Search Student ===")
    students = read_students()
    
    search_term = input("Enter student ID or name to search: ")
    
    results = []
    
    # Check if search term is a number (ID search)
    try:
        search_id = int(search_term)
        results = [s for s in students if s['id'] == search_id]
    except ValueError:
        # Name search
        search_term_lower = search_term.lower()
        results = [s for s in students if 
                   search_term_lower in s['first_name'].lower() or 
                   search_term_lower in s['last_name'].lower() or
                   search_term_lower in s['second_name'].lower()]
    
    if not results:
        print("No students found.")
    else:
        print(f"\nFound {len(results)} student(s):")
        for student in results:
            full_name = f"{student['first_name']} {student['second_name']} {student['last_name']}" if student['second_name'] else f"{student['first_name']} {student['last_name']}"
            print(f"\nID: {student['id']}")
            print(f"Name: {full_name}")
            print(f"Email: {student['email']}")
            print(f"Start Year: {student['start_year']}")
            print(f"Program: {student['program']}")

def search_course():
    """Search for a course by code or name"""
    print("\n=== Search Course ===")
    courses = read_courses()
    
    search_term = input("Enter course code or name to search: ").lower()
    
    results = [c for c in courses if 
               search_term in c['code'].lower() or 
               search_term in c['name'].lower()]
    
    if not results:
        print("No courses found.")
    else:
        print(f"\nFound {len(results)} course(s):")
        for course in results:
            print(f"\nCode: {course['code']}")
            print(f"Name: {course['name']}")
            print(f"Credits: {course['credits']}")
            print(f"Teacher(s): {', '.join(course['teachers'])}")

def add_course_completion():
    """Add or update a course completion record"""
    print("\n=== Add Course Completion ===")
    
    students = read_students()
    courses = read_courses()
    passed = read_passed()
    
    # Get course code
    course_code = input("Enter course code: ").upper()
    course_exists = any(c['code'] == course_code for c in courses)
    if not course_exists:
        print("Error: Course code not found!")
        return
    
    # Get student ID
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: Invalid student ID")
        return
    
    student_exists = any(s['id'] == student_id for s in students)
    if not student_exists:
        print("Error: Student ID not found!")
        return
    
    # Get date
    date_str = input("Enter completion date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print("Error: Invalid date format!")
        return
    
    # Get grade
    try:
        grade = int(input("Enter grade (1-5): "))
        if grade < 1 or grade > 5:
            print("Error: Grade must be between 1 and 5")
            return
    except ValueError:
        print("Error: Invalid grade")
        return
    
    # Check if student already has a record for this course
    existing_record = None
    for record in passed:
        if record['course_code'] == course_code and record['student_id'] == student_id:
            existing_record = record
            break
    
    if existing_record:
        # Update if new grade is better
        if grade > existing_record['grade']:
            existing_record['grade'] = grade
            existing_record['date'] = date_str
            print(f"\nGrade updated to {grade} for course {course_code}")
        else:
            print(f"\nExisting grade ({existing_record['grade']}) is better or equal. No update made.")
    else:
        # Add new record
        passed.append({
            'course_code': course_code,
            'student_id': student_id,
            'date': date_str,
            'grade': grade
        })
        print(f"\nCourse completion added: {course_code} for student {student_id} with grade {grade}")
    
    write_passed(passed)

def show_student_record():
    """Show all courses passed by a student"""
    print("\n=== Show Student's Record ===")
    
    students = read_students()
    courses = read_courses()
    passed = read_passed()
    
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: Invalid student ID")
        return
    
    # Find student
    student = None
    for s in students:
        if s['id'] == student_id:
            student = s
            break
    
    if not student:
        print("Error: Student not found!")
        return
    
    # Display student info
    full_name = f"{student['first_name']} {student['second_name']} {student['last_name']}" if student['second_name'] else f"{student['first_name']} {student['last_name']}"
    print(f"\n{'='*60}")
    print(f"Student: {full_name}")
    print(f"ID: {student['id']}")
    print(f"Email: {student['email']}")
    print(f"Program: {student['program']}")
    print(f"Start Year: {student['start_year']}")
    print(f"{'='*60}")
    
    # Get student's passed courses
    student_records = [p for p in passed if p['student_id'] == student_id]
    
    if not student_records:
        print("\nNo courses completed yet.")
    else:
        print(f"\nCompleted Courses ({len(student_records)}):")
        print(f"{'Course Code':<12} {'Course Name':<40} {'Credits':<8} {'Grade':<6} {'Date'}")
        print("-" * 90)
        
        total_credits = 0
        for record in student_records:
            # Find course details
            course = None
            for c in courses:
                if c['code'] == record['course_code']:
                    course = c
                    break
            
            if course:
                print(f"{course['code']:<12} {course['name']:<40} {course['credits']:<8} {record['grade']:<6} {record['date']}")
                total_credits += course['credits']
        
        print("-" * 90)
        print(f"Total Credits: {total_credits}")


def main():
    """Main program loop"""
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            search_course()
        elif choice == '4':
            add_course_completion()
        elif choice == '5':
            show_student_record()
        elif choice == '6':
            print("\nThank you for using the University Study Register System!")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()