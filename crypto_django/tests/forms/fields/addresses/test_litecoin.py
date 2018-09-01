"""
Provide tests for Litecoin address form field.
"""
from unittest import TestCase

from django.core.exceptions import ValidationError

from crypto_django.forms.fields.addresses.litecoin import LitecoinAddressField


class TestLitecoinAddressField(TestCase):
    """
    Test cases for Litecoin address form field.
    """

    def setUp(self):
        """
        Setup.
        """
        self.required_length_invalid_address = 'LTNJvXUJeRi41DJuEg5V3zWRhUisC3KUtFs'
        self.another_invalid_address = '3MLiqxr3iyER1mZkrdvt83c99P1bsGjqH2'
        self.not_valid_address = 'LTNJvXUJeRi41DJuEg5V3zWRhUisC3KUtFsxxx'
        self.valid_address = 'LTNJvXUJeRi41DJuEg5V3zWRhUisC3KUtF'
        self.segwit_address = 'MAsPueJv1rQrRcRDLYb2YjCfNU9BCnEUmM'

        self.litecoin_address_field = LitecoinAddressField()

    def test_required_length_error(self):
        """
        Case: validate address with invalid required length (less than needed).
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.litecoin_address_field.to_python(value=self.required_length_invalid_address)

    def test_another_address_error(self):
        """
        Case: validate address from another wallet.
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.litecoin_address_field.to_python(value=self.another_invalid_address)

    def test_not_valid(self):
        """
        Case: validate address with official Litecoin utils library for address validation.
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.litecoin_address_field.to_python(value=self.not_valid_address)

    def test_valid(self):
        """
        Case: validate correct address.
        Expect: value put to `to_python` (address) is returned.
        """
        valid_address = self.litecoin_address_field.to_python(value=self.valid_address)
        self.assertEqual(self.valid_address, valid_address)

    def test_valid_segwit(self):
        """
        Case: validate correct SegWit address.
        Expect: value put to `to_python` (address) is returned.
        """
        valid_address = self.litecoin_address_field.to_python(value=self.segwit_address)
        self.assertEqual(self.segwit_address, valid_address)
