from django.urls import path
from . import views


app_name = 'profiles'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('company-info/', views.CompanyInfoView.as_view(), name='company_info'),
    path('user-info/', views.UserInfoView.as_view(), name='user_info'),
    path('favorites/', views.FavoritesHouseListView.as_view(), name='favorites'),
    path('my-house/', views.HouseListView.as_view(), name='my_houses'),
    path('add/house/', views.AddHouseView.as_view(), name='add_house'),
    path('update/house/<int:pk>/', views.house_edit_view, name='house_update'),
    path('delete/house/<int:pk>/', views.house_delete_view, name='house_delete'),
    path('get-provinces/', views.get_provinces, name='get_provinces'),
    path('get-cities/', views.get_cities, name='get_cities'),
    path('manage/property/image/', views.ManagePropertyImageView.as_view(), name='manage_property_image'),
    path('delete/image/<int:pk>/', views.delete_property_image_view, name='delete_image'),
    path('messages/', views.ProfileMessagesView.as_view(), name='messages'),
]
