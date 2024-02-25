from django.shortcuts import render , redirect
from django.views.generic import TemplateView
from django.views import View
from account.models import Profile

# Create your views here.



class HomeView(View):


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:login')
        return super().dispatch(request , *args , **kwargs )


    def setup(self, request, *args, **kwargs):
        self.user = Profile.objects.get(user=request.user)
        return super().setup( request, *args, **kwargs)

    def get(self, request):



        return render(request , 'home/home1.html' , {'message' : 'Hello World!' , 'user' : self.user })


    def post(self, request):
        return render(request , 'home/home1.html' , {'message' : 'Hello World!' , 'user' : self.user})