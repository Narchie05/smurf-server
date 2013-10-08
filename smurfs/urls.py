from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers

from smurfs.models import Smurf

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


# ViewSets define the view behavior.
class SmurfViewSet(viewsets.ModelViewSet):
    model = Smurf

router = routers.DefaultRouter()
router.register(r'smurfs', SmurfViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    # Examples:
    # url(r'^$', 'smurfs.views.home', name='home'),
    # url(r'^smurfs/', include('smurfs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
