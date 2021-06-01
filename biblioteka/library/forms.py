from django import forms


class SearchForm(forms.Form):
    search_text = forms.CharField(label='Search field', max_length=100)
    search_category = forms.ChoiceField(widget=forms.RadioSelect, choices=[
        ('title', 'title'),
        ('author', 'author')
    ])
