"""
Provide abstract behavior for Bitcoin-like address form field.
"""
from abc import abstractmethod

from bit.base58 import b58decode_check
from django import forms
from django.core.exceptions import ValidationError

from crypto_django.forms.fields.bech32 import Bech32


class AbstractBitcoinAddressField(forms.CharField):
    """
    Bitcoin-like address form field abstract implementation.
    """

    default_error_messages = {
        'bech32': 'Invalid bech32 address',
        'length': 'Ensure address must be %(min_address_length)s or %(required_address_length)s character '
                  '(it has %(current_address_length)d).',
        'p2': 'Invalid P2PKH/P2SH address. %(b58decode_error)s',
        'prefix': 'Invalid address prefix - it has to start with one of the '
                  '[%(bech32_prefix)s, %(legacy_prefix)s, %(segwit_prefix)s]',
    }

    @abstractmethod
    def bech32_prefix(self):
        """
        Initialize bech32 address prefix.
        """
        return

    @abstractmethod
    def p2sh_prefix(self):
        """
        Initialize p2sh address prefix.
        """
        return

    @abstractmethod
    def p2pkh_prefix(self):
        """
        Initialize p2pkh address prefix.
        """
        return

    @abstractmethod
    def min_address_length(self):
        """
        Initialize minimal address length.
        """
        return

    @abstractmethod
    def required_address_length(self):
        """
        Initialize maximal address length.
        """
        return

    def to_python(self, value):
        """
        Validate wallet address.

        References:
            - https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki
            - https://github.com/ofek/bit/blob/e5640cbc79c183b8c4051b46b3ccf3e813e021d3/bit/base58.py
            - https://github.com/sipa/bech32/blob/master/ref/python/segwit_addr.py
            - https://blog.trezor.io/litecoins-new-p2sh-segwit-addresses-843633e3e707
            - https://github.com/litecoin-project/litecoin/issues/312
            - https://github.com/sipa/bech32/blob/master/ref/python/segwit_addr.py
            - https://chaining.ru/2018/05/31/litecoin-core-v0-16-0-release-litecoin-project/
        """
        address = value
        address_length = len(address)
        prefixes = (self.p2sh_prefix, self.p2pkh_prefix, self.bech32_prefix)

        if address_length not in (self.min_address_length, self.required_address_length):
            error_message_params = {
                'min_address_length': self.min_address_length,
                'required_address_length': self.required_address_length,
                'current_address_length': address_length,
            }
            raise ValidationError(self.error_messages.get('length'), code='length', params=error_message_params)

        if not any([address.startswith(prefix) for prefix in prefixes]):
            error_message_params = {
                'bech32_prefix': self.bech32_prefix,
                'segwit_prefix': self.p2sh_prefix,
                'legacy_prefix': self.p2pkh_prefix,
            }
            raise ValidationError(self.error_messages.get('prefix'), code='prefix', params=error_message_params)

        if address.startswith(self.bech32_prefix) and not Bech32().bech32_decode(address):
            # Checksum validation for segwit addresses
            raise ValidationError(self.error_messages.get('bech32'), code='bech32')

        if address.startswith(self.p2sh_prefix) or address.startswith(self.p2pkh_prefix):
            # Checksum validation for P2KH/P2SH addresses
            try:
                b58decode_check(value)
            except ValueError as error_message:
                error_message_params = {
                    'b58decode_error': error_message,
                }
                raise ValidationError(self.error_messages.get('p2'), code='p2', params=error_message_params)

        return super().to_python(address)
