# def person():
#     employees = ['John Smith', 'Stacy Maggie', 'Ike Mmadu', 'Nnenna Duru']
#     staff = {"SBA": 'Tony Izuogu', "SBA": 'Mark Owen', "SBA": 'James Oaths'}
#     SBA = ['Anthony Izuogu', 'Mark Johnson', 'James Oats']
#     SBA.append('Wendy Madison')
#     first_name = "Tony"
#     last_name = "Jones"
#     position = "Plumber"
#     PTO = "On"
#     Remark = "PTO Status :"
#     Floor = "61"
#     Location = "Assigned Floor :"
#     print(f"Welcome {first_name.upper()}, {last_name.upper()}")
#     print(Remark, PTO.upper())
#     print(Location, Floor)
#     print(employees[2], employees)
#     print(staff)
#     print(SBA)
#     employees.pop()
    
#     print(employees)

# # person()

print("##### EMPLOYEE'S PAY COMPUTATION ### ")
print('')

def pay():
    payRate = 50
    hours = 40
    gross = payRate * hours
    tax = (gross/100) * 18
    net = gross - tax
    annualGross = gross * 52
    annualNet = net * 52
    print('Weekly Gross:'.upper())
    print(gross)
    print('****')
    print('Weekly Net:'.upper())
    print(net)
    print('****')
    print('Annual Gross:'.upper())
    print(annualGross)
    print('****')
    print('Annual Net:'.upper())
    print(annualNet)

    payLog = [11, 10.5, 18, 23, 24, 30, 45]
    for item in payLog:
        print(f'Pay History: {item}')
        

pay()




