from django.conf import settings
from django.db import models
from django.urls import reverse


class PostCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی مقالات'
        verbose_name_plural = 'دسته بندی های مقالات'

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, related_name='posts', verbose_name='دسته بندی')
    title = models.CharField(max_length=255, verbose_name='عنوان مقاله')
    cover = models.ImageField(upload_to='post-covers/', verbose_name='عکس کاور مقاله')
    content = models.TextField(verbose_name='محتوای مقاله')
    active = models.BooleanField(default=True, verbose_name='وضعیت نمایش')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-datetime_created', )
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    
    @property
    def get_cover_url(self):
        return self.cover.url
    

class CommentPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments', verbose_name='مقاله')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_comments', verbose_name='کاربر')
    text = models.TextField(verbose_name='متن')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'کامنت مقالات'
        verbose_name_plural = 'کامنت های مقالات'
