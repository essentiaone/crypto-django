"""
Provide implementation for Ethereum address form field.
"""
from eth_utils import is_address
from django import forms
from django.core.exceptions import ValidationError

from crypto_django.constants.address import (
    HEX_PREFIX,
    REQUIRED_ETHEREUM_ADDRESS_LENGTH,
)


class EthereumAddressField(forms.CharField):
    """
    Ethereum address form field implementation.
    """

    default_error_messages = {
        'invalid': 'Invalid Ethereum address.',
        'length': 'Ensure address has %(required_address_length)d character (it has %(current_address_length)d).',
        'hex': 'Ensure address has \'0x\' as two first characters.',
    }

    def to_python(self, value):
        """
        Validate Ethereum address.

        References:
            - github.com/ethereum/eth-utils#is_addressvalue---bool
            - github.com/ethereum/eth-utils/blob/a5569fdac5f0e7575872ca3aad7802068974de6b/eth_utils/address.py#L55
            - github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md
        """
        # parameter will be differ from overridden 'to_python' method
        # if `address` in function parameters instead of reassigning to it
        address = value

        address_length = len(address)
        address_first_two_characters = address[:2]

        if address_length != REQUIRED_ETHEREUM_ADDRESS_LENGTH:
            error_message_params = {
                'required_address_length': REQUIRED_ETHEREUM_ADDRESS_LENGTH,
                'current_address_length': address_length,
            }

            raise ValidationError(self.error_messages.get('length'), code='length', params=error_message_params)

        if address_first_two_characters != HEX_PREFIX:
            raise ValidationError(self.error_messages.get('hex'), code='hex')

        if not is_address(address):
            raise ValidationError(self.error_messages.get('invalid'), code='invalid')

        return super().to_python(address)
