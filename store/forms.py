from django import forms


class AddToCartForm(forms.Form):
    """
    A class used to create  add to cart form
    ...
    Attributes
    ----------
    quantity : IntegerField
        an IntegerField to hold the product quantity on form
    """
    quantity = forms.IntegerField(min_value=1, max_value=10, widget=forms.NumberInput(
        attrs={'class': 'quantity-input'}), error_messages={'required': 'please enter the quantity'})
