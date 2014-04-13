from sangakanaku.web.models import *
from django import forms
from crispy_forms.helper import FormHelper
from djangular.forms import NgFormValidationMixin, NgModelFormMixin, AddPlaceholderFormMixin

class ExpenseForm(NgModelFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        setup_bootstrap_helpers(self)

    class Meta:
        model = Expense
        fields = ('bearer', 'description', 'amount', 'house' , 'date')

def setup_bootstrap_helpers(object):
    object.helper = FormHelper()
    object.helper.form_class = 'form-horizontal'
    object.helper.label_class = 'col-lg-3'
    object.helper.field_class = 'col-lg-8'
