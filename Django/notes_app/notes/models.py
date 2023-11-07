from django.db import models
from django.db import models
from django.contrib.auth import authenticate

class Category(models.Model):
    title = models.CharField(max_length=30)
    objects = models.Manager()

    class Meta:
        db_table = 'category'


class Note(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    reminder = models.CharField(max_length=30, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='category')
    objects = models.Manager()

    class Meta:
        db_table = 'note'




# --------------------------------------------------

class Region(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        db_table = 'region'


class Country(models.Model):
    name = models.CharField(max_length=40)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='countries')

    class Meta:
        db_table = 'country'

    def str(self):
        return f"{self.name} in {self.region}"


class Location(models.Model):
    street_address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=15, null=True, blank=True)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.SET_DEFAULT, default=1, related_name='locations')

    class Meta:
        db_table = 'locations'


class Job(models.Model):
    JOB_TITLE = [
        (1, 'CEO'),
        (2, 'CTO'),
        (3, 'PM'),
        (4, 'Business Analytics'),
        (5, 'QA'),
        (6, 'Designer'),
        (7, 'Developer'),
    ]

    title = models.IntegerField(choices=JOB_TITLE, default=1)
    min_salary = models.PositiveIntegerField()
    max_salary = models.PositiveIntegerField()

    @property
    def range(self):
        return self.max_salary - self.min_salary

    class Meta:
        db_table = 'job'


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    hire_data = models.DateField(auto_now=True)
    salary = models.PositiveIntegerField()

    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    manager= models.ForeignKey('self', on_delete=models.PROTECT)
    department_id = models.ForeignKey('Department', on_delete=models.CASCADE)

    class Meta:
        db_table = 'employees'


class Department(models.Model):
    name = models.CharField(max_length=30)
    manager = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True, related_name='departament_manager')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'departments'


class jobHistory(models.Model):
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(null=True)

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    class Meta:
        db_table = 'djob_history'


