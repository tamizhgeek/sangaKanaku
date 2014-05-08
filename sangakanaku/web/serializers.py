from rest_framework import serializers
from sangakanaku.web.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class HouseSerializer(serializers.ModelSerializer):
    expenses = serializers.HyperlinkedRelatedField('expenses', view_name='expense-list', lookup_field='id')

    class Meta:
        model = House
        fields = ('name', 'rent', 'id', 'expenses')

class ExpenseSerializer(serializers.ModelSerializer):
    bearer = UserSerializer(required = False)
    class Meta:
        model = Expense
        
    def get_validation_exclusions(self):
        # Need to exclude `bearer` since we'll add that later based off the request
        exclusions = super(ExpenseSerializer, self).get_validation_exclusions()
        return exclusions + ['bearer']
