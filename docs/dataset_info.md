# RainPredict — Dokumentasi Dataset & Persiapan Project (Minggu 1)

## 1. Ringkasan Dataset
Dataset yang digunakan berasal dari **SACA&D (Southeast Asian Climate Assessment & Dataset)** yang dikelola dalam kerja sama dengan BMKG dan ICA&D.

- **Sumber Data**: SACA&D ([http://sacad.database.bmkg.go.id/](http://sacad.database.bmkg.go.id/) / [http://saca-bmkg.knmi.nl](http://saca-bmkg.knmi.nl))
- **Sitasi Resmi**:
  > van den Besselaar and Coauthors, 2015. *International Climate Assessment & Dataset (ICA&D): climate services across borders.* Bull. Amer. Meteor. Soc., January, 16-21, doi:10.1175/BAMS-D-13-00249.1.
- **Nama Stasiun Utama**: **STASIUN KLIMATOLOGI SEMARANG**
  - **Station ID (STAID)**: `133`
  - **Negara**: Indonesia (`ID`)
  - **Koordinat**: Lintang `-06:59:05` (LS), Bujur `+110:22:52` (BT)
  - **Elevasi (HGTH)**: 6 meter dpl
- **Karakteristik Seri Data**: Merupakan *blended time series* yang menggabungkan 3 sumber data pengamatan (SOUID).

---

## 2. Rincian Sumber Pengamatan (Sources / SOUID)
Berdasarkan `stations.txt` dan `sources.txt`, seri data stasiun 133 ini disusun dari 3 sumber data (*Source Identifier*):

| SOUID | Nama Sumber (SOUNAME) | Koordinat (LAT, LON) | Elevasi | Elemen | Rentang Waktu Sumber | Keterangan / Participant |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **102002** | STASIUN KLIMATOLOGI SEMARANG | -06:59:05, +110:22:52 | 6 m | RR2 | 1980-01-01 s/d 1985-12-31 | JAMSTEC digitization project |
| **996837** | SEMARANG | -06:58:00, +110:25:00 | 3 m | RR7 | 1977-01-30 s/d 2020-03-30 | BMKG Station |
| **996839** | SEMARANG/AHMAD YANI | -06:59:00, +110:23:00 | 3 m | RR7 | 1957-08-19 s/d 2020-03-30 | Stasiun Meteorologi Ahmad Yani |

---

## 3. Kamus Kolom Dataset (`cuaca.csv`)
File `cuaca.csv` memiliki 20 baris metadata awal, diikuti oleh data tabular dengan 4 kolom utama:

| Nama Kolom | Tipe Data Awal | Deskripsi Kolom | Satuan / Format | Nilai Khusus |
| :--- | :--- | :--- | :--- | :--- |
| **`SOUID`** | Integer | Source Identifier (kode unik sumber stasiun pengamatan) | Kode ID | `102002`, `996837`, `996839` |
| **`DATE`** | Integer / String | Tanggal pengamatan harian | Format `YYYYMMDD` (contoh: `19800101`) | Rentang: 1 Januari 1980 s/d 31 Desember 2025 |
| **`RR`** | Integer | *Precipitation amount* (curah hujan harian) | **0.1 mm** *(Perhatian: nilai 230 berarti 23.0 mm)* | `-9999` adalah kode resmi **Missing Value** |
| **`Q_RR`** | Integer | Kode kualitas pengamatan (*Quality code*) | Kategori kualitas | `0` = Valid<br>`1` = Suspect (meragukan)<br>`9` = Missing |

> [!IMPORTANT]
> **Poin Kritis Satuan dan Missing Value:**
> 1. Nilai `RR` berada dalam skala **0.1 mm**, sehingga konversi ke mm memerlukan pembagian 10 (`RR / 10`).
> 2. Nilai `-9999` **bukan curah hujan negatif**, melainkan penanda *missing value*.
> 3. Nilai `RR == 0` adalah **hari tanpa hujan (valid)** dan tidak boleh diubah menjadi missing value.
> 4. Status kualitas `Q_RR`: nilai `0` menandakan pengamatan valid, `1` suspect, dan `9` pengamatan hilang/missing.

---

## 4. Statistik Awal Dataset Mentah
- **Total Baris Data**: 16.802 baris (1 Januari 1980 – 31 Desember 2025, ~46 tahun)
- **Jumlah Missing Value (`RR == -9999` / `Q_RR == 9`)**: 5.013 baris
- **Sebaran Kode Kualitas `Q_RR`**:
  - `0` (Valid): 11.785 baris
  - `9` (Missing): 5.013 baris
  - `1` (Suspect): 4 baris

---

## 5. Struktur Folder Project RainPredict
```text
RainPredict Project/
├── data_raw/                  # Dataset mentah tanpa modifikasi
│   ├── cuaca.csv              # Data curah hujan SACA&D
│   ├── sources.txt            # Metadata sumber stasiun
│   ├── stations.txt           # Metadata stasiun pengamatan
│   └── SACA_blended_custom.zip# Arsip unduhan asli
├── data_cleaning/             # Tempat output dataset hasil pembersihan (Minggu 2)
├── src/                       # Kode program modular & script eksplorasi
│   └── 01_inspeksi_dataset.py # Script inspeksi & validasi struktur (Minggu 1)
├── notebooks/                 # (Opsional) Jupyter Notebook untuk visualisasi & eksperimen
├── docs/                      # Dokumentasi project & kamus data
│   └── dataset_info.md        # Catatan detail dataset & lisensi
├── .gitignore                 # Filter file sementara / file besar
└── Readme.md                  # Dokumentasi utama & roadmap project
```
