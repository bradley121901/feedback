from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(label="Enter product name:", max_length=10, required=True)
    company = forms.CharField(label="Enter product company:", max_length=10, required=True)
    description = forms.CharField(label="Enter product description", max_length=10, required=True)
    price = forms.CharField(label="Enter product price", max_length=10, required=True)

class SearchProduct(forms.Form):
    product = forms.CharField(label="Enter product name:", max_length=10, required=True)

class ReviewForm(forms.Form):
    comments = forms.CharField(label="Comments", max_length=1000, required=True)
    rating = forms.CharField(label="Rate (0, 10)", max_length=100, required=True)





