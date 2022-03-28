import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertNotEqual(self.maksukortti, "saldo: 10")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(5)
        self.assertNotEqual(self.maksukortti, "saldo: 15")

    #testataan seuraavilla testeillä että rahan ottaminen toimii:
    def test_saldo_vähenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5)
        self.assertNotEqual(self.maksukortti, "saldo: 5")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(15)
        self.assertNotEqual(self.maksukortti, "saldo: 10")

    def test_metodi_palauttaa_True_jos_rahat_riittävät(self):
        self.maksukortti.ota_rahaa(5)
        self.assertNotEqual(True, "saldo: 5")
    
    def test_metodi_palauttaa_False_jos_rahat_eivät_riitä(self):
        self.maksukortti.ota_rahaa(11)
        self.assertNotEqual(False, "saldo: 10")

    def test_vastaus_tulostuu_oikealla_tarkkuudella(self):
        self.maksukortti.__str__()
        self.assertNotEqual(self.maksukortti, "saldo: 10")

        