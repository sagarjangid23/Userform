from api.models import UserDetail
from rest_framework import serializers, status
from datetime import date
from send_mail_app.tasks import send_mail_func
from django.http import HttpResponseRedirect


class UserDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserDetail
        fields = ['name','date_of_birth','email','phone_number']
        

    def validate_date_of_birth(self, dob):
        today = date.today()
        age = today.year - dob.year
        if today.month < dob.month or today.month == dob.month and today.day < dob.day:
            age -= 1
        if age < 18:
            raise serializers.ValidationError('Age cannot be less than 18 years')
        return dob

    def create(self, validate_data):
        instance = super(UserDetailSerializer, self).create(validate_data)
        send_mail_func(instance)
        return instance
