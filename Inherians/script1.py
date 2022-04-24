

class Person:
    __counter = 0

    def __init__(self, email, name, tel):
        self.email = email
        self.name = name
        self.tel = tel
        Person.__counter += 1
        self.id = Person.__counter

    def __str__(self) -> str:
        return f"id: {self.id}\nname: {self.name}\nemail: {self.email}\ntel: {self.tel}"

    def startWorking(self):
        print(f"I'm working, {self.name}")


class Teacher(Person):
    def __init__(self, email, name, tel, employement_date, salary):
        super().__init__(email, name, tel)
        self.employement_date = employement_date
        self.salary = salary

    def __str__(self) -> str:
        return super().__str__() + f"\nemployement_date: {self.employement_date}\nsalary: {self.salary}\n"

    def startWorking(self):
        print(f"I'm teaching, {self.name}")


class Student(Person):
    """Class Student

    Args:
        Person (Person): class Student inherits from Person
    """
    def __init__(self, email, name, tel, course_name, registration_date):
        """Initialize Student class

        Args:
            email (str): email of the student
            name (str): name of the student
            tel (str): telephone number of the student
            course_name (str): name of the course
            registration_date (str): date of registration
        """
        super().__init__(email, name, tel)
        self.course_name = course_name
        self.registration_date = registration_date

    def __str__(self) -> str:
        return super().__str__() + f"\ncourse_name: {self.course_name}\nregistration_date: {self.registration_date}\n"

    def startWorking(self):
        print(f"I'm studying, {self.name}")

    def enroll_course(self, course_name):
        self.course_name = course_name
        print(f"{self.name} enrolled in {self.course_name}")

    pass

class JuniorStudents(Student, Person): # Multiple inheritance - Множественное наследование
    
    pass


t1 = Teacher("t1@gmail.com", "T1", "0123456789", "math", 5000)
t1.startWorking()
print(t1)


s1 = Student("s1@gmail.com", "S1", "0123456789", "math", "25/12/2019")
s1.startWorking()
print(s1)
s1.enroll_course("python")
print(s1)
print(s1.__doc__)
print(s1.__init__.__doc__)
print(print.__doc__)

# issubclass(), isinstance(), is - operator, __bases__ - class attribute
print("\n----- issubclass(), isinstance(), is() - operator, __bases__ - class attribute-----\n\n")
print(f"issubclass(Student, Person): {issubclass(Student, Person)}") # Student is a subclass of Person - Студент является подклассом Персоны
print(f"isinstance(s1, Student): {isinstance(s1, Student)}") # s1 is an instance of Student - s1 является экземпляром Студента
print(f" __bases__: {Student.__bases__}") # __bases__ - атрибут класса, возвращает кортеж классов, наследующих от данного класса
print(f"__bases__ JuniorStudents: {JuniorStudents.__bases__}") # __bases__ - атрибут класса, возвращает кортеж классов, наследующих от данного класса