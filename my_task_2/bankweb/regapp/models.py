from django import forms

class BankForm(forms.Form):
    name = forms.CharField(label='Name')
    dob = forms.DateField(label='DOB')
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], label='Gender')
    phone_number = forms.CharField(label='Phone Number')
    mail_id = forms.EmailField(label='Mail ID')
    address = forms.CharField(label='Address')
    district = forms.ChoiceField(choices=[('Ernakulam', 'Ernakulam'), ('Other', 'Other')], label='District')
    branch = forms.ChoiceField(choices=[('edappaly', 'edappaly'), ('current', 'Aluva')], label='Branch')
    account_type = forms.ChoiceField(choices=[('savings', 'Savings Account'), ('current', 'Current Account')], label='Account Type')
    materials_provided = forms.MultipleChoiceField(choices=[('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'), ('cheque_book', 'Cheque Book')], widget=forms.CheckboxSelectMultiple, label='Materials Provided')

