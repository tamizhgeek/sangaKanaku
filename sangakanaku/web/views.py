from django.shortcuts import render
from sangakanaku.web.models import House, Expense
from sangakanaku.web.serializers import *
from django.views.generic import TemplateView
from django.conf import settings
from rest_framework import viewsets, routers, generics, request
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

EXTRA_TEMPLATE_DIRS = ['', 'partials/']


from django.contrib.auth import logout as auth_logout
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect


def logout(request):
    auth_logout(request)
    return redirect("/")

class HouseViewSet(viewsets.ModelViewSet):
    Authentication_classes = (SessionAuthentication, )
    model = House
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return House.objects.filter(members__in=[self.request.user.id])
    

class ExpenseViewSet(viewsets.ModelViewSet):
    Authentication_classes = (SessionAuthentication, )
    model = Expense
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    
    def pre_save(self, obj):
        obj.bearer = self.request.user


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    Authentication_classes = (SessionAuthentication, )
    model = Expense
    serializer_class = ExpenseSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def pre_save(self, obj):
        obj.bearer = request.user
    


class HouseExpenseList(generics.ListAPIView):
    Authentication_classes = (SessionAuthentication, )
    model = Expense
    serializer_class = ExpenseSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    
    def get_queryset(self):
       queryset = super(HouseExpenseList, self).get_queryset()
       return queryset.filter(house__id=self.kwargs.get('house_id'))




class SimpleStaticView(TemplateView):
    def get_template_names(self):
        template_names = map(lambda x: x + self.kwargs.get('template_name') + ".html", EXTRA_TEMPLATE_DIRS)
        return template_names
    
    def get(self, request, *args, **kwargs):
        return super(SimpleStaticView, self).get(request, *args, **kwargs)

class HomePageView(TemplateView):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        return super(HomePageView, self).get(request, *args, **kwargs)

                        
