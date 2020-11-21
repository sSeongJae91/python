#class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕! " + to_name + " 나는 " + self.name)


p = Person("성재", 30)
p.say_hello("워니")


#class 와 상속(inheritance)
class Police(Person): #Police(자식)는 Person(부모)을 상속
    def arrest(self, to_arrest):
        print("넌 체포됐다, " + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("다음엔 이걸 만들자 " + to_program)

a = Person("성재", 30)
b = Police("성재", 30)
b.say_hello("워니")
b.arrest("철수")