#!/usr/bin/python
#coding:utf-8

# Filename: inherit.py

class SchoolMember:#这是一个父类

    '''Represents any school member.'''

    def __init__(self, name, age):

        self.name = name

        self.age = age

        print('(Initialized SchoolMember: {0})'.format(self.name))

   
    def tell(self):

        '''Tell my details.'''

        print('Name:"{0}" Age:"{1}"'.format(self.name, self.age), end="")

 
class Teacher(SchoolMember): #这个一个派生类

    '''Represents a teacher.'''
    

    def __init__(self, name, age, salary):

        SchoolMember.__init__(self, name, age)

        self.salary = salary

        print('(Initialized Teacher: {0})'.format(self.name))
        

    def tell(self):

        SchoolMember.tell(self)

        print('Salary: "{0:d}"'.format(self.salary))
        

class Student(SchoolMember):

    '''Represents a student.'''
    

    def __init__(self, name, age, marks):

        SchoolMember.__init__(self, name, age)

        self.marks = marks

        print('(Initialized Student: {0})'.format(self.name))

   
    def tell(self):

        SchoolMember.tell(self)

        print('Marks: "{0:d}"'.format(self.marks))
        
        

t = Teacher('Mrs. Shrividya', 40, 30000)

s = Student('Swaroop', 25, 75)

print() # 打印一个空行

members = [t, s]

for member in members:

    member.tell() # 在Teacher和Student上都能工作