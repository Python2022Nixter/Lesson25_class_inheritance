# from SchoolProject1.school_v1 import Student
import school_v2 as school


students = [] # Students list

admin = school.Administrator("John", "Doe", "e@r.com")  # instance of Administrator class
print (admin)

students = admin.read_students_from_csv()
admin.remove_student(10,students)


for s in students:
    print (s)
    pass



