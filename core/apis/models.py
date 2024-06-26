from django.db import models


# Create your models here.
# Creating the comapany models
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    about = models.TextField()
    company_type = models.CharField(
        max_length=100,
        choices=(
            ("IT", "IT"),
            ("non_IT", "non_IT"),
            ("Mobiles_phone", "Mobiles_phone"),
        ),
    )
    create_At = models.DateTimeField(auto_now=True)
    is_Active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + self.location


# Employee Models
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    about = models.TextField()
    positon = models.CharField(
        max_length=100,
        choices=(
            ("Manager", "manager"),
            ("Software Developer", "Software Developer"),
            ("Project Leader", "Project leader"),
        ),
    )
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
