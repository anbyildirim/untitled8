
from django.conf.urls import include, url
from django.contrib import admin
from Soft_3.views import index
urlpatterns = (
    #url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^asd/', index)
    #url(r'^form/', include('Soft_3.urls'))
)