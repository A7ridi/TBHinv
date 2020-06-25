from django import forms
from .models import Storage

class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['item', 'amount', 'choices_field', 'expected_need_in', 'location', 'issue_date']
    
    def clean_item(self): # Validates the Computer Name Field
        item = self.cleaned_data.get('item')
        if (item == ""):
            raise forms.ValidationError('This field cannot be left blank')
        return item

class ItemSearchForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['item', 'location']