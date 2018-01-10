from mongoengine import *

connect('employees')


class Address(EmbeddedDocument):
    street1 = StringField(required=True)
    street2 = StringField()
    attn = StringField()
    city = StringField()
    state = StringField(max_length=2, min_length=2)
    zip = StringField(max_length=5, min_length=5)

class Department(Document):
    name = StringField()
    director = LazyReferenceField('Employee')


class Position(Document):
    department = LazyReferenceField(Department)
    description = StringField


class PayType(Document):
    name = StringField()


class PayChangeReason(Document):
    reason = StringField


class Pay(EmbeddedDocument):
    pay_type = LazyReferenceField(PayType)
    pay = DecimalField()
    pay_change_reason = LazyReferenceField(PayChangeReason)
    effective_date = DateTimeField()


class Employment(EmbeddedDocument):
    start_date = DateTimeField()
    end_date = DateTimeField()


class Person(Document):
    last_name = StringField(required=True)
    first_name = StringField(required=True)
    dob = DateTimeField()
    address = EmbeddedDocumentField(Address)
    extension = StringField()

    meta = {'allow_inheritance': True}


class Employee(Person):
    county_id = StringField()
    employments = EmbeddedDocumentListField(Employment)

















