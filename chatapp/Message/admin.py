from django.contrib import admin
from .models import Sender  , Reciver , TextToText


@admin.register(Reciver)
class RiciverAdmin(admin.ModelAdmin):
    list_display = ('UserName' ,  )

    def UserName(self , obj ):
        return obj.reciver1.user.username


@admin.register(Sender)
class SenderAdmin(admin.ModelAdmin):
    list_display = ('UserName' , )

    def UserName(self, obj):
        return obj.sender1.user.username

@admin.register(TextToText)
class TextToTextAdmin(admin.ModelAdmin):
    list_display = ('sender1' , 'reciver1'  )






