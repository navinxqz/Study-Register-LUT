import datetime

def menu():
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

def readStudents():
    students = []
    file=open('students.txt', 'r')
    for line in file:
        line = line.strip()
        if line:
            parts = line.split(',')
            student = {
                'id': int(parts[0]),
                'last_name': parts[1],
                'first_name': parts[2],
                'second_name': parts[3],
                'email': parts[4],
                'start_year': int(parts[5]),
                'program': parts[6]
            }
            students.append(student)
    file.close()
    return students

def addStudent():
    print("\n=== Add New Student ===")
    stds = readStudents()

    while True:
        sid_input = input("Enter student ID: ")
        if sid_input.isdigit():
            sid = int(sid_input)
            idExists = False
            for s in stds:
                if s['id'] == sid:
                    idExists = True
                    break
            if idExists:
                print("Error: Student ID already exists!")
            else:
                break
        else:
            print("Error: Please enter numbers only for student ID")
    
    ln = input("Enter last name: ")
    fn = input("Enter first name: ")
    sn = input("Enter second name (press Enter if none): ")
    em = input("Enter email: ")
    
    while True:
        yr_input = input("Enter starting year: ")
        if yr_input.isdigit():
            yr = int(yr_input)
            break
        else:
            print("Error: Please enter numbers only for year")
    
    progs = ['CE', 'EE', 'ET', 'ME', 'SE']
    while True:
        prog = input("Enter program (CE/EE/ET/ME/SE): ").upper()
        if prog in progs:
            break
        print(f"Error: Program must be one of {', '.join(progs)}")
    
    stds.append({'id': sid, 'last_name': ln, 'first_name': fn,'second_name': sn, 'email': em, 'start_year': yr, 'program': prog})
    
    writeStudents(stds)
    print(f"\nStudent {fn} {ln} (ID: {sid}) added successfully!")
    
def readCourses():
    courses = []
    file=open('courses.txt', 'r')
    for line in file:
        line = line.strip()
        if line:
            parts = line.split(',')
            course = {
                'code': parts[0],
                'name': parts[1],
                'credits': int(parts[2]),
                'teachers': parts[3:]
            }
            courses.append(course)
    file.close()
    return courses

def readPassed():
    passed_records = []
    file=open('passed.txt', 'r')
    for line in file:
        line = line.strip()
        if line:
            parts = line.split(',')
            record = {
                'course_code': parts[0],
                'student_id': int(parts[1]),
                'date': parts[2],
                'grade': int(parts[3])
            }
            passed_records.append(record)
    file.close()
    return passed_records

def writeStudents(students):
    file=open('students.txt', 'w')
    for s in students:
        file.write(f"{s['id']},{s['last_name']},{s['first_name']},{s['second_name']},{s['email']},{s['start_year']},{s['program']}\n")
    file.close()

def writePassed(passed):
    file=open('passed.txt', 'w')
    for r in passed:
        file.write(f"{r['course_code']},{r['student_id']},{r['date']},{r['grade']}\n")
    file.close()

def searchStudent():
    print("\n=== Search Student ===")
    stds = readStudents()
    term = input("Enter student ID or name to search: ")
    results = []
    if term.isdigit():
        sid=int(term)
        for s in stds:
            if s['id'] == sid:
                results.append(s)
    else:
        search_term = term.lower()
        for s in stds:
            first_name_lower = s['first_name'].lower()
            last_name_lower = s['last_name'].lower()
            second_name_lower = s['second_name'].lower()
            
            if (search_term in first_name_lower or 
                search_term in last_name_lower or 
                search_term in second_name_lower):
                results.append(s)

    if len(results) == 0:
        print("No students found.")
    else:
        print(f"\nFound {len(results)} student(s):")
        for s in results:
            if s['second_name']:
                name = f"{s['first_name']} {s['second_name']} {s['last_name']}"
            else:
                name = f"{s['first_name']} {s['last_name']}"
            print(f"\nID: {s['id']}")
            print(f"Name: {name}")
            print(f"Email: {s['email']}")
            print(f"Start Year: {s['start_year']}")
            print(f"Program: {s['program']}")

