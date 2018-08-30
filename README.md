# Crypto-Django

The API wrapper written in Python allow you to speak with Bridges REST API in pythonic way.

![Build](https://api.travis-ci.com/essentiaone/crypto-django.svg?branch=developp)
![Python35](https://img.shields.io/badge/Python-3.5-brightgreen.svg)
![Python36](https://img.shields.io/badge/Python-3.6-brightgreen.svg)
[![Release](https://img.shields.io/github/release/essentiaone/crypto-django.svg)](https://github.com/essentiaone/crypto-django/releases)

  * [Getting started](#getting-started)
  * [API documentation](#api)
    * [Forms](#forms)

## Getting started

Install package from terminal using `pip`:

```
$ pip3 install crypto-django
```

Simple usage of the library introduced below:

```python
from crypto_django.forms import EthereumAddressField
from django import forms


class EthreumTransactionForm(forms.Form):
    address_from = EthereumAddressField()
    address_to = EthereumAddressField()
    amount = FloatField()
    gas_limit = IntegerField()
    gas_price = IntegerField()


form = EthreumTransactionForm({
    'address_from': '0x4Aa548D7589f003486892777CBb0B70dff5d6949',
    'address_to': '0xb563Dde324fa9842E74bbf98571e9De4FD5FE9bA',
    'amount': 10.5,
    'gas_limit': 26000,
    'gas_price': 11
})

if form.is_valid():
    ...
    
return form.errors
```

## API

### Forms

#### Ethereum

Validate Ethreum address.

```python
from crypto_django.forms import EthereumAddressField
from django import forms


class EthreumTransactionForm(forms.Form):
    address = EthereumAddressField()


form = EthreumTransactionForm({
    'address': '0x4Aa548D7589f003486892777CBb0B70dff5d6949',
})
```

#### Bitcoin

Validate Bitcoin address.

```python
from crypto_django.forms import BitcoinAddressField
from django import forms


class BitcoinTransactionForm(forms.Form):
    address = BitcoinAddressField()


form = BitcoinTransactionForm({
    'address': '3MLiqxr3iyER1mZkrdvt83c99P1bsGjqH2',
})
```

#### Litecoin

Validate Litecoin address.

```python
from crypto_django.forms import LitecoinAddressField
from django import forms


class LitecoinTransactionForm(forms.Form):
    address = LitecoinAddressField()


form = BitcoinTransactionForm({
    'address': 'LTNJvXUJeRi41DJuEg5V3zWRhUisC3KUtF',
})
```
