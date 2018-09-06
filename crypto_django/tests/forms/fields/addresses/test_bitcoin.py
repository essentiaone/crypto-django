"""
Provide tests for Bitcoin address form field.
"""
from unittest import TestCase

from django.core.exceptions import ValidationError

from crypto_django.forms.fields.addresses.bitcoin import BitcoinAddressField


class TestBitcoinAddressField(TestCase):
    """
    Test cases for Bitcoin address form field.
    """

    def setUp(self):
        """
        Setup.
        """
        self.required_length_invalid_address = '16DWEqF6pX314CjV5u2dmiMhcXtyY6z7'
        self.another_invalid_address = 'LMLiqxr3iyER1mZkrdvt83c99P1bsGjqH2'
        self.not_valid_address = '16DWEqF6pX314CjV5u2dmiMhcXtyY6z7odzz'
        self.valid_address = '16DWEqF6pX314CjV5u2dmiMhcXtyY6z7od'
        self.segwit_address = '3MLiqxr3iyER1mZkrdvt83c99P1bsGjqH2'

        self.bitcoin_address_field = BitcoinAddressField()

    def test_required_length_error(self):
        """
        Case: validate address with invalid required length (less than needed).
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.bitcoin_address_field.to_python(value=self.required_length_invalid_address)

    def test_another_address_error(self):
        """
        Case: validate address from another wallet.
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.bitcoin_address_field.to_python(value=self.another_invalid_address)

    def test_not_valid(self):
        """
        Case: validate address with official Bitcoin utils library for address validation.
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.bitcoin_address_field.to_python(value=self.not_valid_address)

    def test_valid(self):
        """
        Case: validate correct address.
        Expect: value put to `to_python` (address) is returned.
        """
        valid_address = self.bitcoin_address_field.to_python(value=self.valid_address)
        self.assertEqual(self.valid_address, valid_address)

    def test_valid_segwit(self):
        """
        Case: validate correct SegWit address.
        Expect: value put to `to_python` (address) is returned.
        """
        valid_address = self.bitcoin_address_field.to_python(value=self.segwit_address)
        self.assertEqual(self.segwit_address, valid_address)
