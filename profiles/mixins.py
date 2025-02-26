from django.core.exceptions import PermissionDenied

class AccessControlMixin:
    def dispatch(self, request, *args, **kwargs):
        # بررسی سطح دسترسی
        if not self.has_permission(request):
            raise PermissionDenied  # یا می‌توانید به یک صفحه دیگر ریدایرکت کنید

        return super().dispatch(request, *args, **kwargs)

    def has_permission(self, request):
        # این متد را اورراید کنید تا منطق بررسی دسترسی را پیاده‌سازی کنید
        # به عنوان مثال، بررسی کنید که کاربر وارد سیستم باشد یا نقش خاصی داشته باشد
        return request.user.is_authenticated