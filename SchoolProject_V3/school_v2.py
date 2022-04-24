import pathlib

STUDENTS_CSV_FILE = "students.csv"  
TEACHERS_CSV_FILE = "teachers.csv"

class Person:
    __counter = 0
    
    def __init__(self, first_name: str, last_name: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.id = Person.__counter
        Person.__counter += 1
    
    def __str__(self) -> str:
        return f"id = {self.id:5d}, first_name = {self.first_name:20s}, last_name = {self.last_name:20s}, email = {self.email:35s}"
    
    pass

class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, email: str, salary: int, speciality: str):
        super().__init__(first_name, last_name, email)
        self.salary = salary
        self.speciality = speciality
    
    def __str__(self) -> str:
        return super().__str__() + f"\nsalary = {self.salary:10d}, speciality = {self.speciality:10s}"
    pass
   
    def to_csv_string(self) -> str:
        return f"{self.id},{self.first_name},{self.last_name},{self.email},{self.age},{self.group}"
        
    
    pass

class Student(Person):
    
    def __init__(self, first_name: str, last_name: str, email: str, age: int, group: str ) -> None:
        super().__init__(first_name, last_name, email)
        self.age = age
        self.group = group      
        pass
    
    def __str__(self) -> str:
        return f"{super().__str__()}, age = {self.age}, group = {self.group}"
        
    def ask_teacher(self, teacher_mail: str = "admin@corp.com") -> None:
        print (F"Student {self.last_name} sending mail to: {teacher_mail}")        
        pass
    
    def send_homework(self, teacher_mail: str = "admin@corp.com") -> None:
        print (F"Student {self.last_name} passing homework to: {teacher_mail}")        
        pass

    def register_for_exam(self, exam_name: str) -> None:
        print (F"Student {self.last_name} registering for exam: {exam_name}")        
        pass  
    
    def to_csv_string(self) -> str:
        return f"{self.id},{self.first_name},{self.last_name},{self.email},{self.age},{self.group}"
    pass

class Administrator(Person):
    
    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        super().__init__(first_name, last_name, email)     
        pass
    
    def __str__(self) -> str:
        return super().__str__()
    
    def add_new_student(self, new_student: Student, students: list[Student]):
        
        pass
    
    def remove_student(self, student_id: int, students: list[Student]):
        for i in range(len(students)):
            if students[i].id == student_id: del_ind = i
            pass
        students.remove(students[del_ind])        
        
        pass
    
    def change_student(self, student_id: int, students: list[Student]):
        
        pass
    
    def read_students_from_csv(self) -> list[Student]:
        # STEP1: read SCV file
        students_strings = []
        students = []
        if pathlib.Path(STUDENTS_CSV_FILE).exists():
            path_to_file = pathlib.Path(STUDENTS_CSV_FILE)
        else:
            path_to_file = pathlib.Path(__file__).parent.joinpath(STUDENTS_CSV_FILE) 
        # print(path_to_file)       
        with open(path_to_file) as f:
            self.student_headers = f.readline()        
            students_strings = f.readlines()          
            pass
        
        # STEP2: create list - students
        for next_row in students_strings:
            # create Student
            # 2,Yance,Ilbert,yilbert1@meetup.com,87,C#
            stud_data = next_row.strip().split(",")
            first_name = stud_data[1]
            last_name = stud_data[2]
            email = stud_data[3]
            age = int (stud_data[4])
            group = stud_data[5]

            next_student = Student(first_name, last_name, email, age, group)
            
            # add to list
            students.append(next_student)            
            pass
        
        
        
        return students
    
    def write_students_to_csv(self, students: list[Student]) -> None:
        # create string
        
        csv_string_student = self.student_headers
        
        for next_student in students:
            csv_string_student += next_student.to_csv_string() + "\n"
            pass
        
        
        
        # write to file
        with open(STUDENTS_CSV_FILE, "w") as f:
            f.write(csv_string_student)
            pass
        return
    
    def read_teachers_from_csv(self) -> list[Teacher]:
        # STEP1: read SCV file
        teachers_strings = []
        teachers = []
        if pathlib.Path(TEACHERS_CSV_FILE).exists():
            path_to_file = pathlib.Path(TEACHERS_CSV_FILE)
        else:
            path_to_file = pathlib.Path(__file__).parent.joinpath(TEACHERS_CSV_FILE) 
        # print(path_to_file)       
        with open(path_to_file) as f:
            self.student_headers = f.readline()        
            teachers_strings = f.readlines()          
            pass
        # STEP2: create list - teachers
        for next_row in teachers_strings:
            # create Teacher
            # 2,Yance,Ilbert,
            teach_data = teachers_strings[0].strip().split(",")
            first_name = teach_data[1]
            last_name = teach_data[2]
            email = teach_data[3]
            salary = int (teach_data[4])
            spacialities = teach_data[5]
        
            next_teachers = Teacher(first_name, last_name, email, salary, spacialities)
        
            teachers.append(next_teachers)
        
        return teachers
    pass