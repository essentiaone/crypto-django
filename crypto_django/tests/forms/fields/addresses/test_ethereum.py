"""
Provide tests for Ethereum address form field.
"""
from unittest import TestCase

from django.core.exceptions import ValidationError

from crypto_django.forms.fields.addresses.ethereum import EthereumAddressField


class TestEthereumAddressField(TestCase):
    """
    Test cases for Ethereum address form field.
    """

    def setUp(self):
        """
        Setup.
        """
        self.required_length_invalid_address = '0xb563Dde324fa9842E74bbf98571e9De4FD5FE9'
        self.no_hex_invalid_address = 'deb563Dde324fa9842E74bbf98571e9De4FD5FE9bA'
        self.not_valid_address = '0xb563Dde324fa9842E74bbf98571e9De4FD5FEvvv'
        self.valid_address = '0xb563Dde324fa9842E74bbf98571e9De4FD5FE9bA'

        self.ethereum_address_field = EthereumAddressField()

    def test_required_length_error(self):
        """
        Case: validate address with invalid required length (less than needed).
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.ethereum_address_field.to_python(value=self.required_length_invalid_address)

    def test_no_hex_address_error(self):
        """
        Case: validate address without `0x` at the start.
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.ethereum_address_field.to_python(value=self.no_hex_invalid_address)

    def test_not_valid(self):
        """
        Case: validate address with official Ethereum utils library for address validation.
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.ethereum_address_field.to_python(value=self.not_valid_address)

    def test_valid(self):
        """
        Case: validate correct address.
        Expect: value put to `to_python` (address) is returned.
        """
        valid_address = self.ethereum_address_field.to_python(value=self.valid_address)
        self.assertEqual(self.valid_address, valid_address)
