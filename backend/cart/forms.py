from django import forms
from django.core.validators import RegexValidator


class CheckoutForm(forms.Form):

    def __init__(self, *args, **kwargs):
        checkout_type = kwargs.pop('checkout_type', 'cart')
        super().__init__(*args, **kwargs)

        if checkout_type == 'premium':
            self.fields.pop('pickup_location')

    full_name = forms.CharField(
        max_length=100,
        label="Full Name",
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )

    billing_address = forms.CharField(
        max_length=255,
        required=False,
        label="Billing Address",
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )

    card_number = forms.CharField(
        label="Card Number",
        validators=[RegexValidator(
            r'^\d{4} \d{4} \d{4} \d{4}$', 'Enter a valid card number in the format XXXX XXXX XXXX XXXX.')],
        widget=forms.TextInput(attrs={
            "placeholder": "1234 1234 1234 1234",
            "class": "form-control",
            "inputmode": "numeric",
            "maxlength": "19",
            "oninput": "formatCardNumber(this)"
        })
    )

    expiration_date = forms.CharField(
        label="Expiration Date (MM/YY)",
        validators=[RegexValidator(
            r'^(0[1-9]|1[0-2])\/\d{2}$', 'Enter date in MM/YY format.')],
        widget=forms.TextInput(
            attrs={"placeholder": "MM/YY", "class": "form-control"})
    )

    cvv = forms.CharField(
        label="CVV",
        validators=[RegexValidator(
            r'^\d{3,4}$', 'Enter a valid 3 or 4 digit CVV.')],
        widget=forms.TextInput(
            attrs={"placeholder": "123", "class": "form-control"})
    )

    PICKUP_LOCATIONS = [
        ("", "-----------------------"),
        ("neumarkt", "Neumarkt 9-19, 04109 Leipzig, Germany"),
        ("karl_liebknecht", "Karl-Liebknecht-Straße 128, 04275 Leipzig, Germany"),
        ("oststrasse", "Oststraße 2, 04317 Leipzig, Germany"),
        ("brandtplatz", "Willi-Brandt-Platz 5, 04109 Leipzig, Germany"),
        ("ludwigsburger", "Ludwigsburger Straße 9, 04209 Leipzig, Germany"),
        ("paunsdorf", "Paunsdorfer Allee 1, 04329 Leipzig, Germany"),
        ("airport", "Terminalring 11, 04435 Leipzig-Halle (LEJ Airport), Germany"),
        ("bruenner", "Brünner Straße 28, 04209 Leipzig, Germany"),
        ("brandtplatz2", "Willy-Brandt-Platz 7, 04109 Leipzig, Germany"),
        ("erhard", "Ludwig-Erhard-Straße 14, 04103 Leipzig, Germany"),
        ("bornaische", "Bornaische Straße 140, 04279 Leipzig, Germany"),
        ("maximilianallee", "Maximilianallee 16, 04129 Leipzig, Germany"),
        ("tierkliniken", "An den Tierkliniken 42, 04103 Leipzig, Germany"),
        ("georg_schumann", "Georg-Schumann-Straße 133, 04155 Leipzig, Germany"),
        ("taucha", "Leipziger Straße 102, 04425 Taucha, Germany"),
    ]

    pickup_location = forms.ChoiceField(
        choices=PICKUP_LOCATIONS,
        label="Pickup Location",
        widget=forms.Select(attrs={
            "class": "form-select"
        })
    )

    def clean_pickup_location(self):
        data = self.cleaned_data['pickup_location']
        if data == "":
            raise forms.ValidationError(
                "Please select a valid pickup location.")
        return data
