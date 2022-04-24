import pathlib

STUDENTS_CSV_FILE = "students.csv"  

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
    def __init__(self, first_name: str, last_name: str, email: str, employement_date: str, salary: int):
        super().__init__(first_name, last_name, email)
        self.employement_date = employement_date
        self.salary = salary
    
    def __str__(self) -> str:
        return super().__str__() + f"\nemployement_date = {self.employement_date:20s}, salary = {self.salary:5d}"
    
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
        headers = []
        students_strings = []
        students = []
        path_to_file = pathlib.Path(__file__).parent.joinpath(STUDENTS_CSV_FILE) 
        print(path_to_file)       
        with open(path_to_file) as f:
            headers = f.readline()        
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
        
        return
    pass