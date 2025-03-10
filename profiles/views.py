from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.views.decorators.http import require_GET

from models.models import (
    HomeVisitRequest, Amenities, Property, Province, City, Country, RealStateCompany,
    FavoriteProperty, PropertyImage
)
from profiles.mixins import AccessControlMixin

from .forms import (
    AddPropertyImageForm, EditRentPropertyForm, AddRentPropertyForm, AddSalePropertyForm,
    EditPropertyForm, RealStateCompanyForm, EditUserInfoForm, EditSalePropertyForm
)
# Create your views here.

class DashboardView(LoginRequiredMixin, AccessControlMixin, generic.TemplateView):
    template_name = 'profiles/dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('models.is_agent'):
            return redirect('profiles:user_info')
        return super().dispatch(request, *args, **kwargs)
    
    def has_permission(self, request):
        return bool(request.user.has_perm('models.is_agent'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['houses'] = Property.objects.filter(company__user_id=self.request.user.pk).order_by('-created_at')
        context['visit_requests'] = HomeVisitRequest.objects.filter(property__company__user=self.request.user)
        return context


class UserInfoView(LoginRequiredMixin, generic.FormView):
    form_class = EditUserInfoForm
    template_name = 'profiles/user_info.html'
    success_url = reverse_lazy('profiles:user_info')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs


class CompanyInfoView(LoginRequiredMixin, AccessControlMixin, generic.FormView):
    form_class = RealStateCompanyForm
    template_name = 'profiles/company_info.html'
    success_url = reverse_lazy('profiles:company_info')

    def has_permission(self, request):
        if self.get_form_kwargs().get('instance'):
            return bool(request.user.has_perm('models.is_agent'))
        return super().has_permission(request)

    def form_valid(self, form):
        new_form = form.save(commit=False)
        new_form.user = self.request.user
        if self.request.POST.get('is_updated'):
            permission = Permission.objects.get(name='has a real state company')
            self.request.user.user_permissions.add(permission.pk)
            self.request.user.is_agent = True
            self.request.user.save()
        new_form.save()
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        try:
            company = RealStateCompany.objects.get(user_id=self.request.user.pk)
            kwargs['instance'] = company
        except RealStateCompany.DoesNotExist:
            ...
        return kwargs


class FavoritesHouseListView(LoginRequiredMixin, generic.ListView):
    template_name = 'profiles/favorites.html'
    context_object_name = 'properties'
    paginate_by = 10

    def get_queryset(self):
        queryset = FavoriteProperty.objects.filter(user_id=self.request.user.pk)
        return queryset


class HouseListView(LoginRequiredMixin, AccessControlMixin, generic.ListView):
    template_name = 'profiles/my_house_list.html'
    context_object_name = 'houses'
    paginate_by = 10

    def has_permission(self, request):
        return bool(request.user.has_perm('models.is_agent'))

    def get_queryset(self):
        queryset = Property.objects.filter(company__user_id=self.request.user.pk).order_by('-created_at')
        return queryset
    

def house_edit_view(request, pk):
    house = get_object_or_404(Property, pk=pk)
    context = {
        'countries': Country.objects.all()
    }
    try:
        if house.rent_info:
            context['edit_rent_info_form'] = EditRentPropertyForm(instance=house.rent_info)
    except:
        if house.sale_info:
            context['edit_sale_info_form'] = EditSalePropertyForm(instance=house.sale_info)
    context['property_form'] = EditPropertyForm(instance=house)

    if request.method == 'POST':
        property_form = EditPropertyForm(data=request.POST, files=request.FILES, instance=house)
        try:
            if house.rent_info:
                rent_info_form = EditRentPropertyForm(data=request.POST, instance=house.rent_info)
                if property_form.is_valid() and rent_info_form.is_valid():
                    property_form.save()
                    rent_info_form.save()
        except:
            if house.sale_info:
                edit_sale_info_form = EditSalePropertyForm(data=request.POST, instance=house.sale_info)
                if property_form.is_valid() and edit_sale_info_form.is_valid():
                    property_form.save()
                    edit_sale_info_form.save()
        return redirect('profiles:dashboard')
    return render(request, 'profiles/edit_house.html', context)


@login_required
@permission_required(perm='models.is_agent')
def house_delete_view(request, pk):
    Property.objects.get(pk=pk).delete()
    return redirect('profiles:dashboard')


class AddHouseView(LoginRequiredMixin, AccessControlMixin, generic.FormView):
    template_name = 'profiles/add_house.html'
    # form_class = AddRentPropertyForm
    success_url = reverse_lazy('profiles:my_houses')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        context['amenities'] = Amenities.objects.all()
        return context

    def get_form_class(self):
        if self.request.method == 'POST' and self.request.POST['price'] != '':
            return AddSalePropertyForm
        return AddRentPropertyForm

    def form_valid(self, form):
        data = form.cleaned_data
        property = Property.objects.create(
            company_id=self.request.user.company.pk,
            title=data['title'],
            description=data['description'],
            address=data['address'],
            cover=self.request.FILES['cover'],
            house_type=data['house_type'],
            post_code=data['post_code'],
            country=data['country'],
            province=data['province'],
            city=data['city'],
            area=data['area'],
            land_area=data['land_area'],
            house_id=data['house_id'],
            num_rooms=data['num_rooms'],
            num_bedrooms=data['num_bedrooms'],
            num_bathrooms=data['num_bathrooms'],
            num_garage=data['num_garage'],
            garage_area=data['garage_area'],
            year_construction=data['year_construction'],
            transaction_type=data['transaction_type'],
            video=data['video'],
            house_plan=data['house_plan'],
        )
        querydict = dict(self.request.POST)
        property.facilities.set(querydict['fac'])
        property.save()
        new_form = form.save(commit=False)
        new_form.property_id = property.id
        new_form.save()
        messages.success(self.request, 'آگهی شما با موفقیت ثبت شد')
        return super().form_valid(form)
    

@require_GET
def get_provinces(request):
    country_id = request.GET.get('country_id')
    if not country_id:
        return JsonResponse({"erorr": "country_id url param in not valid"}, status=400)
    provinces = Province.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse(list(provinces), safe=False, status=200)


@require_GET
def get_cities(request):
    province_id = request.GET.get('province_id')
    if not province_id:
        return JsonResponse({"erorr": "province_id url param in not valid"}, status=400)
    cities = City.objects.filter(province_id=province_id).values('id', 'name')
    return JsonResponse(list(cities), safe=False, status=200)


class ManagePropertyImageView(LoginRequiredMixin, AccessControlMixin, generic.FormView):
    form_class = AddPropertyImageForm
    template_name = 'profiles/manage_property_image.html'
    success_url = reverse_lazy('profiles:manage_property_image')

    def has_permission(self, request):
        return bool(request.user.has_perm('models.is_agent'))

    def form_valid(self, form):
        form.save()
        # # new_form.house_id = self.request.POST.get('house_pk')
        # new_form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = PropertyImage.objects.all()
        return context


@login_required
@permission_required('models.is_agent')
def delete_property_image_view(request, pk):
    property_image_obj = get_object_or_404(PropertyImage, pk=pk)
    property_image_obj.delete()
    return redirect('profiles:manage_property_image')


class ProfileMessagesView(LoginRequiredMixin, AccessControlMixin, generic.ListView):
    template_name = 'profiles/messages.html'
    context_object_name = 'visit_requests'

    def has_permission(self, request):
        return bool(request.user.has_perm('models.is_agent'))

    def get_queryset(self):
        queryset = HomeVisitRequest.objects.filter(property__company__user_id=self.request.user.pk)
        return queryset
