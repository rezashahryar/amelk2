from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.contrib import messages

from models.models import Property, FavoriteProperty

from .forms import PropertyCommentForm, AddHomeVisitRequestForm, RequestAdviceForm
# Create your views here.


class EstateAlquilarView(generic.TemplateView):
    template_name = 'pages/EstateAlquilar.html'


class LearnMoreBuyPageView(generic.FormView):
    template_name = 'pages/learn_more_buy.html'
    form_class = RequestAdviceForm
    success_url = reverse_lazy('pages:home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'درخواست شما با موفقیت ثبت شد')
        return super().form_valid(form)


class LearnMoreSellPageView(generic.TemplateView):
    template_name = 'pages/EstateSell.html'


@require_POST
def add_home_visit_request_view(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    form = AddHomeVisitRequestForm(request.POST)
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.property = property_obj
        new_form.save()
    return redirect(request.headers['Referer'])


class HomePageView(generic.TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['properties'] = Property.objects.all()
        return context


class AboutPageView(generic.TemplateView):
    template_name = 'pages/about.html'


class ContactUsPageView(generic.TemplateView):
    template_name = 'pages/contact_us.html'


class FaqPageView(generic.TemplateView):
    template_name = 'pages/faq.html'


class OurServicesView(generic.TemplateView):
    template_name = 'pages/our_services.html'


class HouseListView(generic.ListView):
    queryset = Property.objects.filter(show_status=True).order_by('-created_at')
    template_name = 'pages/house_list.html'
    context_object_name = 'houses'
    paginate_by = 10


class HouseDetailView(generic.DetailView):
    template_name = 'pages/house_detail.html'
    context_object_name = 'house'

    def get_object(self):
        house_obj = get_object_or_404(
            Property,
            pk=self.kwargs['house_pk']
        )
        return house_obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['houses'] = Property.objects.filter(show_status=True)
        return context
    

@login_required
@require_POST
def property_comment_view(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    form = PropertyCommentForm(data=request.POST)
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.property = property_obj
        new_form.user = request.user
        new_form.save()
    return redirect(request.headers['Referer'])
    

@require_GET
def add_favorite_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    obj, created = FavoriteProperty.objects.get_or_create(
        property_id=property.pk,
        user_id=request.user.pk,
    )
    if created:
        messages.success(request, 'به لیست آگهی های مورد علاقه شما افزوده شد')
    else:
        messages.warning(request, 'این آگهی در لیست شما از قبل موجود است')
    return redirect(reverse('pages:house_detail', kwargs={'house_pk': property.pk}))


@require_GET
def delete_favorite_property(request, pk):
    property = get_object_or_404(FavoriteProperty, pk=pk)
    property.delete()
    return redirect('profiles:favorites')


class RequestAdviceView(generic.FormView):
    form_class = RequestAdviceForm
    template_name = 'pages/request_advice.html'
    success_url = reverse_lazy('pages:home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'درخواست شما با موفقیت ثبت شد')
        return super().form_valid(form)
