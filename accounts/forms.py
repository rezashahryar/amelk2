from django import forms
from django.core.validators import validate_integer
from django.db.models import Q
from models.models.user import User


class LoginForm(forms.Form):
    mobile = forms.CharField(max_length=11, validators=[validate_integer])
    password = forms.CharField()

    def clean_mobile(self):
        global user
        username = self.cleaned_data['mobile']
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
        except User.DoesNotExist:
            raise forms.ValidationError("کاربری با این مشخصات در سیستم وجود ندارد")
        return username
    
    def clean_password(self):
        username = self.cleaned_data.get('mobile')
        password = self.cleaned_data['password']
        if not username:
            return password
        if user.check_password(password):
            return password
        else:
            raise forms.ValidationError('پسورد وارد شده صحیح نیست')
        

class RegisterForm(forms.ModelForm):
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ['full_name', 'mobile', 'email', 'password']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        try:
            user = User.objects.get(Q(username=mobile) | Q(mobile=mobile))
            if user:
                raise forms.ValidationError('کاربری از قبل با این مشخصات ثبت نام کرده است')
        except User.DoesNotExist:
            ...
        return mobile

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            raise forms.ValidationError('پسورد ها باید با یکدیگر تطابق داشته باشند')
        return password2

    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data['mobile']
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
