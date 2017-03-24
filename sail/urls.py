from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^gift/', include('gift.urls')),
    url(r'^admin/', admin.site.urls),

]
