from django.contrib import admin
from models.models import EstateRentRequest, RequestAdvice, HomeAccess, Amenities, PropertyImage, FavoriteProperty, HomeVisitRequest, PropertyComment, Property, Province, City, Country, Facility, SaleInfo, RentInfo, RealStateCompany


@admin.register(RequestAdvice)
class RequestAdviceAdmin(admin.ModelAdmin):
    ...


@admin.register(HomeAccess)
class HomeAccessAdmin(admin.ModelAdmin):
    ...


@admin.register(Amenities)
class AmenitiesAdmin(admin.ModelAdmin):
    ...


@admin.register(PropertyImage)
class PropertyImage(admin.ModelAdmin):
    ...


@admin.register(FavoriteProperty)
class FavoritePropertyAdmin(admin.ModelAdmin):
    ...


@admin.register(HomeVisitRequest)
class HomeVisitRequestAdmin(admin.ModelAdmin):
    ...


@admin.register(PropertyComment)
class PropertyCommentAdmin(admin.ModelAdmin):
    ...


@admin.register(RealStateCompany)
class RealStateCompanyAdmin(admin.ModelAdmin):
    ...


@admin.register(EstateRentRequest)
class EstateRentRequestAdmin(admin.ModelAdmin):
    ...


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'house_type']


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    ...


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    ...


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    ...


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    ...


@admin.register(SaleInfo)
class SaleInfoAdmin(admin.ModelAdmin):
    ...


@admin.register(RentInfo)
class RentInfoAdmin(admin.ModelAdmin):
    ...
