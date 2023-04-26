from django import forms


class TopicForm(forms.Form):
    name=forms.CharField(max_length=10)
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(max_length=20,required=False,widget=forms.HiddenInput)


    def clean(self):
        name=self.cleaned_data['name']
        email=self.cleaned_data['email']
        remail=self.cleaned_data['re_enter_email']
        if email!=remail:
            raise forms.ValidationError('not valid data')


        return ('not valid data')
    def clean_botcatcher(self):
        bc=self.cleaned_data['botcatcher']
        if len(bc)>0:
            raise forms.ValidationError('not valid data')
        return

