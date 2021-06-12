from django import forms


class SearchForm(forms.Form):
    search_text = forms.CharField(label='Search field', max_length=100)
    search_category = forms.ChoiceField(widget=forms.RadioSelect, choices=[
        ('title', 'title'),
        ('author', 'author'),
        ('category', 'category')
    ])


class RatingForm(forms.Form):
    number_value = forms.ChoiceField(widget=forms.RadioSelect, choices=[
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ])
