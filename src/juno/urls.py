from django.conf.urls import url, include
from django.contrib import admin

#from shortener.views import KirrCBView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^kirr/', include('shortener.urls')),
]
