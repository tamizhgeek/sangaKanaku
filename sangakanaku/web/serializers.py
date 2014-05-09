from rest_framework import serializers
from sangakanaku.web.models import *
import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class HouseSerializer(serializers.ModelSerializer):
    expenses = serializers.HyperlinkedRelatedField('expenses', view_name='expense-list', lookup_field='id')
    my_share = serializers.SerializerMethodField("my_expense")

    def my_expense(self, obj):
        return obj.calculate_rent(VALID_MONTHS[datetime.datetime.now().month])[self.context['request'].user]

    class Meta:
        model = House
        fields = ('name', 'rent', 'id', 'expenses', 'my_share')

class ExpenseSerializer(serializers.ModelSerializer):
    bearer = UserSerializer(required = False)
    house = HouseSerializer(required = False)

    class Meta:
        model = Expense
        
    def get_validation_exclusions(self):
        # Need to exclude `bearer` since we'll add that later based off the request
        exclusions = super(ExpenseSerializer, self).get_validation_exclusions()
        return exclusions + ['bearer']
