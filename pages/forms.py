from django import forms
from models.models import PropertyComment, HomeVisitRequest, RequestAdvice


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
        )
    )
    transaction_type = forms.ChoiceField(
        choices=(
            ('sale', 'برای فروش'),
            ('rent', 'برای اجاره')
        )
    )
    area = forms.IntegerField()
    land_area = forms.IntegerField()
    num_rooms = forms.IntegerField()
    num_bedrooms = forms.IntegerField()
    num_bathrooms = forms.IntegerField()
    num_garage = forms.IntegerField()
    land_garage = forms.IntegerField()
    year_construction = forms.IntegerField()
    full_name = forms.CharField()
    mobile = forms.IntegerField()

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
            mobile=data['mobile']
        )
        return obj
