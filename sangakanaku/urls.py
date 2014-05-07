from django.conf.urls import patterns, include, url
from django.contrib import admin
from sangakanaku.web.models import House, Expense
from django.views.generic import TemplateView
from django.conf import settings
from sangakanaku.web.views import *
from rest_framework import viewsets, routers, generics

admin.autodiscover()


router = routers.DefaultRouter()
router.register(r'house', HouseViewSet)
router.register(r'expense', ExpenseViewSet)

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include(router.urls)),
                       url(r'^api/house/(?P<house_id>\d+)/expenses$', HouseExpenseList.as_view(), name='house-expense-list'),
                       url(r'^api/expense/(?P<pk>\d+)$', ExpenseDetail.as_view(), name="expense-detail"),
                       url(r'', include('social.apps.django_app.urls', namespace='social')),
                       url(r'^logout/', logout, name='logout'), 
                       url(r'^', HomePageView.as_view(), name="index"),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root', settings.STATICFILES_DIRS}
  ),
)
