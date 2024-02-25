from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True )
    profile_pic = models.FileField(verbose_name="تصویر کاربری" , upload_to='Profile_pics' , null = True , blank = True )
    first_name = models.CharField(max_length=100 , verbose_name="نام" , null = True , blank = True )
    last_name = models.CharField(max_length=100 , verbose_name="نام خانوادگی" , null = True , blank = True )
    bio = models.TextField(verbose_name="متن خلاصه" , null = True , blank = True)


    def get_absolute_url(self):
        return reverse("account:profile", args=[self.user.username])




    def __str__(self):
        return self.user.username



    class Meta :
        db_table = 'profile'
        verbose_name_plural =  'حساب کاربری'



