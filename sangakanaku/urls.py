from django.conf.urls import patterns, include, url
from django.contrib import admin
from sangakanaku.web.models import House, Expense
from django.views.generic import TemplateView
from django.conf import settings
from rest_framework import viewsets, routers, generics

admin.autodiscover()

EXTRA_TEMPLATE_DIRS = ['', 'partials/']

class HouseViewSet(viewsets.ModelViewSet):
    model = House

class ExpenseViewSet(viewsets.ModelViewSet):
    model = Expense

class HouseExpenseList(generics.ListAPIView):
    model = Expense
    
    def get_queryset(self):
       queryset = super(HouseExpenseList, self).get_queryset()
       return queryset.filter(house__id=self.kwargs.get('house_id'))
        

router = routers.DefaultRouter()
router.register(r'house', HouseViewSet)
router.register(r'expense', ExpenseViewSet)



class SimpleStaticView(TemplateView):
    def get_template_names(self):
        template_names = map(lambda x: x + self.kwargs.get('template_name') + ".html", EXTRA_TEMPLATE_DIRS)
        return template_names
    
    def get(self, request, *args, **kwargs):
        # from django.contrib.auth import authenticate, login
        # if request.user.is_anonymous():
        #     # Auto-login the User for Demonstration Purposes
        #     user = authenticate()
        #     login(request, user)
        return super(SimpleStaticView, self).get(request, *args, **kwargs)

class HomePageView(TemplateView):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        return super(HomePageView, self).get(request, *args, **kwargs)


urlpatterns = patterns('',
                       
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^(?P<template_name>\w+)$', SimpleStaticView.as_view()),
                       url(r'^partials/(?P<template_name>\w+)$', SimpleStaticView.as_view()),
                       url(r'^api/', include(router.urls)),
                       url(r'^api/house/(?P<house_id>\d+)/expenses$', HouseExpenseList.as_view(), name='house-expense-list'),
                       url(r'^', HomePageView.as_view(), name="index"),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root', settings.STATICFILES_DIRS}
  ),
)
