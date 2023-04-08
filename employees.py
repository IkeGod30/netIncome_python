class Employee():
    print('EMPLOYEE RECORD')
    Vendor = "Vendor: Rapport"
    
    def __init__(self, first_name, last_name, role):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

Ave = Employee(first_name="Avelima", last_name="Cortez", role="Welcome Host")
print(Ave.first_name.upper(), Ave.last_name.upper(), Ave.role.upper())
print(Ave.Vendor)
