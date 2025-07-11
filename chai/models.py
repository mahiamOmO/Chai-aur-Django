from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML','MASALA'),
        ('AL','MASALA'),
        ('BL','KIWI'),
        ('XL','PLAIN'),
        ('XL','GINGER'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    Type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')


    def __str__(self):
        return self.name 
    

    # One to Many
class ChaiReview(models.Model):
    chai =  models.ForeignKey(ChaiVarity,on on_delete= models.CASACDE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chai_reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username}' review for {self.chai.name}'

# Many to many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVarity, related_name='stores')

    def __str__(self):
        return self.name

# One to one

class ChaiCertificate(models.Model):
    chai = models.OneToOneFiels(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    on_delete = models.CASACADE,related_name='certificate')
    certificate_number = models.CharField(max_length= 100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name} - {self.certificate_number}'