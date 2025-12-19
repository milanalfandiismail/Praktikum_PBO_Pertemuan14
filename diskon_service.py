# diskon_service.py
import pdb

class DiskonCalculator:
    """Menghitung harga akhir setelah diskon."""

    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:

        jumlah_diskon = harga_awal * persentase_diskon / 100

        harga_akhir = harga_awal - jumlah_diskon

        # : PPN 10% diterapkan DUA KALI secara tidak sengaja
        harga_akhir = harga_akhir * 1.1  # PPN pertama (disengaja)
        harga_akhir = harga_akhir * 1.1  # PPN kedua (bug, seharusnya tidak ada)

        return harga_akhir

# -- UJI COBA (CASE GAGAL)

if __name__ == '__main__':
    calc = DiskonCalculator()
    hasil = calc.hitung_diskon(1000, 10)
    print (f"Hasil : {hasil}")