from django.db import models
from django.contrib.auth.models import User
from django.db import models
class userdetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    dob=models.DateField(default='2007-03-08')
    phonenumber = models.IntegerField()
    address=models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    urlfield=models.URLField()
    image = models.ImageField(upload_to='userdetails/')


    def __str__(self):
        return '{}'.format(self.name)
class academicdetails(models.Model):
    # user = models.OneToOne(User,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    yoj = models.DateField()
    yop = models.DateField()
    qualification = models.CharField(max_length=200)
    university=models.CharField(max_length=200)
    institution=models.CharField(max_length=200)
    mark=models.IntegerField()
    desc=models.CharField(max_length=200)

class skill(models.Model):
    # user = models.OneToOne(User,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill1 = models.CharField(max_length=200)
    skill2 = models.CharField(max_length=200)
    skill3 = models.CharField(max_length=200)
class exp(models.Model):
     # user = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

class project(models.Model):
     # user = models.ForeignKey(User,on_delete=models.CASCADE)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     projectname = models.CharField(max_length=200)
     projectdescription = models.CharField(max_length=200)
     language = models.CharField(max_length=200)
     projectimage = models.ImageField(upload_to='project/')

class cert(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     certifications = models.CharField(max_length=200)


     # country = models.CharField(max_length=200)
     # state = models.CharField(max_length=200)

# Create your models here.
