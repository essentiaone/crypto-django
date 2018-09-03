"""
Provide implementation for Bitcoin Cash address form field.
"""
from cashaddress.convert import is_valid
from django import forms
from django.core.exceptions import ValidationError

from crypto_django.constants.address import (
    BITCOIN_CASH_NEW_PREFIXES,
    BITCOIN_CASH_OLD_PREFIXES,
    REQUIRED_BITCOIN_CASH_NEW_ADDRESS_LENGTH,
    REQUIRED_BITCOIN_CASH_OLD_ADDRESS_LENGTH,
)


class BitcoinCashAddressField(forms.CharField):
    """
    Bitcoin Cash address form field implementation.
    """

    default_error_messages = {
        'invalid': 'Invalid Bitcoin Cash address.',
        'length':
            'Ensure address has %(required_address_format_length)d character (it has %(current_address_length)d).',
        'prefix': 'Ensure address has \'bitcoincash:p\' or \'bitcoincash:q\' as thirteen first characters '
                  'for new address or has \'1\' or \'3\' as first character for old address.',
    }

    def to_python(self, value):
        """
        Validate Bitcoin Cash address.

        References:
            - https://github.com/bitcoincashorg/bitcoincash.org/blob/master/spec/cashaddr.md
            - https://github.com/oskyk/cashaddress
            - https://github.com/oskyk/cashaddress/blob/master/cashaddress/convert.py#L122
        """
        # parameter will be differ from overridden 'to_python' method
        # if `address` in function parameters instead of reassigning to it
        address = value

        address_length = len(address)

        address_first_character = address[:1]
        address_first_13_characters = address[:13]

        error_message_params = {
            'current_address_length': address_length,
        }

        if address_first_character in BITCOIN_CASH_OLD_PREFIXES:

            if address_length != REQUIRED_BITCOIN_CASH_OLD_ADDRESS_LENGTH:
                error_message_params.update({
                    'required_address_format_length': REQUIRED_BITCOIN_CASH_OLD_ADDRESS_LENGTH,
                })

                raise ValidationError(self.error_messages.get('length'), code='length', params=error_message_params)

            if not is_valid(address):
                raise ValidationError(self.error_messages.get('invalid'), code='invalid')

            return super().to_python(address)

        if address_first_13_characters in BITCOIN_CASH_NEW_PREFIXES:

            if address_length != REQUIRED_BITCOIN_CASH_NEW_ADDRESS_LENGTH:
                error_message_params.update({
                    'required_address_format_length': REQUIRED_BITCOIN_CASH_NEW_ADDRESS_LENGTH,
                })

                raise ValidationError(self.error_messages.get('length'), code='length', params=error_message_params)

            if not is_valid(address):
                raise ValidationError(self.error_messages.get('invalid'), code='invalid')

            return super().to_python(address)

        raise ValidationError(self.error_messages.get('prefix'), code='prefix', params=error_message_params)
