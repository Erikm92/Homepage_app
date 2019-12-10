from django import forms

class todoform(forms.Form):
    text = forms.CharField(max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'formpadding form-control', 'placeholder': 'Enter todo','aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}
        )
    )

class saveurlform(forms.Form):
    
    url_name = forms.CharField(max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'formpadding form-control', 'placeholder': 'Name','aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}
        )
    )
    url_link = forms.CharField(max_length=50,
        widget=forms.TextInput(
            attrs={'class' : 'formpadding form-control', 'placeholder': 'Url link','aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}
        )
    )
    
