from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class property(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    property_type=models.CharField(
        max_length=20,
        choices=[
            ('PG','PG'),
            ('Coliving','Coliving'),
            ('Home','Home')
        ]
    )
    stay_type=models.CharField(max_length=20)
    owner_no=models.CharField(
        max_length=10,
        validators=[
            RegexValidator(regex=r'^\d{10}$',
                           message="phone number must contain 10 digites")
        ])
    property_img=models.ImageField(upload_to='property/',blank=True,null=True)

    def __str__(self):
        return self.name #to visible in admin

class property_details(models.Model):
    property_de=models.ForeignKey(property,related_name="p_details",on_delete=models.CASCADE)
    property_owner=models.CharField(max_length=20)
    category_type=models.CharField(max_length=10)
    security_deposit=models.IntegerField()
    location=models.CharField(max_length=50)
    location_link=models.URLField(blank=False,null=False)
    rent=models.IntegerField(blank=False,null=False)

    def __str__(self):
        return self.property_owner

class property_interior_img(models.Model):
    property_interior=models.ForeignKey(property,related_name="p_interior",on_delete=models.CASCADE)
    property_interior_img=models.ImageField(upload_to="interior/",blank=True,null=True)

    