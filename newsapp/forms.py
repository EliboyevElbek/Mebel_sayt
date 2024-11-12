from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label= False, widget=forms.TextInput(attrs={'class': 'email-bt', 'placeholder':'Ism'}))
    phone = forms.CharField(max_length=15, label= False, widget=forms.TextInput(attrs={'class': 'email-bt', 'placeholder':'Telqfon raqam'}))
    message = forms.CharField(label= False, widget=forms.Textarea(attrs={'class': 'massage-bt', 'placeholder':'Xabaringizni kiriting'}))


class ContactBuyForm(forms.Form):
    key = forms.CharField(max_length=20, label=False, widget=forms.TextInput(attrs={'class': 'email-bt', 'placeholder':'Mebel ID\'si'}))
    name = forms.CharField(max_length=100, label= False, widget=forms.TextInput(attrs={'class': 'email-bt', 'placeholder':'Ism'}))
    phone = forms.CharField(max_length=15, label= False, widget=forms.TextInput(attrs={'class': 'email-bt', 'placeholder':'Telqfon raqam'}))
    message = forms.CharField(label= False, widget=forms.Textarea(attrs={'class': 'massage-bt', 'placeholder':'Xabaringizni kiriting'}))


class SearchForm(forms.Form):
    query = forms.CharField(label=False, max_length=100, widget=forms.TextInput(attrs={'class': 'email-bt', 'placeholder': 'Qidiruv'}))
