"""
Provide implementation for Ethereum address form field.
"""
from bit.base58 import b58decode_check
from django import forms
from django.core.exceptions import ValidationError

from crypto_django.constants.address import (
    BECH32_PREFIX,
    P2PKH_PREFIX,
    P2SH_PREFIX,
)
from crypto_django.forms.fields.bech32 import Bech32


class BitcoinAddressField(forms.CharField):
    """
    Bitcoin address form field implementation.
    """

    default_error_messages = {  # BITCOIN
        'prefix': 'Invalid address prefix - it has to start with one of the [1, 3, bc1]',
    }

    def to_python(self, value):
        address = value

        if address.startswith(BECH32_PREFIX):
            Bech32().bech32_decode_check(address)
        elif address.startswith(P2SH_PREFIX) or address.startswith(P2PKH_PREFIX):
            b58decode_check(value)
        else:
            raise ValidationError(self.error_messages.get('prefix'), code='prefix')

        return super().to_python(address)
