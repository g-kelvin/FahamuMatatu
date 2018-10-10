from django.conf.urls import url,  include
from django.contrib import admin
from sacco.views import err_403

urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^sacco/', include('sacco.urls')),
]
handler403 = err_403