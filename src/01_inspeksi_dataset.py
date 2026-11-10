"""
Project: RainPredict
Tahap: Minggu 1 - Persiapan Project dan Eksplorasi Awal Dataset
Deskripsi:
    Script ini bertujuan untuk memeriksa struktur file cuaca.csv tanpa mengubah
    atau memanipulasi data mentah. Script membaca metadata, kolom, rentang waktu,
    serta mendeteksi penanda missing value dan kode kualitas sesuai dokumentasi SACA&D.
"""

from io import StringIO
import os
import pandas as pd


def load_raw_dataset(filepath: str) -> pd.DataFrame:
    """Membaca dataset cuaca.csv mentah dengan melewati baris metadata."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File tidak ditemukan: {filepath}")

    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip().replace(";;", "") for line in f if line.strip()]

    # Menemukan letak header tabel
    header_idx = None
    for idx, line in enumerate(lines):
        if "SOUID" in line and "DATE" in line:
            header_idx = idx
            break

    if header_idx is None:
        raise ValueError("Header tabel (SOUID, DATE, RR, Q_RR) tidak ditemukan.")

    # Membaca data tabular ke dalam DataFrame Pandas
    csv_stream = StringIO("\n".join(lines[header_idx:]))
    df = pd.read_csv(csv_stream, skipinitialspace=True)
    return df


def inspect_dataset(df: pd.DataFrame) -> None:
    """Mencetak ringkasan inspeksi dataset sesuai checklist Minggu 1."""
    print("=" * 60)
    print("HASIL INSPEKSI STRUKTUR DATASET (MINGGU 1)")
    print("=" * 60)

    # 1. Dimensi dan Kolom
    print(f"\n1. Dimensi Dataset : {df.shape[0]} baris x {df.shape[1]} kolom")
    print(f"   Daftar Kolom    : {df.columns.tolist()}")

    # 2. Tipe Data Kolom
    print("\n2. Tipe Data Kolom:")
    for col, dtype in df.dtypes.items():
        print(f"   - {col:7s} : {dtype}")

    # 3. Rentang Waktu
    min_date = str(df["DATE"].min())
    max_date = str(df["DATE"].max())
    print("\n3. Rentang Waktu:")
    print(f"   - Dari : {min_date[:4]}-{min_date[4:6]}-{min_date[6:]} ({min_date})")
    print(f"   - Sampai: {max_date[:4]}-{max_date[4:6]}-{max_date[6:]} ({max_date})")

    # 4. Sumber Stasiun (SOUID)
    souids = df["SOUID"].unique().tolist()
    print("\n4. Identifikasi Stasiun (SOUID):")
    print(f"   - Jumlah SOUID unik : {len(souids)}")
    for souid in souids:
        count = (df["SOUID"] == souid).sum()
        print(f"   - SOUID {souid:<6} : {count:6d} observasi ({count/len(df)*100:5.2f}%)")

    # 5. Kode Kualitas (Q_RR) & Missing Value
    print("\n5. Pemeriksaan Nilai Missing Value & Kualitas (Q_RR):")
    missing_rr_count = (df["RR"] == -9999).sum()
    print(f"   - Observasi RR bernilai -9999 (Missing Value) : {missing_rr_count} baris ({missing_rr_count/len(df)*100:5.2f}%)")
    print("   - Distribusi Kode Kualitas Q_RR:")
    for q_val, count in df["Q_RR"].value_counts().items():
        keterangan = {0: "Valid", 1: "Suspect (Meragukan)", 9: "Missing"}.get(q_val, "Tidak Terdefinisi")
        print(f"     * Q_RR = {q_val} ({keterangan:<20}) : {count:6d} baris ({count/len(df)*100:5.2f}%)")

    # 6. Sampel Data Awal dan Akhir
    print("\n6. Cuplikan 5 Baris Teratas:")
    print(df.head())

    print("\n7. Cuplikan 5 Baris Terbawah:")
    print(df.tail())
    print("\n" + "=" * 60)


if __name__ == "__main__":
    raw_path = os.path.join("data_raw", "cuaca.csv")
    df_raw = load_raw_dataset(raw_path)
    inspect_dataset(df_raw)
