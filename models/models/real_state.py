from django.conf import settings
from django.db import models
from django.core.validators import validate_integer
from django.urls import reverse


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام کشور')

    class Meta:
        verbose_name = 'کشور'
        verbose_name_plural = 'کشورها'

    def __str__(self):
        return self.name
    

class Province(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='provinces', verbose_name='کشور')
    name = models.CharField(max_length=255, verbose_name='نام استان')

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'

    def __str__(self):
        return self.name
    

class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cities', verbose_name='استان')
    name = models.CharField(max_length=255, verbose_name='نام شهر')

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهرها'

    def __str__(self):
        return self.name
    

class RealStateCompany(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='company', verbose_name='کاربر')
    avatar = models.ImageField(upload_to='company-avatars/', null=True)
    full_name = models.CharField(max_length=255, verbose_name='نام و نام خانوادگی')
    description = models.TextField(verbose_name='توضیحات')
    name = models.CharField(max_length=255, verbose_name='نام بنگاه املاک')
    location = models.CharField(max_length=255, verbose_name='شهر')
    office_number = models.CharField(max_length=11, validators=[validate_integer], verbose_name='شماره تلفن محل کار')
    office_address = models.CharField(max_length=255, verbose_name='آدرس')
    email = models.EmailField(verbose_name='ایمیل')
    facebook_url = models.URLField(null=True, blank=True, verbose_name='آدرس فیسبوک')
    tweeter_url = models.URLField(null=True, blank=True, verbose_name='آدرس توییتر')
    linkedin_url = models.URLField(null=True, blank=True, verbose_name='آدرس لینکدین')

    class Meta:
        verbose_name = 'بنگاه املاک'
        verbose_name_plural = 'بنگاه های املاک'

    def __str__(self):
        return self.name


class Property(models.Model):
    TRANSACTION_TYPES = (
        ('sell', 'فروش'),
        ('rent', 'اجاره'),
    )
    class PROPERTY_TYPE(models.TextChoices):
        VILLA = 'v', 'ویلا'
        OFFICE = 'o', 'اداری'
        APARTMENT = 'a', 'آپارتمان'
        COMMERCIAL = 'c', 'تجاری'

    class HasParking(models.TextChoices):
        HAS = 'd', 'دارد'
        HAS_NOT = 'n', 'ندارد'
    
    house_type = models.CharField(max_length=1, choices=PROPERTY_TYPE.choices, null=True, verbose_name='نوع خانه')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties', null=True, blank=True)
    company = models.ForeignKey(RealStateCompany, on_delete=models.CASCADE, related_name='houses', null=True, verbose_name='بنگاه املاک')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    cover = models.ImageField(upload_to='properties-covers', null=True, verbose_name='عکس کاور آگهی')
    address = models.TextField(verbose_name='آدرس')
    post_code = models.CharField(max_length=10, verbose_name='کد پستی', validators=[validate_integer])
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='houses', verbose_name='کشور')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='houses', verbose_name='استان')
    video = models.FileField(upload_to='property-video/', null=True, blank=True, verbose_name='ویدئو')
    house_plan = models.FileField(upload_to='property-plan/', null=True, blank=True, verbose_name='نقشه ملک')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='houses', verbose_name='شهر')
    area = models.PositiveIntegerField(verbose_name='متراژ (متر مربع)')
    land_area = models.PositiveIntegerField(default=0, verbose_name='متراژ زمین', null=True, blank=True)
    house_id = models.CharField(max_length=255, verbose_name='شناسه ملک', null=True, blank=True)
    num_rooms = models.PositiveIntegerField(verbose_name='تعداد اتاقها')
    num_bedrooms = models.PositiveIntegerField(default=0, verbose_name='تعداد اتاق خواب ها', null=True, blank=True)
    num_bathrooms = models.PositiveIntegerField(default=0, verbose_name=' تعداد حمام ها', null=True, blank=True)
    parking = models.CharField(max_length=1, choices=HasParking.choices)
    elevator = models.CharField(max_length=1, choices=HasParking.choices)
    year_construction = models.CharField(max_length=4, validators=[validate_integer], verbose_name='سال ساخت')
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES,
        verbose_name='نوع معامله',
    )
    facilities = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    show_status = models.BooleanField(default=True, verbose_name='وضعیت نمایش')

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'آگهی'
        verbose_name_plural = 'آگهی ها'

    def __str__(self):
        return self.title
    
    @property
    def get_cover_url(self):
        return self.cover.url
    
    def get_absolute_url(self):
        return reverse("pages:house_detail", kwargs={"house_pk": self.pk})
    

