from django import forms
from api.models import UserDetail
from datetime import date

class DateInput(forms.DateInput):
    input_type = 'date'


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['name','date_of_birth','email','phone_number']
        widgets = {
            'date_of_birth': DateInput(),
            }
    
    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        today = date.today()
        age = today.year - dob.year
        if today.month < dob.month or today.month == dob.month and today.day < dob.day:
            age -= 1
        if age < 18:
            raise forms.ValidationError('Age cannot be less than 18 years')
        return dob