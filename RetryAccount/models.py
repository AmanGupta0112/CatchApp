from django.db import models
from django.contrib.auth.models import User,PermissionsMixin
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField
User_o = get_user_model()
import PIL
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from RetryAccount.constants import Interest_choice,Age_range,Gender,Income_Range
from RetryAccount.constants import Profession_choice,State_Choice,Education_choice
# Create your models here.


class UserCreateModel(User, PermissionsMixin):

    def __str__(self):
        return self.username

    class  Meta():
        db_table = "User_Credential"

class Profile(models.Model):

    user = models.OneToOneField(User_o, on_delete=models.CASCADE)
    image = models.ImageField(default = 'b4.jpg' , upload_to='profile_pics')
    # image_thumbnail = ImageSpecField(source= 'image', processors = [ResizeToFill(150,150)],format='JPEG', options = {'quality':60})

    Age = models.CharField(max_length = 50, choices = Age_range,default = 'Age')
    Gender = models.CharField(max_length = 20, choices = Gender,default='gender')
    Education = models.CharField(max_length = 100 , choices = Education_choice, default= 'Education')
    Profession = models.CharField(max_length=50,choices=Profession_choice)
    State = models.CharField(max_length= 50 ,choices = State_Choice,default='State')
    Income = models.CharField(max_length=20,choices = Income_Range,default='Income')
    Interest= MultiSelectField(choices=Interest_choice)

    def __str__(self):
        return self.user.username

    def save(self,*args,**kwargs):
        super(Profile, self).save(*args,**kwargs)

    class  Meta():
        db_table = "Profile"
