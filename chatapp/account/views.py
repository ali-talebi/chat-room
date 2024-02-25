from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render , redirect
from .forms import Loginform , RegisterForm , ProfileEditForm
from django.views import View
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.core.exceptions import ValidationError




# Create your views here.
class LoginView(View):

    form = Loginform



    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated :
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)


    def get(self , request ):

        return render(request , 'login_logout/just_login.html' , {'form' : self.form()} )


    def post(self , request ):
        fill_form = self.form(request.POST)
        if fill_form.is_valid():
            username = fill_form.cleaned_data.get('username')
            password = fill_form.cleaned_data.get('password')
            user = authenticate(request , username=username , password=password)
            if user  :
                login(request , user  )
                messages.success (request , 'با موفقیت وارد شدید' , 'success')
                return redirect('home:home')

            else :
                messages.error (request , 'مشکلی در وارد شدن داریم' , 'error')

        return render(request , 'login_logout/just_login.html' , {'form' :fill_form})



class RegisterView(View) :




    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated :
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request ):
        form1 = RegisterForm()

        return render(request , 'login_logout/just_signup.html' , {'form1' : form1})

    def post(self , request ):

        form1 = RegisterForm(request.POST)
        if form1.is_valid():
            new_username = form1.cleaned_data['username']
            new_email = form1.cleaned_data['email']
            new_password = form1.cleaned_data['password1']
            new_password2 = form1.cleaned_data['password2']
            if new_password != new_password2 :
                messages.error(request ,  'عدم تطابق رمز های کاربری' , 'error')
                return redirect('account:register')

            register_user = User.objects.create_user(username = new_username, email = new_email , password = new_password )
            Profile(user = register_user).save()
            login(request , register_user )
            messages.success (request ,  'با موفقیت ثبت نام شدید'  , 'success' )
            return redirect('home:home' )



        else :
            messages.error (request , 'در ثبت نام مشکلی وجود دارد ' , 'error')


        return render(request , 'login_logout/just_signup.html' , {'form1' : form1})


class LogoutView(LoginRequiredMixin , View ) :

    login_url = "login/"
    def get(self, request ) :
        logout(request)
        messages.success(request , 'با موفقیت خارج شدید' , 'success' )
        return redirect('account:login')

    def post(self, request ) :
        logout(request)
        messages.success(request , 'با موفقیت خارج شدید' , 'success' )
        return redirect('account:login')




class ProfileView(LoginRequiredMixin , View ) :
    login_url = "login/"
    def get(self ,request , username  ) :
        profile = Profile.objects.get( user__username = username  )
        return render(request , 'profile_user/basic.html' , {'profile' : profile})


    def post(self , request , username  ) :
        profile = Profile.objects.get(user__username = username  )
        return render(request , 'profile_user/basic.html' , {'profile' : profile})

class EditProfileView(LoginRequiredMixin , View ) :
    login_url = "login/"
    def get(self,request , username ) :
        if request.user.username != username :
            messages.error(request , 'شما نمیتوانید پروفایل شخص دیگری را تغیر بدهید ' , 'error')
            return redirect('home:home')

        else :
            form = ProfileEditForm()
            return render(request , 'profile_user/change_profile.html' , {'form':form} )


    def post(self , request  , username  ) :
        if request.user.username != username :
            messages.error(request , 'شما نمیتوانید پروفایل شخص دیگری را تغیر بدهید ' , 'error')
            return redirect('home:home')
        else :
            profile = Profile.objects.get( user = request.user    )
            form = ProfileEditForm( request.POST , instance = profile )
            if form.is_valid() :
                #profile.profile_pic = form.cleaned_data['profile_pic']
                profile.first_name = form.cleaned_data['first_name']
                profile.last_name = form.cleaned_data['last_name']
                form.save(commit = False  )
                profile.save()

                messages.success(request ,'با موفقیت تغیرات اعمال شد ' , 'success')
                return redirect('home:home')

            else :
                messages.error(request , 'در ثبت تغییرات مشکلی داریم ' , 'error' )
                return redirect('account:profile')
            return render(request , 'profile_user/change_profile.html' , {'form':form} )

