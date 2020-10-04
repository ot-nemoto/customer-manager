from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ("search_name", "delete_flg", "create_user", "update_user")
