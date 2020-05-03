from B.Student import Student


class Main:
    def manager(self):
        print("How many do you want to input numbers student?")
        number = int(input())
        studentList = []
        for x in range(0, number):
            student = Student()
            print("Please, Input name: ")
            name = input()
            print("Please, Input birthday")
            birthday = input()
            print("Please, Input education")
            education = input();
            print("Please, Input homeTown")
            homeTown = input();

            # setter
            student.set_name(name)
            student.set_birthday(birthday)
            student.set_education(education)
            student.set_homeTown(homeTown)

            studentList.append(student)
        return studentList

    def show(self, studentList):
        for student in studentList:
            print(student.get_birthday())
            print(student.get_name())
            print(student.get_education())
            print(student.get_homeTown())
            print("---------------------")


main01 = Main()
studentList = main01.manager()
main01.show(studentList)
