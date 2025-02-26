from django.urls import path
from . import views


app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact-us/', views.ContactUsPageView.as_view(), name='contact_us'),
    path('faq/', views.FaqPageView.as_view(), name='faq'),
    path('our-services/', views.OurServicesView.as_view(), name='our_services'),
    path('houses/', views.HouseListView.as_view(), name='house_list'),
    path('house/<int:house_pk>/', views.HouseDetailView.as_view(), name='house_detail'),
    path('add/comment/<int:pk>/', views.property_comment_view, name='property_comment'),
    path('add/request/<int:pk>/', views.add_home_visit_request_view, name='add_request'),
    path('add/favorite/property/<int:pk>/', views.add_favorite_property, name='add_favorite_property'),
    path('delete/favorite/property/<int:pk>/', views.delete_favorite_property, name='delete_favorite_property'),
    path('request/advice/', views.RequestAdviceView.as_view(), name='request_advice'),
]
