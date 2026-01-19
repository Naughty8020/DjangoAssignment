from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer  # これを必ず書く！
        # HTMLで表示したい「モデル内の名前」を正確に並べる
        fields = [
            'customer_code', 
            'customer_name', 
            'customer_telno', 
            'customer_postalcode', 
            'customer_address'
        ]
