"""ezreg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from ezreg.api.views import PriceViewset, PaymentProcessorViewset
from ezreg.views import RegistrationWizard
from ezreg.forms import RegistrationForm, PriceForm

router = routers.DefaultRouter()
router.register(r'prices', PriceViewset)
router.register(r'payment_processors', PaymentProcessorViewset)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ezreg.views.home',name='home'),
    url(r'^events/$', 'ezreg.views.events',name='events'),
    url(r'^events/create/$', 'ezreg.views.create_modify_event',name='create_event'),
    url(r'^events/(?P<id>[A-Z0-9]{10})/modify/$', 'ezreg.views.create_modify_event',name='modify_event'),
    url(r'^events/(?P<slug_or_id>[A-Za-z0-9_\-]{5,100})/$', 'ezreg.views.event',name='event'),
    url(r'^events/(?P<slug_or_id>[A-Za-z0-9_\-]{5,100})/register/$', RegistrationWizard.as_view(), name="register"),
    url(r'^events/(?P<slug_or_id>[A-Za-z0-9_\-]{5,100})/registrations/$', 'ezreg.views.registrations', name="registrations"),
    url(r'^registrations/(?P<id>[A-Za-z0-9_\-]{10})/$', 'ezreg.views.registration', name="registration"),
    url(r'^payment_processors/$', 'ezreg.views.payment_processors',name='payment_processors'),
    url(r'^payment_processors/create/$', 'ezreg.views.create_modify_payment_processor',name='create_payment_processor'),
    url(r'^payment_processors/(?P<id>\d+)/modify/$', 'ezreg.views.create_modify_payment_processor',name='modify_payment_processor'),
    url(r'^payment_processors/(?P<id>\d+)/configure/$', 'ezreg.views.configure_payment_processor',name='configure_payment_processor'),
    
    url(r'^api/', include(router.urls)),
    url(r'^api/event/(?P<event_id>[A-Za-z0-9_\-]{10})/payment_processors/$', 'ezreg.api.views.event_payment_processors', name="event_payment_processors"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
