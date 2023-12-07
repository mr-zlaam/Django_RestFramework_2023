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


# Employee Models