def searchCourse():
    print("\n=== Search Course ===")
    crs = readCourses()
    term = input("Enter course code or name to search: ").lower()
    results = []

    for c in crs:
        cLower = c['code'].lower()
        nLower = c['name'].lower()
        if term in cLower or term in nLower:
            results.append(c)
    
    if len(results) == 0:
        print("No courses found.")
    else:
        print(f"\nFound {len(results)} course(s):")
        for c in results:
            print(f"\nCode: {c['code']}")
            print(f"Name: {c['name']}")
            print(f"Credits: {c['credits']}")
            print(f"Teacher(s): {', '.join(c['teachers'])}")

def courseCompletion():
    print("\n=== Add Course Completion ===")
    stds = readStudents()
    crs = readCourses()
    psd = readPassed()

    cc = input("Enter course code: ").upper()
    courseFound = False
    for c in crs:
        if c['code'] == cc:
            courseFound = True
            break
    
    if not courseFound:
        print("Error: Course code not found!")
        return
    
    sid_input = input("Enter student ID: ")
    if not sid_input.isdigit():
        print("Error: Invalid student ID")
        return
    sid = int(sid_input)

    studentFound = False
    for s in stds:
        if s['id'] == sid:
            studentFound = True
            break
    
    if not studentFound:
        print("Error: Student ID not found!")
        return
    
    dt = input("Enter completion date (YYYY-MM-DD): ")
    date_parts = dt.split('-')
    if len(date_parts) != 3:
        print("Error: Invalid date format!")
        return
    if not (date_parts[0].isdigit() and date_parts[1].isdigit() and date_parts[2].isdigit()):
        print("Error: Invalid date format!")
        return
    
    # Get grade
    grade_input = input("Enter grade (1-5): ")
    if not grade_input.isdigit():
        print("Error: Invalid grade")
        return
    
    gr = int(grade_input)
    if gr <1 or gr >5:
        print("Error: Grade must be between 1 and 5")
        return
    
    rec = None
    for r in psd:
        if r['course_code'] == cc and r['student_id'] == sid:
            rec = r
            break
    
    if rec:
        if gr > rec['grade']:
            rec['grade'] = gr
            rec['date'] = dt
            print(f"\nGrade updated to {gr} for course {cc}")
        else:
            print(f"\nExisting grade ({rec['grade']}) is better or equal. No update made.")
    else:
        psd.append({'course_code': cc, 'student_id': sid, 'date': dt, 'grade': gr})
        print(f"\nCourse completion added: {cc} for student {sid} with grade {gr}")
    
    writePassed(psd)

def record():
    print("\n=== Show Student's Record ===")
    stds = readStudents()
    crs = readCourses()
    psd = readPassed()
    
    sid_input = input("Enter student ID: ")
    if not sid_input.isdigit():
        print("Error: Invalid student ID")
        return
    sid = int(sid_input)

    student = None
    for s in stds:
        if s['id'] == sid:
            student = s
            break
    
    if not student:
        print("Error: Student not found!")
        return
    
    if student['second_name']:
        name = f"{student['first_name']} {student['second_name']} {student['last_name']}"
    else:
        name = f"{student['first_name']} {student['last_name']}"

    print(f"\n{'='*60}")
    print(f"Student: {name}")
    print(f"ID: {student['id']}")
    print(f"Email: {student['email']}")
    print(f"Program: {student['program']}")
    print(f"Start Year: {student['start_year']}")
    print(f"{'='*60}")
    
    rec = []
    for p in psd:
        if p['student_id'] == sid:
            rec.append(p)
    
    if len(rec) == 0:
        print("\nNo courses completed yet.")
    else:
        print(f"\nCompleted Courses ({len(rec)}):")
        print(f"{'Course Code':<12} {'Course Name':<40} {'Credits':<8} {'Grade':<6} {'Date'}")
        print("-" * 90)
        
        tot = 0
        for r in rec:
            course = None
            for c in crs:
                if c['code'] == r['course_code']:
                    course = c
                    break
            
            if course:
                print(f"{course['code']:<12} {course['name']:<40} {course['credits']:<8} {r['grade']:<6} {r['date']}")
                tot += course['credits']
        
        print("-" * 90)
        print(f"Total Credits: {tot}")

def main():
    while True:
        menu()
        ch = input("Enter your choice (1-6): ")
        
        if ch == '1':
            addStudent()
        elif ch == '2':
            searchStudent()
        elif ch == '3':
            searchCourse()
        elif ch == '4':
            courseCompletion()
        elif ch == '5':
            record()
        elif ch == '6':
            print("\nThank you for using our system!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()