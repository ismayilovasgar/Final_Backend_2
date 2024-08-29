from django import forms


class SearchForm(forms.Form):
    search1 = forms.CharField(required=False, label="Search 1")
