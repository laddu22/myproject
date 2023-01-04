from django import forms  


class resultForm(forms.Form):  
    enterid = forms.IntegerField(label="Savart-Id",required=True)  
   