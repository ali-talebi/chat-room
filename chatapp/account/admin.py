from django.contrib import admin
from .models import Profile
from django.utils.html import format_html
# Register your models here.

@admin.register(Profile)
class Profile_Admin(admin.ModelAdmin):
    list_display = ('user' , "show_username" , "show_name"  , "show_family" , "show_email"   )

    def show_username(self , obj ) :
        return obj.user.username

    def show_name(self , obj ) :
        return obj.first_name

    def show_family(self , obj ) :
        return obj.last_name

    def show_email(self , obj ):
        return obj.user.email





