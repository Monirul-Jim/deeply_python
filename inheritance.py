class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
             print(f"this employee name is {self.name} and his id number is {self.id}")


class Programmer(Employee):
    def showLanguage(self):
        print(f'this progamer name{self.name} and his id number {self.id} ')
a=Employee("rahim",400)
a.showDetails()
b=Programmer("monirul",40000)
b.showLanguage()