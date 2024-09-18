from person import Person
from employee import Employee
from employee import Employee

class Teacher(Person,Employee):
    def teach():
        return "Teach"
    

Tung = Teacher()
print(Tung.get_fired())