from django.shortcuts import render,redirect
from django.contrib.auth.forms import  UserCreationForm
from .models import UserProfile
from django.contrib.auth import  login
# from .form import PhoneForm

# Create your views here.

def SignUp(request):
    # form = UserCreationForm()
    # No = PhoneForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        # phone = PhoneForm(request.post)
        # form = SignUpForm(request.POST)

        if form.is_valid() and phone.is_valid():
             user = form.save()
             number = request.POST.get('phone')
             phone = UserProfile.objects.create(user=user,)
             phone.save()
             login(request,user)
             return redirect('/')

            # phone = request.POST.get('phone','jobseeker')
        #     if account_type == 'employer':
        #         userprofile = UserProfile.objects.create(user=user,is_employer= True)
        #         # user.userprofile.is_employer =True
        #         userprofile.save()
        #     else:
        #         userprofile = UserProfile.objects.create(user=user,is_employer= False)
        #         # user.userprofile.is_employer =True
        #         userprofile.save()

        #     login(request,user)
        #     return redirect('dashboard')
        # else:
        #     print("SignUp Form Error")
    else:
        form = UserCreationForm()
    return render(request,'customerApp/signup.html',{'form':form,})

