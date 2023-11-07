
from django import forms
from notes.models import Category





class NoteForm(forms.Form):
    title = forms.CharField(max_length=30)
    text = forms.CharField(widget=forms.Textarea, required=False)
    reminder = forms.CharField(max_length=30)
    category = forms.TypedChoiceField(coerce=lambda pk: Category.objects.all().get(pk=pk), choices=Category.objects.all().values_list('id', 'title'))

