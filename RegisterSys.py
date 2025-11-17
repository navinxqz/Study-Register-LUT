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

def read_students():
    with open('students.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
        return [{'id': int(p[0]), 'last_name': p[1], 'first_name': p[2], 
                'second_name': p[3], 'email': p[4], 'start_year': int(p[5]), 'program': p[6]} 
                for p in [line.split(',') for line in lines]]

def add_student():
    print("\n=== Add New Student ===")
    stds = read_students()

    while True:     #sid
        try:
            sid = int(input("Enter student ID: "))
            if any(s['id'] == sid for s in stds):
                print("Error: Student ID already exists!")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer for student ID")
    
    ln = input("Enter last name: ")
    fn = input("Enter first name: ")
    sn = input("Enter second name (press Enter if none): ")
    em = input("Enter email: ")
    
    while True:
        try:
            yr = int(input("Enter starting year: "))
            break
        except ValueError:
            print("Error: Please enter a valid year")
    
    progs = ['CE', 'EE', 'ET', 'ME', 'SE']
    while True:
        prog = input("Enter program (CE/EE/ET/ME/SE): ").upper()
        if prog in progs:
            break
        print(f"Error: Program must be one of {', '.join(progs)}")
    
    stds.append({'id': sid, 'last_name': ln, 'first_name': fn,'second_name': sn, 'email': em, 'start_year': yr, 'program': prog})
    
    write_students(stds)
    print(f"\nStudent {fn} {ln} (ID: {sid}) added successfully!")
    
def read_courses():
    with open('courses.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
        return [{'code': p[0], 'name': p[1], 'credits': int(p[2]), 'teachers': p[3:]} 
                for p in [line.split(',') for line in lines]]


def read_passed():
    with open('passed.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
        return [{'course_code': p[0], 'student_id': int(p[1]), 'date': p[2], 'grade': int(p[3])} 
                for p in [line.split(',') for line in lines]]

def write_students(students):
    with open('students.txt', 'w') as f:
        for s in students:
            f.write(f"{s['id']},{s['last_name']},{s['first_name']},{s['second_name']},{s['email']},{s['start_year']},{s['program']}\n")

def write_passed(passed):
    with open('passed.txt', 'w') as f:
        for r in passed:
            f.write(f"{r['course_code']},{r['student_id']},{r['date']},{r['grade']}\n")

def search_student():
    print("\n=== Search Student ===")
    stds = read_students()
    term = input("Enter student ID or name to search: ")
    
    try:
        sid = int(term)
        res = [s for s in stds if s['id'] == sid]
    except ValueError:
        t = term.lower()
        res = [s for s in stds if t in s['first_name'].lower() or t in s['last_name'].lower() or t in s['second_name'].lower()] #lc
    
    if not res:
        print("No students found.")
    else:
        print(f"\nFound {len(res)} student(s):")
        for s in res:
            nm = f"{s['first_name']} {s['second_name']} {s['last_name']}" if s['second_name'] else f"{s['first_name']} {s['last_name']}"
            print(f"\nID: {s['id']}")
            print(f"Name: {nm}")
            print(f"Email: {s['email']}")
            print(f"Start Year: {s['start_year']}")
            print(f"Program: {s['program']}")

def search_course():
    print("\n=== Search Course ===")
    crs = read_courses()
    term = input("Enter course code or name to search: ").lower()
    res = [c for c in crs if term in c['code'].lower() or term in c['name'].lower()]
    
    if not res:
        print("No courses found.")
    else:
        print(f"\nFound {len(res)} course(s):")
        for c in res:
            print(f"\nCode: {c['code']}")
            print(f"Name: {c['name']}")
            print(f"Credits: {c['credits']}")
            print(f"Teacher(s): {', '.join(c['teachers'])}")

def add_course_completion():
    print("\n=== Add Course Completion ===")
    stds = read_students()
    crs = read_courses()
    psd = read_passed()

    cc = input("Enter course code: ").upper()
    if not any(c['code'] == cc for c in crs):
        print("Error: Course code not found!")
        return
    
    try:
        sid = int(input("Enter student ID: "))
    except ValueError:
        print("Error: Invalid student ID")
        return
    
    if not any(s['id'] == sid for s in stds):
        print("Error: Student ID not found!")
        return
    
    dt = input("Enter completion date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(dt, '%Y-%m-%d')
    except ValueError:
        print("Error: Invalid date format!")
        return
    
    try:
        gr = int(input("Enter grade (1-5): "))
        if gr < 1 or gr > 5:
            print("Error: Grade must be between 1 and 5")
            return
    except ValueError:
        print("Error: Invalid grade")
        return
    
    rec = next((r for r in psd if r['course_code'] == cc and r['student_id'] == sid), None)
    
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
    
    write_passed(psd)

def show_student_record():
    print("\n=== Show Student's Record ===")
    stds = read_students()
    crs = read_courses()
    psd = read_passed()
    
    try:
        sid = int(input("Enter student ID: "))
    except ValueError:
        print("Error: Invalid student ID")
        return
    
    std = next((s for s in stds if s['id'] == sid), None)
    
    if not std:
        print("Error: Student not found!")
        return
    
    nm = f"{std['first_name']} {std['second_name']} {std['last_name']}" if std['second_name'] else f"{std['first_name']} {std['last_name']}"
    print(f"\n{'='*60}")
    print(f"Student: {nm}")
    print(f"ID: {std['id']}")
    print(f"Email: {std['email']}")
    print(f"Program: {std['program']}")
    print(f"Start Year: {std['start_year']}")
    print(f"{'='*60}")
    
    recs = [p for p in psd if p['student_id'] == sid]   #using lc
    
    if not recs:
        print("\nNo courses completed yet.")
    else:
        print(f"\nCompleted Courses ({len(recs)}):")
        print(f"{'Course Code':<12} {'Course Name':<40} {'Credits':<8} {'Grade':<6} {'Date'}")
        print("-" * 90)
        
        tot = 0
        for r in recs:
            c = next((x for x in crs if x['code'] == r['course_code']), None)
            if c:
                print(f"{c['code']:<12} {c['name']:<40} {c['credits']:<8} {r['grade']:<6} {r['date']}")
                tot += c['credits']
        
        print("-" * 90)
        print(f"Total Credits: {tot}")

def main():
    while True:
        display_menu()
        ch = input("Enter your choice (1-6): ")
        
        if ch == '1':
            add_student()
        elif ch == '2':
            search_student()
        elif ch == '3':
            search_course()
        elif ch == '4':
            add_course_completion()
        elif ch == '5':
            show_student_record()
        elif ch == '6':
            print("\nThank you for using our system!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()