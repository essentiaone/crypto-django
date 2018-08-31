"""
Provide implementation for Litecoin address form field.
"""
from crypto_django.constants.address import (
    LITECOIN_BECH32_PREFIX,
    LITECOIN_P2SH_PREFIX,
    LITECOIN_P2PKH_PREFIX,
    MIN_LITECOIN_ADDRESS_LENGTH,
    REQUIRED_LITECOIN_ADDRESS_LENGTH,
)
from crypto_django.forms.abc.fields.addresses.bitcoin import AbstractBitcoinAddressField


class LitecoinAddressField(AbstractBitcoinAddressField):
    """
    Litecoin address form field implementation.
    """

    @property
    def bech32_prefix(self):
        """
        Initialize bech32 address prefix.
        """
        return LITECOIN_BECH32_PREFIX

    @property
    def p2sh_prefix(self):
        """
        Initialize p2sh address prefix.
        """
        return LITECOIN_P2SH_PREFIX

    @property
    def p2pkh_prefix(self):
        """
        Initialize p2pkh address prefix.
        """
        return LITECOIN_P2PKH_PREFIX

    @property
    def min_address_length(self):
        """
        Initialize minimal address length.
        """
        return MIN_LITECOIN_ADDRESS_LENGTH

    @property
    def required_address_length(self):
        """
        Initialize maximal address length.
        """
        return REQUIRED_LITECOIN_ADDRESS_LENGTH
