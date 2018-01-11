from models import *
from faker import Faker
from random import  randint
fake = Faker()


def generate(value):
    i = 0
    while i < value:
        e = Employee()
        e.county_id = str(randint(1, 10000))
        e.last_name = fake.last_name()
        e.first_name = fake.first_name()

        e.address = Address()
        e.address.street1 = fake.building_number() + " " + fake.street_name() + " " + fake.street_suffix()
        if randint(1, 10) > 6:
            e.address.street2 = fake.secondary_address()
        e.address.city = fake.city()
        e.address.state = fake.state_abbr()
        e.address.zip = fake.zipcode()
        e.address.save()
        e.save()
        print(e.address.street1)
        i += 1