from random import randint
from models import *
from faker import Faker
connect('employees')

fake = Faker()

result = Employee.objects(county_id=577)
for emp in result:
    print(emp.county_id)

















