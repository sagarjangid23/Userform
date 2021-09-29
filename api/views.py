from rest_framework.generics import ListCreateAPIView
from django.shortcuts import render
from api.models import UserDetail
from api.serializers import UserDetailSerializer
from api.forms import UserDetailForm
from send_mail_app.tasks import send_mail_func
from django.http import HttpResponseRedirect
from django.contrib import messages


# API related view
class UserForm(ListCreateAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer


# Django app related view
def showall(request):
    user = UserDetail.objects.all().order_by("-id")
    return render(request, 'api/show.html', {'user':user})

def user_create(request):
    if request.method == 'POST':
        fm = UserDetailForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data.get('name')
            dob = fm.cleaned_data.get('date_of_birth')
            email = fm.cleaned_data.get('email')
            phonenumber = fm.cleaned_data.get('phone_number')
            user = UserDetail(name=name, date_of_birth=dob, email=email, phone_number=phonenumber)
            user.save()
            send_mail_func(user)
            messages.success(request, 'Your data is submitted successfully')
            return HttpResponseRedirect('/')
    else:
        fm = UserDetailForm()
    return render(request, 'api/create.html', {'form':fm})
