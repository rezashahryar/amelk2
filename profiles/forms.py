from django import forms
from django.contrib.auth import get_user_model

from models.models import PropertyImage, RentInfo, Country, Province, City, SaleInfo, RealStateCompany, Property


class AddHouseBaseForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField()
    post_code = forms.IntegerField()
    cover = forms.ImageField()
    house_type = forms.ChoiceField(
        choices=(
            ('v', 'ویلا'),
            ('o', 'اداری'),
            ('a', 'آپارتمان'),
            ('h', 'خانه')
        )
    )
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        widget=forms.Select(attrs={'class': 'nice-select', 'id': 'country'})
    )
    province = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        widget=forms.Select(attrs={'class': 'nice-select', 'id': 'province'})
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': 'nice-select', 'id': 'city'})
    )
    transaction_type = forms.ChoiceField(
        choices=(
            ('sale', 'برای فروش'),
            ('rent', 'برای اجاره')
        ),
        widget=forms.Select(attrs={'class': 'nice-select'})
    )
    address = forms.CharField()
    area = forms.IntegerField(initial=0)
    land_area = forms.IntegerField(initial=0)
    house_id = forms.IntegerField(initial=0)
    num_rooms = forms.IntegerField(initial=0)
    num_bedrooms = forms.IntegerField(initial=0)
    num_bathrooms = forms.IntegerField(initial=0)
    num_garage = forms.IntegerField(initial=0)
    garage_area = forms.IntegerField(initial=0)
    year_construction = forms.IntegerField()
    video = forms.FileField(required=False)
    house_plan = forms.FileField(required=False)

    class Meta:
        ...


class AddRentPropertyForm(AddHouseBaseForm):
    class Meta:
        model = RentInfo
        fields = [
            'monthly_rent', 'deposit'
        ]


class AddSalePropertyForm(AddHouseBaseForm):
    class Meta:
        model = SaleInfo
        fields = ['prepayment', 'price']


class RealStateCompanyForm(forms.ModelForm):
    class Meta:
        model = RealStateCompany
        fields = [
            'full_name', 'description', 'avatar', 'name', 'location', 'office_number', 'office_address',
            'email', 'facebook_url', 'tweeter_url', 'linkedin_url'
        ]


class EditUserInfoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['mobile', 'email']


class EditPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'title', 'description', 'address', 'post_code', 'cover', 'country', 'province', 'city', 'area',
            'land_area', 'house_id', 'num_rooms', 'num_bedrooms', 'num_bathrooms', 'num_garage',
            'garage_area', 'year_construction', 'transaction_type'
        ]
        widgets = {
            'address': forms.TextInput,
            'transaction_type': forms.Select(attrs={'class': 'nice-select'}),
            'country': forms.Select(attrs={'class': 'nice-select', 'id': 'country'}),
            'province': forms.Select(attrs={'class': 'nice-select', 'id': 'province'}),
            'city': forms.Select(attrs={'class': 'nice-select', 'id': 'city'}),
        }


class EditSalePropertyForm(forms.ModelForm):
    class Meta:
        model = SaleInfo
        fields = ['prepayment', 'price']


class EditRentPropertyForm(forms.ModelForm):
    class Meta:
        model = RentInfo
        fields = ['deposit', 'monthly_rent']


class AddPropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['house', 'image']
        widgets = {
            'house': forms.Select
        }
