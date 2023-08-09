from django import forms
from .models import CustomUser
from django.core.validators import RegexValidator

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=20, validators=[RegexValidator(regex=r'^\d+$', message='전화번호에는 숫자만 입력할 수 있습니다.')])
    password = None
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('이미 사용 중인 전화번호입니다.')
        return phone_number