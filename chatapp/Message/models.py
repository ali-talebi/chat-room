from django.db import models
from account.models import Profile
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Sender(models.Model):
    sender1 = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="کاربر فرستنده", null=True, blank=True)


    def __str__(self):

        return self.sender1.user.username


    class Meta:
        verbose_name_plural = "ارسال کنندگان"




class Reciver(models.Model):
    reciver1 = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="کاربر دریافت کننده", null=True, blank=True)


    def __str__(self):

        return self.reciver1.user.username


    class Meta:
        verbose_name_plural  = "دریافت کنندگان"








class TextToText(models.Model):
    sender1 = models.ForeignKey(User , related_name = "writer", on_delete=models.CASCADE , verbose_name="کاربر فرستنده" , null = True , blank = True )
    reciver1 = models.ForeignKey(User , related_name="reader" , on_delete=models.CASCADE , verbose_name= "کاربر دریافت کننده"  , null = True , blank=True )
    time = models.DateTimeField(verbose_name= "تاریخ پیام" , default=timezone.now   )
    edit = models.DateTimeField(verbose_name= "تاریخ تغییر "  , auto_now = True )
    text = models.TextField()


    def __str__(self):
        return f"{self.id}"

    class Meta :
        db_table = 'TextToText'
        verbose_name_plural  = "پیام های فرستاده شده "