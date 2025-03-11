from django import forms
from models.models import PropertyComment, HomeVisitRequest, RequestAdvice, Property, EstateRentRequest


class EstateRentForm(forms.ModelForm):
    class Meta:
        model = EstateRentRequest
        fields = [
            'house_type', 'location', 'min_area', 'num_rooms', 'max_budget', 'max_monthly_rent',
            'job', 'num_family_members', 'full_name', 'mobile', 'description',
        ]


class AddHomeVisitRequestForm(forms.ModelForm):
    class Meta:
        model = HomeVisitRequest
        fields = ['full_name', 'mobile', 'email', 'text']


class PropertyCommentForm(forms.ModelForm):
    class Meta:
        model = PropertyComment
        fields = ['text']


class RequestAdviceForm(forms.Form):
    house_type = forms.ChoiceField(
        choices=(
            ('villa', 'ویلا'),
            ('office', 'اداری'),
            ('apartman', 'آپارتمان'),
            ('house', 'خانه'),
        ),
        required=False
    )
    transaction_type = forms.ChoiceField(
        choices=(
            ('sale', 'برای فروش'),
            ('rent', 'برای اجاره')
        ),
        required=False
    )
    area = forms.IntegerField(required=False)
    land_area = forms.IntegerField(required=False)
    num_rooms = forms.IntegerField(required=False)
    num_bedrooms = forms.IntegerField(required=False)
    num_bathrooms = forms.IntegerField(required=False)
    num_garage = forms.IntegerField(required=False)
    land_garage = forms.IntegerField(required=False)
    year_construction = forms.IntegerField(required=False)
    full_name = forms.CharField(required=False)
    mobile = forms.IntegerField(required=False)
    price = forms.IntegerField(required=False)
    location = forms.CharField(required=False)

    def save(self):
        data = self.cleaned_data
        obj = RequestAdvice.objects.create(
            house_type=data['house_type'],
            transaction_type=data['transaction_type'],
            area=data['area'],
            land_area=data['land_area'],
            num_rooms=data['num_rooms'],
            num_bedrooms=data['num_bedrooms'],
            num_bathrooms=data['num_bathrooms'],
            num_garage=data['num_garage'],
            land_garage=data['land_garage'],
            year_construction=data['year_construction'],
            full_name=data['full_name'],
            mobile=data['mobile'],
            price=data['price'],
            location=data['location'],
        )
        return obj
