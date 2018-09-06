from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sacco/', include('sacco.urls')),
    url(r'^driver/', include('driver.urls')),
    url(r'^vihecle/',include('vihecle.urls'))
]
