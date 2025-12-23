class Student:
    students = {}

    def __init__(self, name, age, gender, phone, desc):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.desc = desc

    def __str__(self):
        pass

    @classmethod
    def getstudnets(cls):
        file_r = None
        file_w = None
        try:
            file_r = open('student.txt', 'r', encoding='utf-8')
        except:
            file_w = open('student.txt', 'w', encoding='utf-8')
        content = file_r.read()
        if len(content) == 0:
            cls.students = {}
        else:
            datas = eval(content)
            # cls.students = {i["name"]:Student(i["name"],i["age"],i["gender"],i["phone"],i["desc"])for i in datas}
            cls.students = datas
        print(f'所有学生信息：{cls.students}')
        if file_r is not None:
            file_r.close()
        if file_w is not None:
            file_w.close()
        return cls.students

    @classmethod
    def getstudnetinfo(cls, name):
        return cls.students[name]

    def add_student(self, student):
        self.students[student.name] = student.__dict__
        return True

    @classmethod
    def delete_student(cls, name):
        cls.students.pop(name)

    @classmethod
    def save_students(cls):
        with open('student.txt', 'w', encoding='utf') as file:
            result = str(cls.students)
            file.write(result)


if __name__ == '__main__':
    # Student('张三',23,'男',"131200893298",'')
    # print(Student)
    Student.getstudnets()
