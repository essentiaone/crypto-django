"""
Provide tests for Bitcoin Cash address form field.
"""
from unittest import TestCase

from django.core.exceptions import ValidationError

from crypto_django.forms.fields.addresses.bitcoin_cash import BitcoinCashAddressField


class TestBitcoinCashAddressField(TestCase):
    """
    Test cases for Bitcoin Cash address form field.
    """

    def setUp(self):
        """
        Setup.
        """
        self.bitcoin_cash_address_field = BitcoinCashAddressField()

        self.invalid_prefix_address = 'qzahuzrezp0259h8zgtpuajkm34xqq9s8vpsq27'

    def test_invalid_prefix_error(self):
        """
        Case: validate address with invalid prefix.
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.bitcoin_cash_address_field.to_python(value=self.invalid_prefix_address)


class TestOldBitcoinCashAddressField(TestCase):
    """
    Test cases for old Bitcoin Cash address form field.
    """

    def setUp(self):
        """
        Setup.
        """
        self.bitcoin_cash_address_field = BitcoinCashAddressField()

        self.old_invalid_address_prefix = '8J6NLoiPfUCYVr46oHnDFZTYbzrMxp'
        self.old_invalid_address_lenght = '1J6NLoiPfUCYVr46oHnDFZTYbzrMxp'
        self.old_invalid_address = '1J6NLoiPfUCYVr46oHnDFZTYbzrMxerqU1'
        self.old_valid_address = '1J6NLoiPfUCYVr46oHnDFZTYbzrMxpyqU1'

    def test_invalid_prefix_error(self):
        """
        Case: validate address with invalid prefix.
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.bitcoin_cash_address_field.to_python(value=self.old_invalid_address_prefix)

    def test_invalid_address_len_error(self):
        """
        Case: validate address with old invalid required length (less than needed).
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.bitcoin_cash_address_field.to_python(value=self.old_invalid_address_lenght)

    def test_invalid_address_error(self):
        """
        Case: validate address with old invalid address.
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.bitcoin_cash_address_field.to_python(value=self.old_invalid_address)

    def test_valid(self):
        """
        Case: check if old address is valid.
        Expect: value put to `to_python` (address) is returned.
        """
        old_valid_address = self.bitcoin_cash_address_field.to_python(value=self.old_valid_address)
        self.assertEqual(self.old_valid_address, old_valid_address)


class TestNewBitcoinCashAddressField(TestCase):
    """
    Test cases for new Bitcoin Cash address form field.
    """

    def setUp(self):
        """
        Setup.
        """
        self.bitcoin_cash_address_field = BitcoinCashAddressField()

        self.new_invalid_address_prefix = 'litcoincash:qzahuzrezp0259h8zgtpuajkm34xqq9s8vpsq27qm0'
        self.new_invalid_address_lenght = 'bitcoincash:qzahuzrezp0259h8zgtpuajkm34x'
        self.new_invalid_address = 'bitcoincash:qzahuzrezp0259h8zgtpuajkm34xqq9s8vpsq27rew'
        self.new_valid_address = 'bitcoincash:qzahuzrezp0259h8zgtpuajkm34xqq9s8vpsq27qm0'

    def test_invalid_prefix_error(self):
        """
        Case: validate address with invalid prefix.
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.bitcoin_cash_address_field.to_python(value=self.new_invalid_address_prefix)

    def test_invalid_address_len_error(self):
        """
        Case: validate address with new invalid required length (less than needed).
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.bitcoin_cash_address_field.to_python(value=self.new_invalid_address_lenght)

    def test_invalid_address_error(self):
        """
        Case: validate address with new invalid address.
        Expect: validation error is raised.
        """
        with self.assertRaises(ValidationError):
            self.bitcoin_cash_address_field.to_python(value=self.new_invalid_address)

    def test_valid(self):
        """
        Case: check if new address is valid.
        Expect: value put to `to_python` (address) is returned.
        """
        new_valid_address = self.bitcoin_cash_address_field.to_python(value=self.new_valid_address)
        self.assertEqual(self.new_valid_address, new_valid_address)
