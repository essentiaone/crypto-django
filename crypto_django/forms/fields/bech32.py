"""
Tools for checking segwit address validity.
"""
CHARSET = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"


class Bech32:
    """
    Algorithm implementation for checking addresses of Bech32 type.

    References:
        - github.com/bitcoin/bips/blob/master/bip-0173.mediawiki
        - github.com/sipa/bech32/blob/master/ref/python/segwit_addr.py
    """

    @staticmethod
    def bech32_hrp_expand(hrp):
        """
        Expand the HRP into values for checksum computation.
        """
        return [ord(x) >> 5 for x in hrp] + [0] + [ord(x) & 31 for x in hrp]

    @staticmethod
    def bech32_polymod(values):
        """
        Internal function that computes the Bech32 checksum.
        """
        generator = [0x3b6a57b2, 0x26508e6d, 0x1ea119fa, 0x3d4233dd, 0x2a1462b3]
        chk = 1
        for value in values:
            top = chk >> 25
            chk = (chk & 0x1ffffff) << 5 ^ value
            for i in range(5):
                chk ^= generator[i] if ((top >> i) & 1) else 0
        return chk

    def bech32_verify_checksum(self, hrp, data):
        """
        Verify a checksum given HRP and converted data characters.
        """
        return self.bech32_polymod(self.bech32_hrp_expand(hrp) + data) == 1

    def bech32_decode(self, bech):
        """
        Validate a Bech32 string, and determine HRP and data.
        """
        if ((any(ord(x) < 33 or ord(x) > 126 for x in bech)) or
                (bech.lower() != bech and bech.upper() != bech)):
            return (None, None)
        bech = bech.lower()
        pos = bech.rfind('1')
        if pos < 1 or pos + 7 > len(bech) or len(bech) > 90:
            return (None, None)
        if not all(x in CHARSET for x in bech[pos + 1:]):
            return (None, None)
        hrp = bech[:pos]
        data = [CHARSET.find(x) for x in bech[pos + 1:]]
        if not self.bech32_verify_checksum(hrp, data):
            return (None, None)
        return (hrp, data[:-6])
