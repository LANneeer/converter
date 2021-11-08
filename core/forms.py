from django import forms


class TranslateForm(forms.Form):
    text_input = forms.CharField(widget=forms.Textarea(attrs={'class': "translator__textarea", 'name': "from",
                                                              'cols': "30", 'rows': "10"}), label='', required=False)
    text_output = forms.CharField(widget=forms.Textarea(attrs={'class': "translator__textarea", 'name': "to",
                                                               'cols': "30", 'rows': "10"}),
                                  label='', required=False)


