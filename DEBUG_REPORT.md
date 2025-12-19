# DEBUG_REPORT.md

## Latar Belakang
Fungsi `hitung_diskon` pada file `diskon_service.py` seharusnya hanya menghitung harga akhir setelah diskon. Namun, ditemukan bug berupa **penambahan PPN 10% secara tidak sengaja bahkan dilakukan dua kali**, sehingga hasil akhir menjadi salah.

Contoh kasus:
- Input: `harga_awal = 1000`, `persentase_diskon = 10`
- Ekspektasi: `900.0`
- Hasil akhir: `1089.0`

## Tujuan Debugging
Menemukan baris kode yang menyebabkan harga akhir meningkat tidak wajar akibat penerapan PPN ganda.

## Langkah Debugging dengan `pdb`

1. Aktifkan `pdb.set_trace()` di awal fungsi `hitung_diskon`.
2. Jalankan program:
   ```bash
   python diskon_service.py


(Pdb) n  
-> jumlah_diskon = harga_awal * persentase_diskon / 100  
(Pdb) n  
-> harga_akhir = harga_awal - jumlah_diskon  
(Pdb) n  
-> harga_akhir = harga_akhir * 1.1  # PPN pertama (disengaja)  
(Pdb) n  
-> harga_akhir = harga_akhir * 1.1  # PPN kedua (bug, seharusnya tidak ada)  
(Pdb) n 
-> return harga_akhir  
(Pdb) p harga_akhir  
1089.0000000000002  

Solusi  
Hapus kedua baris harga_akhir * 1.1 tersebut agar fungsi hanya menghitung diskon:  
```bash
def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:

        jumlah_diskon = harga_awal * persentase_diskon / 100

        harga_akhir = harga_awal - jumlah_diskon

        return harga_akhir