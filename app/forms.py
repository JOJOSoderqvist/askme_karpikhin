from django import forms


class RegisterForm(forms.Form):
    django_username = forms.CharField(max_length=20)
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField()
    repeat_password = forms.CharField()


class LoginForm(forms.Form):
    django_username = forms.CharField(max_length=20)
    password = forms.CharField()


class UserEditForm(forms.Form):
    django_username = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(required=False)
    username = forms.CharField(required=False)


class NewQuestionForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(max_length=1000)
    tags = forms.CharField()


class NewAnswerForm(forms.Form):
    answer_text = forms.CharField(max_length=1000)
