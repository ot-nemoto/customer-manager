from django import forms
from .models import Company, Section, Person

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
