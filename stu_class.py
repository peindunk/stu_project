# ２　将学生信息管理程序　把用于存储学生信息的字典　换成用student类型对象来存储学生信息
class Student:
    def __init__(self , name ,age = 0,score = 0):
        self.name = name
        self.age = age
        self.score = score
    
    