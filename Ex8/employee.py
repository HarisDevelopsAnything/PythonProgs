class Employee:
    def __init__(self,name, age, sal):
        self.name= name
        self.age= age
        self.sal= sal
    def __lt__(self, other):
        return self.age<other.age
    def __gt__(self, other):
        return self.sal>other.sal
    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.sal}")
emps= list()
n= int(input("Enter the number of employees: "))
for i in range(n):
    print(f"Employee {i}:")
    name= input("Enter the name: ")
    age= int(input("Enter the age: "))
    sal= int(input("Enter the salary: "))
    emp= Employee(name, age, sal)
    emps.append(emp)
least_age= emps[0]
most_sal= emps[0]
for i in range(0, len(emps)):
    if(emps[i]<least_age):
        least_age= emps[i]
    if(emps[i]>most_sal):
        most_sal= emps[i]
print("The employee with most salary: ")
Employee.showDetails(most_sal)
print("Employee with least age: ")
Employee.showDetails(least_age)