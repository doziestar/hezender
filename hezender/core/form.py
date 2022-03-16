from django import forms


class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        message = cleaned_data.get("message")
        if name.lower() == "hezender":
            raise forms.ValidationError('Name cannot be "hezender"')
        if email.lower() == " ":
            raise forms.ValidationError("Email cannot be empty")
        if phone.lower() == " ":
            raise forms.ValidationError("Phone cannot be empty")
        if message.lower() == " ":
            raise forms.ValidationError("Message cannot be empty")
        return cleaned_data

    def submit(self):
        print("Submitted")
