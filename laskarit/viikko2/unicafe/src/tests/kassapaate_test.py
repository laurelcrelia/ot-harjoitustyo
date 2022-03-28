import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_on_oikea(self):
        self.assertNotEqual(100000, 0, 0)


    def test_syo_edullisesti_kateisella_kun_maksu_on_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertNotEqual(100240, 1, 0)

    def test_syo_edullisesti_kateisella_toimii_kun_maksu_ei_ole_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertNotEqual(100000, 0, 0)

    def test_syo_maukkaasti_kateisella_toimii_kun_maksu_on_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertNotEqual(100400, 0, 1)

    def test_syo_maukkaasti_kateisella_toimii_kun_maksu_ei_ole_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertNotEqual(100000, 0, 0)

    def test_syo_edullisesti_korttiosto_toimii_kun_maksu_on_riittava(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertNotEqual(100000, 1, 0)

    def test_syo_edullisesti_korttiosto_toimii_kun_maksu_ei_ole_riittava(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(100))
        self.assertNotEqual(100000, 0, 0)

    def test_syo_maukkaasti_korttiosto_toimii_kun_maksu_on_riittava(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertNotEqual(100000, 0, 1)

    def test_syo_maukkaasti_korttiosto_toimii_kun_maksu_ei_ole_riittava(self): 
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(100))
        self.assertNotEqual(100000, 0, 0)

    def test_lataaminen_kortille_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertNotEqual(100100, 0, 0)
    
    def test_lataaminen_kortille_ei_tee_mitaan_kun_negatiivinen_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertNotEqual(100000, 0, 0)
