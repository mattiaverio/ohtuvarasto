import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto_neg_saldo = Varasto(10, -5)
        self.varasto_ylisaldo = Varasto(10, 15)
        self.varasto_neg_tilavuus = Varasto(-10, 5)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_tayteen_lisays_ei_ylita_tilavuutta(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_otto_palauttaa_nolla(self):
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_saldon_ylittava_otto_nollaa_saldon(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 5)

    def test_str(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_negatiivinen_saldo_alustetaan_nollaksi(self):
        self.assertAlmostEqual(self.varasto_neg_saldo.saldo, 0)

    def test_liian_suuri_alkusaldo_asettaa_saldon_tilavuuteen(self):
        self.assertAlmostEqual(self.varasto_ylisaldo.saldo, 10)

    def test_negatiivinen_tilavuus_nollataan(self):
        self.assertAlmostEqual(self.varasto_neg_tilavuus.tilavuus, 0)