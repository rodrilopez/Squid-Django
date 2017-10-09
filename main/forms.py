from django import forms
from .models import Category, Permission

class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
