"""
Docs.
"""
from django import forms


class EthereumAddressField(forms.CharField):
    """
    Docs.
    """

    default_error_messages = {
        'invalid': 'Invalid Ethereum address.',
    }

    def __init__(self, *args, **kwargs):
        super(EthereumAddressField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        """
        Docs.
        """
        return super().to_python(value)
