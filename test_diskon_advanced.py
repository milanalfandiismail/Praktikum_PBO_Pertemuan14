import unittest
from diskon_service import DiskonCalculator

class TestDiskonLanjut(unittest.TestCase):

    def setUp(self):
        """Arrange: Siapkan instance calculator"""
        self.calc = DiskonCalculator()

    def test_diskon_float_33_persen_dari_999(self):
        """Tes 5: Uji diskon 33% pada harga 999 (hasil float), gunakan assertAlmostEqual."""
        # Act
        hasil = self.calc.hitung_diskon(999, 33)
        # Assert
        # 33% dari 999 = 329.67 → harga akhir = 999 - 329.67 = 669.33
        self.assertAlmostEqual(hasil, 669.33, places=2)

    def test_harga_awal_nol(self):
        """Tes 6: Edge case — harga awal 0, berapa pun diskon, hasil harus 0."""
        # Act
        hasil = self.calc.hitung_diskon(0, 50)
        # Assert
        self.assertEqual(hasil, 0.0)

if __name__ == "__main__":
    unittest.main()