from django import forms
from .models import Company, Section, Person
import logging

logger = logging.getLogger(__name__)

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('search_name', 'delete_flg', 'create_user', 'update_user')

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        exclude = ('search_name', 'delete_flg', 'create_user', 'update_user')

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ('search_name', 'delete_flg', 'create_user', 'update_user')
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['section'].queryset = \
            Section.objects.filter(company_id=self.instance.company_id)
