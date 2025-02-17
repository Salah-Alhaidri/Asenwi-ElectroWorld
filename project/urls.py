
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


from django.views.generic import TemplateView
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('shop/', include('order.urls')),
    path('accounts/', include('accounts.urls')),





]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