class EstateRentRequest(models.Model):
    house_type = models.CharField(max_length=3, choices=Property.PROPERTY_TYPE.choices)
    location = models.CharField(max_length=255)
    min_area = models.IntegerField()
    num_rooms = models.IntegerField()
    max_budget = models.IntegerField()
    max_monthly_rent = models.IntegerField()
    job = models.CharField(max_length=255)
    num_family_members = models.IntegerField()
    full_name = models.CharField(max_length=255)
    mobile = models.IntegerField()
    description = models.CharField(max_length=255)
    

class HomeAccess(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='access', verbose_name='آگهی')
    name_access = models.CharField(max_length=255, verbose_name='نام دسترسی')
    distance = models.CharField(max_length=255, verbose_name='فاصله')

    class Meta:
        verbose_name = 'دسترسی خانه'
        verbose_name_plural = 'دسترسی های خانه ها'
    

class PropertyImage(models.Model):
    house = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images', verbose_name='آگهی')
    image = models.ImageField(upload_to='prooperty-more-images/', verbose_name='انتخاب عکس')

    datetime_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-datetime_created', )
        verbose_name = 'عکس آگهی'
        verbose_name_plural = 'عکس های آگهی ها'

    @property
    def get_image_url(self):
        return self.image.url
    

class Facility(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')

    class Meta:
        verbose_name = 'امکانات'
        verbose_name_plural = 'امکانات'

    def __str__(self):
        return self.name
    

class Amenities(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')
    facility = models.ManyToManyField(Facility, blank=True, verbose_name='امکانات')

    class Meta:
        verbose_name = 'دسته بندی امکانات'
        verbose_name_plural = 'دسته بندی های امکانات'
    

class SaleInfo(models.Model):
    property = models.OneToOneField(
        Property,
        on_delete=models.CASCADE,
        related_name='sale_info',
        verbose_name='آگهی'
    )
    price = models.BigIntegerField(verbose_name='قیمت فروش (تومان)')
    prepayment = models.BigIntegerField(verbose_name='پیشپرداخت (تومان)', null=True, blank=True, default=0)

    class Meta:
        verbose_name = 'آگهی فروش'
        verbose_name_plural = 'آگهی های فروش'


class RentInfo(models.Model):
    property = models.OneToOneField(
        Property,
        on_delete=models.CASCADE,
        related_name='rent_info',
        verbose_name='آگهی'
    )
    monthly_rent = models.BigIntegerField(verbose_name='اجاره ماهانه (تومان)')
    deposit = models.BigIntegerField(verbose_name='ودیعه (تومان)')

    class Meta:
        verbose_name = 'آگهی اجاره'
        verbose_name_plural = 'آگهی های اجاره'


class PropertyComment(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='comments', verbose_name='آگهی')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', verbose_name='کاربر')
    text = models.TextField(verbose_name='متن')
    datetime_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-datetime_created', )
        verbose_name = 'کامنت اگهی'
        verbose_name_plural = 'کامنت های اگهی'


class HomeVisitRequest(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='requests', verbose_name='آگهی')
    full_name = models.CharField(max_length=255, verbose_name='نام و نام خانوادگی')
    mobile = models.CharField(max_length=11, validators=[validate_integer], verbose_name='موبایل')
    email = models.EmailField(verbose_name='ایمیل')
    text = models.TextField(verbose_name='متن')
    datetime_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-datetime_created', )
        verbose_name = 'درخواست بازدید خانه'
        verbose_name_plural = 'درخواست های بازدید خانه'


class FavoriteProperty(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='favorites', verbose_name='آگهی')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites', verbose_name='کاربر')

    datetime_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'آگهی نشان شده'
        verbose_name_plural = 'آگهی های نشان شده'


class RequestAdvice(models.Model):
    full_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=11, validators=[validate_integer])
    price = models.IntegerField(null=True, blank=True)
    house_type = models.CharField(
        max_length=9,
        choices=[
            ('villa', 'ویلا'),
            ('office', 'اداری'),
            ('apartman', 'آپارتمان'),
            ('house', 'خانه'),
        ]
    )
    transaction_type = models.CharField(
        max_length=10,
        choices=[
            ('sale', 'برای فروش'),
            ('rent', 'برای اجاره')
        ]
    )
    location = models.CharField(max_length=555, null=True, blank=True)
    area = models.IntegerField(null=True)
    land_area = models.IntegerField(null=True)
    num_rooms = models.IntegerField(null=True)
    num_bedrooms = models.IntegerField(null=True)
    num_bathrooms = models.IntegerField(null=True)
    num_garage = models.IntegerField(null=True)
    land_garage = models.IntegerField(null=True)
    year_construction = models.IntegerField(null=True)
    full_name = models.CharField(max_length=255, null=True)
    mobile = models.IntegerField(null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-datetime_created', )
        verbose_name = 'درخواست مشاوره'
        verbose_name_plural = 'درخواست های مشاوره'
