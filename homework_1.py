class Person:
    def __init__(self, full_name,age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married



    def IntroduceMyself(self):
        mar_status = 'married' if self.is_married else 'not married'
        print(f'Hi! My full name is: {self.full_name} '
              f'and im {self.age} years old,'
              f' also im {mar_status}')

class Student(Person):
    def __init__(self, full_name,age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks


    def StudentAverageRating(self):
        total_marks = sum(self.marks.values())
        subjects = len(self.marks)
        return total_marks / subjects if subjects >0 else 0

    def IntroduceMyself(self):
        super().IntroduceMyself()#Здесь я открыл для себя возможность использования super и в подобном подходе
        print('Marks:',self.marks)
        print(f'Student Average Rating is: {self.StudentAverageRating()}')

class Teacher(Person):
    base_salary = 30000
    def __init__(self,full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def salary_bonus(self):
        bonus_years = max(self.experience - 3, 0)
        salary_with_bonus = Teacher.base_salary *((1 + 0.05) ** bonus_years)
        return salary_with_bonus

    def IntroduceMyself(self):
        super().IntroduceMyself()
        print(f'Teacher salary with bonus is:{self.salary_bonus():.2f}')


def create_student():
    students = [Student('Peter Parker', 17, False,
                        {'Math': 90, 'Chemistry': 90, 'Physics':90}),
                Student('Barry Allen', 18, True,{'Math':70, 'Chemistry':50, 'Physics': 60}),
                Student('Morty Smith', 16, False, {'Math': 77, 'Chemistry': 69, 'Physics': 49})]
    return students


students_list = create_student()
for student in students_list:
    student.IntroduceMyself()

teacher_ = Teacher ('Sensei Aleksey', 39, True, 13)
teacher_.IntroduceMyself()

