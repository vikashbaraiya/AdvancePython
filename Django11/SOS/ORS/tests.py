from django.test import TestCase
from .models import student

class TestModel(TestCase):
    form = student(firstName = "ram", lastName = "dev",mobileNumber = "988978783", email = "ram@gmail.com", password= "ram1234" )
    form.save()
    print("Data Saved")
