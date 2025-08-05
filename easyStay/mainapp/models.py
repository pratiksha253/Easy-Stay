from django.db import models

STATE_CHOICES = [
    # States
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),

    # Union Territories
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'National Capital Territory of Delhi'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
]


class Address(models.Model):
    door_number = models.PositiveIntegerField()
    floor_number = models.PositiveIntegerField()
    line1 = models.TextField(max_length=200)
    line2 = models.TextField(max_length=200)
    pincode = models.PositiveIntegerField()
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    
    def __str__(self):
        return f"Address :{self.door_number}, pin: {self.pincode}..."
    
class BuildingType(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='building_types/')
    
    def __str__(self):
        return f"{self.title.capitalize()} building"
    
class Facility(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title.capitalize()
    
    


# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(BuildingType, on_delete=models.CASCADE, related_name='building_types')
    rent_price=models.FloatField(default=00000)
    deposite=models.FloatField(default=00000)
    thumbnail=models.ImageField(upload_to='buildings/', blank=True, null=True)
    address=models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True, related_name='building_address' )
    # owner=models.CharField(max_length=100)
    # contact=models.CharField(max_length=200)
    # facility=models.CharField(max_length=500,default='Default Facility')
    facilities = models.ManyToManyField(Facility, related_name='building_facilities')
    
    def __str__(self):
        return f"Home:{self.name}"
    
class BuildingImage(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField('building_images/')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='building_images')