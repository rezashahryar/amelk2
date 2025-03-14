# Generated by Django 5.1.6 on 2025-02-25 13:55

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0011_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenities',
            name='facility',
            field=models.ManyToManyField(blank=True, to='models.facility', verbose_name='امکانات'),
        ),
        migrations.AlterField(
            model_name='amenities',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام شهر'),
        ),
        migrations.AlterField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='models.province', verbose_name='استان'),
        ),
        migrations.AlterField(
            model_name='commentpost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='models.post', verbose_name='مقاله'),
        ),
        migrations.AlterField(
            model_name='commentpost',
            name='text',
            field=models.TextField(verbose_name='متن'),
        ),
        migrations.AlterField(
            model_name='commentpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام کشور'),
        ),
        migrations.AlterField(
            model_name='facility',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='favoriteproperty',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='models.property', verbose_name='آگهی'),
        ),
        migrations.AlterField(
            model_name='favoriteproperty',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='homeaccess',
            name='distance',
            field=models.CharField(max_length=255, verbose_name='فاصله'),
        ),
        migrations.AlterField(
            model_name='homeaccess',
            name='name_access',
            field=models.CharField(max_length=255, verbose_name='نام دسترسی'),
        ),
        migrations.AlterField(
            model_name='homeaccess',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access', to='models.property', verbose_name='آگهی'),
        ),
        migrations.AlterField(
            model_name='homevisitrequest',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='homevisitrequest',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='نام و نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='homevisitrequest',
            name='mobile',
            field=models.CharField(max_length=11, validators=[django.core.validators.validate_integer], verbose_name='موبایل'),
        ),
        migrations.AlterField(
            model_name='homevisitrequest',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='models.property', verbose_name='آگهی'),
        ),
        migrations.AlterField(
            model_name='homevisitrequest',
            name='text',
            field=models.TextField(verbose_name='متن'),
        ),
        migrations.AlterField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True, verbose_name='وضعیت نمایش'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='models.postcategory', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='محتوای مقاله'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(upload_to='post-covers/', verbose_name='عکس کاور مقاله'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='عنوان مقاله'),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام دسته بندی'),
        ),
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='models.city', verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='property',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='models.realstatecompany', verbose_name='بنگاه املاک'),
        ),
        migrations.AlterField(
            model_name='property',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='models.country', verbose_name='کشور'),
        ),
        migrations.AlterField(
            model_name='property',
            name='cover',
            field=models.ImageField(null=True, upload_to='properties-covers', verbose_name='عکس کاور آگهی'),
        ),
        migrations.AlterField(
            model_name='property',
            name='facilities',
            field=models.ManyToManyField(blank=True, to='models.facility', verbose_name='دسترسی ها'),
        ),
        migrations.AlterField(
            model_name='property',
            name='garage_area',
            field=models.PositiveIntegerField(default=0, verbose_name='متراژ پارکینگ'),
        ),
        migrations.AlterField(
            model_name='property',
            name='house_id',
            field=models.CharField(max_length=255, verbose_name='شناسه ملک'),
        ),
        migrations.AlterField(
            model_name='property',
            name='house_plan',
            field=models.FileField(blank=True, null=True, upload_to='property-plan/', verbose_name='نقشه ملک'),
        ),
        migrations.AlterField(
            model_name='property',
            name='house_type',
            field=models.CharField(choices=[('v', 'villa'), ('o', 'office'), ('a', 'apartment'), ('h', 'house')], max_length=1, null=True, verbose_name='نوع خانه'),
        ),
        migrations.AlterField(
            model_name='property',
            name='land_area',
            field=models.PositiveIntegerField(default=0, verbose_name='متراژ زمین'),
        ),
        migrations.AlterField(
            model_name='property',
            name='num_bathrooms',
            field=models.PositiveIntegerField(default=0, verbose_name=' تعداد حمام ها'),
        ),
        migrations.AlterField(
            model_name='property',
            name='num_bedrooms',
            field=models.PositiveIntegerField(default=0, verbose_name='تعداد اتاق خواب ها'),
        ),
        migrations.AlterField(
            model_name='property',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='models.province', verbose_name='استان'),
        ),
        migrations.AlterField(
            model_name='property',
            name='show_status',
            field=models.BooleanField(default=True, verbose_name='وضعیت نمایش'),
        ),
        migrations.AlterField(
            model_name='property',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='property-video/', verbose_name='ویدئو'),
        ),
        migrations.AlterField(
            model_name='property',
            name='year_construction',
            field=models.CharField(max_length=4, validators=[django.core.validators.validate_integer], verbose_name='سال ساخت'),
        ),
        migrations.AlterField(
            model_name='propertycomment',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='models.property', verbose_name='آگهی'),
        ),
        migrations.AlterField(
            model_name='propertycomment',
            name='text',
            field=models.TextField(verbose_name='متن'),
        ),
        migrations.AlterField(
            model_name='propertycomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='models.property', verbose_name='آگهی'),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=models.ImageField(upload_to='prooperty-more-images/', verbose_name='انتخاب عکس'),
        ),
        migrations.AlterField(
            model_name='province',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provinces', to='models.country', verbose_name='کشور'),
        ),
        migrations.AlterField(
            model_name='province',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام استان'),
        ),
        migrations.AlterField(
            model_name='realstatecompany',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='realstatecompany',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='realstatecompany',
            name='facebook_url',
            field=models.URLField(blank=True, null=True, verbose_name='آدرس فیسبوک'),
        ),
        migrations.AlterField(
            model_name='realstatecompany',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='نام و نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='realstatecompany',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True, verbose_name='آدرس لینکدین'),
        ),
        migrations.AlterField(
            model_name='realstatecompany',
            name='location',
            field=models.CharField(max_length=255, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='realstatecompany',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام بنگاه املاک'),
        ),
        migrations.AlterField(
            model_name='realstatecompany',
            name='office_address',
            field=models.CharField(max_length=255, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='realstatecompany',
            name='office_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.validate_integer], verbose_name='شماره تلفن محل کار'),
        ),
        migrations.AlterField(
            model_name='realstatecompany',
            name='tweeter_url',
            field=models.URLField(blank=True, null=True, verbose_name='آدرس توییتر'),
        ),
        migrations.AlterField(
            model_name='realstatecompany',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='rentinfo',
            name='property',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rent_info', to='models.property', verbose_name='آگهی'),
        ),
        migrations.AlterField(
            model_name='saleinfo',
            name='property',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sale_info', to='models.property', verbose_name='آگهی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False, verbose_name='مشاور املاک هست'),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=11, validators=[django.core.validators.validate_integer], verbose_name='موبایل'),
        ),
    ]
