from random import randint
from models import *
from faker import Faker
from generator import generate
from mongoengine import *
import anvil.server

connect('employees')
anvil.server.connect("5VMSTHCN6L3XNRVQ-5W2TDAKL3ORXSJBV")



if not Employee.objects():
    generate(20)

@anvil.server.callable
def from_mongo():
    result = Employee.objects()
    lst = list()
    for emp in result:
        #print(emp.county_id, emp.last_name, emp.first_name, emp.address.street1)
        lst.append(emp.to_json())
    print(lst)
    return lst
anvil.server.wait_forever()
















