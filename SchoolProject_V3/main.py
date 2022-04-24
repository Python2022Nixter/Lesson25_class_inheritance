# from SchoolProject1.school_v1 import Student
import school_v2 as school


students = [] # Students list

admin = school.Administrator("John", "Doe", "e@r.com")  # instance of Administrator class
# print (admin)

students = admin.read_students_from_csv()
admin.remove_student(10,students)
admin.remove_student(15,students)
admin.write_students_to_csv(students)

teachers = admin.read_teachers_from_csv()
[print(teacher) for teacher in teachers]
# print(type(students))
# print(type(students[0]))
# print(students[0])
# print(students[0].first_name)


# for s in students:
#     print (s)
#     pass



