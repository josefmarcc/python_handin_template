import names
import random
import csv


class Student():
    """ Class used to create a student with name, gender, data_sheet and img_url"""

# format stud_name, course_name, teacher, ects, classroom, grade, img_url

    def __init__(self, name, gender, data_sheet, img_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.img_url = img_url


    
    def __repr__(self):
        return '%r, %r, %r, %r' % (self.name, self.gender, 
                                     self.data_sheet, self.img_url)


    def get_avg_grade(self):
        total_sum = sum(self.data_sheet.get_grades_as_list())
        total_len = len(self.data_sheet.get_grades_as_list())
        return total_sum / total_len

    def __iter__(self):
        return iter([self.name, self.gender, self.data_sheet , self.img_url])

class Course():
    """ Create a course with a name, classroom, teacher, ETCS, Optional grade """

    def __init__(self, name, classroom, teacher, ETCS, grade=0):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade

    def __repr__(self):
        return '(%r, %r, %r, %r, %r)' % (self.name, self.classroom, self.teacher, self.ETCS, self.grade)

class DataSheet():
    """ Create a DataSheet that takes multiple courses """

    def __init__(self, *courses):
        self.courses = courses

    def get_grades_as_list(self):
        grade_list = []
        for element in self.courses:
            grade_list.append(element.grade)
        return grade_list


def student_generator(n):
    genders = ["male", "female"]
    course_name_list = ["Python", "JavaScript",
                        "Functional Programming", "Math", "DataScience", "C++"]
    teachers = ["Lars", "Thomas", "Kim", "Jon"]
    grade_list = [0, 2, 4, 7, 10, 12]
    student_list = []

    for n in range(n):
        course = Course(random.choice(course_name_list), random.choice(
            range(0, 30)), random.choice(teachers), 15, random.choice(grade_list))
        for n in range(n):
            student = Student(names.get_full_name(),
                              random.choice(genders), course, "img")
            student_list.append(student)

    return student_list


## Write the result to a CSV file
def write_list_to_file(output_file, lst):

    csv.register_dialect('myDialect', delimiter=',')

    with open(output_file, 'w') as output_file:
        output_writer = csv.writer(output_file, dialect = "myDialect")
        print(lst[0])
        fields = ["Name", "Gender", "Classes", "Image url", "Grades"]
        output_writer.writerow(fields)
        for student in lst:
            output_writer.writerow(list(student))

course1 = Course("Python", 2, "Thomas", 30, 12)
course2 = Course("JS", 2, "Lars", 30, 10)
course3 = Course("Functional Programming", 2, "Kim", 30, 7)

d1 = DataSheet(course1, course2, course3)
student1 = Student("Jesus", "male", d1, "img")

print(d1.get_grades_as_list())
print(student1.get_avg_grade())

student_gen_list = student_generator(5)

write_list_to_file("student_list.csv", student_gen_list)


## Read student data into a list of students from a CSV file as a list

def read_csv_filecontent(file):
    list_of_students = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for lines in csv_reader:
            name = lines[0]
            gender = lines[1]
            data_sheet = lines[2]
            img_url = lines[3]
            s = Student(name, gender, data_sheet, img_url)

            list_of_students.append(s)

    return list_of_students

st_lst = read_csv_filecontent("./student_list.csv")

for Student in st_lst:
    student_avg = Student.data_sheet
    print(student_avg)

