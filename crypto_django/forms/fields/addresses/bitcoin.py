"""
Provide implementation for Bitcoin address form field.
"""
from crypto_django.constants.address import (
    BITCOIN_BECH32_PREFIX,
    BITCOIN_P2SH_PREFIX,
    BITCOIN_P2PKH_PREFIX,
    MIN_BITCOIN_ADDRESS_LENGTH,
    REQUIRED_BITCOIN_ADDRESS_LENGTH,
)
from crypto_django.forms.abc.fields.addresses.bitcoin import AbstractBitcoinAddressField


class BitcoinAddressField(AbstractBitcoinAddressField):
    """
    Bitcoin address form field implementation.
    """

    @property
    def bech32_prefix(self):
        """
        Initialize bech32 address prefix.
        """
        return BITCOIN_BECH32_PREFIX

    @property
    def p2sh_prefix(self):
        """
        Initialize p2sh address prefix.
        """
        return BITCOIN_P2SH_PREFIX

    @property
    def p2pkh_prefix(self):
        """
        Initialize p2pkh address prefix.
        """
        return BITCOIN_P2PKH_PREFIX

    @property
    def min_address_length(self):
        """
        Initialize minimal address length.
        """
        return MIN_BITCOIN_ADDRESS_LENGTH

    @property
    def required_address_length(self):
        """
        Initialize maximal address length.
        """
        return REQUIRED_BITCOIN_ADDRESS_LENGTH
