"""
Provide implementation for Bitcoin address form field.
"""
from bit.base58 import b58decode_check
from django import forms
from django.core.exceptions import ValidationError

from crypto_django.constants.address import (
    BECH32_PREFIX,
    P2PKH_PREFIX,
    P2SH_PREFIX,
    REQUIRED_BITCOIN_ADDRESS_LENGTH,
)
from crypto_django.forms.fields.bech32 import Bech32


class BitcoinAddressField(forms.CharField):
    """
    Bitcoin address form field implementation.
    """

    default_error_messages = {
        'bech32': 'Invalid bech32 address',
        'length': 'Ensure address has %(required_address_length)d character (it has %(current_address_length)d).',
        'p2': 'Invalid P2PKH/P2SH address. %(b58decode_error)s',
        'prefix': 'Invalid address prefix - it has to start with one of the [1, 3, bc1]',
    }

    def to_python(self, value):
        """
        Validate Bitcoin address.

        References:
            - github.com/bitcoin/bips/blob/master/bip-0173.mediawiki
            - github.com/ofek/bit/blob/e5640cbc79c183b8c4051b46b3ccf3e813e021d3/bit/base58.py
            - github.com/sipa/bech32/blob/master/ref/python/segwit_addr.py
        """
        address = value
        address_length = len(address)
        prefixes = [P2SH_PREFIX, P2PKH_PREFIX, BECH32_PREFIX]

        if address_length < REQUIRED_BITCOIN_ADDRESS_LENGTH:
            error_message_params = {
                'required_address_length': REQUIRED_BITCOIN_ADDRESS_LENGTH,
                'current_address_length': address_length,
            }
            raise ValidationError(self.error_messages.get('length'), code='length', params=error_message_params)

        if not any([address.startswith(prefix) for prefix in prefixes]):
            raise ValidationError(self.error_messages.get('prefix'), code='prefix')

        if address.startswith(BECH32_PREFIX) and not Bech32().bech32_decode(address):
            # Checksum validation for segwit addresses
            raise ValidationError(self.error_messages.get('bech32'), code='bech32')

        if address.startswith(P2SH_PREFIX) or address.startswith(P2PKH_PREFIX):
            # Checksum validation for P2KH/P2SH addresses
            try:
                b58decode_check(value)
            except ValueError as error_message:
                error_message_params = {
                    'b58decode_error': error_message,
                }
                raise ValidationError(self.error_messages.get('p2'), code='p2', params=error_message_params)

        return super().to_python(address)
