from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import Profile
from .models import TextToText  , Reciver , Sender
from .forms import  TextToTextForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.




class TotalChatView(LoginRequiredMixin, View):




    def dispatch(self, request , *args , **kwargs  ) :
        if not request.user.is_authenticated :
            return redirect('account:login')
        return super().dispatch(request , *args , **kwargs )

    def get(self, request):
        clients = Profile.objects.all()

        return render(request, 'chat_room/gradient.html' , {'total_chat':None , 'clients' : clients})

    def post(self , request ) :
        clients = Profile.objects.all()

        return render(request, 'chat_room/gradient.html', {'total_chat': None , 'clients' : clients})



class ChatBetweenView(LoginRequiredMixin, View):
    def dispatch(self, request , *args , **kwargs  ) :
        if not request.user.is_authenticated :
            return redirect('account:login')
        return super().dispatch(request , *args , **kwargs )


    def setup(self, request, *args, **kwargs):
        self.clients = Profile.objects.all()
        self.form = TextToTextForm
        self.sender_flag = User.objects.filter(  username = request.user.username ).exists()
        self.reciver_flag = User.objects.filter(username= kwargs['username'] ).exists()


        return super().setup(request , *args , **kwargs )

    def get(self , request , username ) :
        reciver = User.objects.get(username=username)
        reciver_profile = Profile.objects.get(user__username=reciver.username)
        sender = User.objects.get(username=request.user.username)
        sender_profile = Profile.objects.get(user__username=sender.username)
        total_chats1 = TextToText.objects.filter((Q(sender1 = sender ) & Q( reciver1 = reciver)) | (Q(sender1=reciver ) & Q(reciver1=sender)) ) .order_by("id")


        return render(request, 'chat_room/window.html' , { "reciver_profile" : reciver_profile ,"sender_profile" : sender_profile  , 'form' : self.form , 'clients':self.clients , 'total_chats' : total_chats1})


    def post(self , request , username )  :

        reciver = User.objects.get(username=username)
        reciver_profile = Profile.objects.get(user__username=reciver.username )
        sender = User.objects.get(username=request.user.username)
        sender_profile = Profile.objects.get(user__username=sender.username )
        total_chats1 = TextToText.objects.filter(Q(sender1 = sender) | Q(reciver1 = reciver) | Q(sender1=reciver)| Q(reciver1=sender) ) .order_by("id")



        form = self.form(request.POST)
        if form.is_valid() :
            new_text = form.cleaned_data['text']


            if self.sender_flag and  self.reciver_flag  :
                reciver = User.objects.get(username = username )
                sender = User.objects.get(username = request.user.username )
                mess = TextToText(sender1 = sender, reciver1 = reciver, text = new_text ,  )
                mess.save()
                messages.success(request, 'پیام شما با موفقیت ثبت شده است'  , 'success' )
                return redirect('home:home')
            else :
                messages.error(request, 'در ایجاد پیام مشکلی داریم')
                return redirect('home:home')


        return render(request, 'chat_room/window.html' , {"reciver_profile" : reciver_profile ,"sender_profile" : sender_profile   , 'form' : form , 'clients':self.clients ,  'total_chats' : total_chats1 })






