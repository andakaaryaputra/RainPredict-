1. Gambaran umum project RainPredict
RainPredict
8 minggu
Rainfall Analysis & Prediction
Sistem analisis dan prediksi curah hujan berdasarkan data historis untuk membantu mengidentifikasi pola musim hujan dan memperkirakan periode terjadinya musim hujan.
Fokus utama
Data Science
Bahasa pemrograman
Python
Pengolahan data
Pandas, NumPy
Visualisasi
Matplotlib, Seaborn
Pemodelan
Time Series
Version control
Git & GitHub
Hasil akhir yang ditargetkan:
Dataset curah hujan yang sudah dibersihkan dan tervalidasi.
Analisis pola curah hujan historis.
Visualisasi tren dan pola musim hujan.
Model prediksi curah hujan.
Evaluasi hasil prediksi.
Dokumentasi project di GitHub.
Catatan: Prediksi curah hujan dan penentuan awal musim hujan merupakan dua hal yang berkaitan, tetapi tidak sama. Kita harus menentukan definisi operasional musim hujan terlebih dahulu sebelum membuat kesimpulan mengenai waktunya.
2. Workflow RainPredict per minggu
Roadmap pengerjaan
Minggu 1 — Persiapan project dan dataset
Fondasi project
Membuat repository GitHub.
Menyusun struktur folder.
Memastikan sumber dan lisensi dataset.
Memahami kolom dataset.
Mengidentifikasi stasiun pengamatan.
Output: Repository awal dan dokumentasi dataset.
Minggu 2 — Data Cleaning
Mengatasi missing value.
Memeriksa data duplikat.
Memeriksa kode kualitas pengamatan.
Memeriksa nilai ekstrem.
Memvalidasi format tanggal dan satuan curah hujan.
Output: Dataset bersih dan tervalidasi.
Minggu 3 — Exploratory Data Analysis (EDA)
Memahami distribusi curah hujan.
Menghitung statistik deskriptif.
Menganalisis pola curah hujan bulanan.
Membandingkan pola antarperiode.
Mengidentifikasi pola musiman.
Output: Hasil EDA dan interpretasi awal.
Minggu 4 — Feature Engineering
Mengubah data harian menjadi agregasi yang sesuai.
Membuat fitur bulanan atau musiman.
Menentukan indikator musim hujan.
Memeriksa tren dan pola temporal.
Menentukan variabel yang digunakan untuk pemodelan.
Output: Dataset siap pemodelan.
Minggu 5 — Pengembangan Model
Menentukan pendekatan time series.
Membuat baseline model.
Membangun model prediksi.
Menentukan pembagian data training dan testing berdasarkan waktu.
Melatih model.
Output: Model prediksi awal.
Minggu 6 — Evaluasi Model
Menghitung MAE.
Menghitung RMSE.
Menghitung metrik tambahan jika diperlukan.
Membandingkan hasil prediksi dengan data aktual.
Memeriksa kemungkinan overfitting.
Output: Model terpilih dan laporan evaluasi.
Minggu 7 — Visualisasi dan Interpretasi
Membuat grafik aktual vs prediksi.
Menampilkan pola curah hujan.
Menginterpretasikan periode musim hujan.
Menjelaskan keterbatasan prediksi.
Menyusun hasil analisis.
Output: Visualisasi dan hasil interpretasi RainPredict.
Minggu 8 — Finalisasi dan Publikasi
Merapikan notebook dan script.
Menyusun README.md.
Menyimpan dependensi project.
Memeriksa struktur GitHub.
Membuat kesimpulan dan dokumentasi akhir.
Output: Repository RainPredict yang siap dipresentasikan.
3. Workflow detail dan prompt AI setiap minggu
Bagian ini yang akan menjadi pedoman utama pengerjaan. Setiap minggu memiliki tujuan, pekerjaan, hasil akhir, dan prompt yang bisa kamu berikan kepada ChatGPT.
Minggu 1 — Persiapan project dan dataset
Fokus: memahami data
Workflow:
Memeriksa struktur folder RainPredict.
Memeriksa sumber dataset dan dokumentasi aslinya.
Memahami arti setiap kolom.
Memeriksa satuan curah hujan.
Memeriksa identitas dan jumlah stasiun.
Membuat dokumentasi dataset.
Mengunggah struktur project ke GitHub.
Batasan:
Jangan melakukan manipulasi data sebelum memahami struktur dataset.
Jangan menghapus kolom yang belum dipahami.
Jangan menggabungkan data antarstasiun secara sembarangan.
Jangan mengunggah dataset mentah ke GitHub tanpa memeriksa lisensi dan ukurannya.
Jangan membuat asumsi bahwa seluruh stasiun berada di lokasi yang sama.
Prompt minggu 1:
Saya sedang mengembangkan project RainPredict, yaitu project Data Science untuk menganalisis dan memprediksi curah hujan berdasarkan data historis.
Bantu saya melakukan persiapan project dan eksplorasi awal dataset.
Tugas:
Periksa struktur dataset dan nama setiap kolom.
Jelaskan fungsi masing-masing kolom berdasarkan dokumentasi sumber data.
Identifikasi satuan curah hujan dan kode penanda missing value.
Identifikasi jumlah stasiun pengamatan.
Periksa rentang waktu dataset.
Berikan rekomendasi struktur folder project.
Buat dokumentasi awal dataset.
Batasan:
Jangan langsung melakukan data cleaning.
Jangan menghapus atau mengubah data.
Jangan mengarang arti kolom.
Jika informasi tidak tersedia, katakan bahwa informasi tersebut belum diketahui.
Berikan kode Python secara bertahap dan jelaskan fungsi setiap kode.
Saya akan memberikan hasil pemeriksaan dataset secara bertahap. Jangan melanjutkan ke tahap berikutnya sebelum tahap saat ini selesai.
Minggu 2 — Data Cleaning
Fokus: kualitas data
Workflow:
Menangani nilai penanda missing value seperti -9999.
Memeriksa kolom kualitas Q_RR;;.
Memeriksa duplikasi berdasarkan stasiun dan tanggal.
Memvalidasi format tanggal.
Mengonversi satuan curah hujan.
Memeriksa nilai ekstrem.
Membuat dataset hasil cleaning.
Batasan:
Jangan mengubah nilai curah hujan 0 menjadi missing value.
Jangan menghapus nilai ekstrem hanya karena nilainya tinggi.
Jangan mengisi missing value dengan rata-rata secara otomatis.
Jangan menghapus kode kualitas sebelum memahami artinya.
Simpan dataset mentah tanpa perubahan.
Semua proses cleaning harus bisa diulang.
Prompt minggu 2:
Lanjutkan project RainPredict ke tahap Data Cleaning.
Bantu saya membersihkan dataset curah hujan menggunakan Python dan Pandas.
Tahapan:
Identifikasi missing value berdasarkan kode resmi dataset.
Periksa data duplikat.
Validasi format tanggal.
Validasi satuan curah hujan.
Periksa kode kualitas pengamatan.
Identifikasi nilai ekstrem.
Buat dataset hasil cleaning.
Batasan:
Jangan menghapus data tanpa alasan yang jelas.
Pertahankan nilai curah hujan 0 jika valid.
Jangan melakukan imputasi sebelum menganalisis pola missing value.
Jangan mencampur data dari stasiun berbeda.
Jangan menimpa dataset mentah.
Jelaskan alasan setiap proses cleaning.
Berikan kode per tahap, bukan satu program besar. Setelah setiap tahap, berikan kode untuk memeriksa hasilnya. Tunggu hasil pemeriksaan saya sebelum melanjutkan.
Minggu 3 — Exploratory Data Analysis (EDA)
Fokus: memahami pola curah hujan
Workflow:
Menghitung mean, median, minimum, maksimum, dan standar deviasi.
Menganalisis distribusi curah hujan.
Menganalisis curah hujan berdasarkan bulan.
Menganalisis curah hujan berdasarkan tahun.
Mengidentifikasi periode curah hujan tinggi dan rendah.
Membuat visualisasi awal.
Batasan:
Jangan langsung membuat model prediksi.
Jangan menyimpulkan musim hujan hanya dari satu bulan.
Jangan menyimpulkan pengaruh El Niño tanpa data pendukung.
Jangan membuat kesimpulan hanya berdasarkan grafik.
Setiap visualisasi harus disertai interpretasi.
Prompt minggu 3:
Lanjutkan project RainPredict ke tahap Exploratory Data Analysis (EDA).
Bantu saya mengeksplorasi pola curah hujan berdasarkan dataset yang sudah dibersihkan.
Analisis yang perlu dilakukan:
Statistik deskriptif curah hujan.
Distribusi nilai curah hujan.
Pola curah hujan bulanan.
Pola curah hujan tahunan.
Perbandingan pola antarperiode.
Identifikasi kemungkinan pola musiman.
Buat visualisasi menggunakan Matplotlib atau Seaborn.
Batasan:
Jangan melakukan pemodelan.
Jangan mengarang hasil analisis.
Gunakan data aktual dari dataset.
Jangan menyimpulkan pengaruh El Niño tanpa data pendukung.
Jelaskan setiap grafik berdasarkan hasil yang benar-benar terlihat.
Jangan mengubah dataset hasil cleaning.
Berikan kode secara bertahap dan jelaskan tujuan setiap visualisasi.
Minggu 4 — Feature Engineering
Fokus: menyiapkan variabel analisis
Workflow:
Menentukan resolusi data yang digunakan.
Mengagregasi curah hujan harian menjadi bulanan jika sesuai tujuan.
Membuat fitur tahun dan bulan.
Menentukan indikator musim hujan berdasarkan definisi yang dapat dipertanggungjawabkan.
Memeriksa konsistensi data temporal.
Menyiapkan dataset untuk pemodelan.
Batasan:
Jangan membuat fitur tanpa alasan analitis.
Jangan mencampurkan data harian dan bulanan tanpa penjelasan.
Jangan menetapkan awal musim hujan secara asal.
Jangan menggunakan informasi masa depan sebagai fitur prediksi masa lalu (data leakage).
Jangan melakukan normalisasi sebelum kebutuhan model diketahui.
Prompt minggu 4:
Lanjutkan project RainPredict ke tahap Feature Engineering.
Bantu saya menyiapkan fitur yang relevan untuk analisis dan prediksi curah hujan.
Tugas:
Tentukan apakah data harian atau bulanan lebih sesuai dengan tujuan penelitian.
Buat fitur temporal yang diperlukan.
Lakukan agregasi data jika memang diperlukan.
Identifikasi indikator untuk menentukan periode musim hujan.
Periksa kelengkapan dan konsistensi data.
Siapkan dataset untuk pemodelan.
Batasan:
Jangan membuat indikator musim hujan tanpa dasar ilmiah.
Jangan menggunakan informasi masa depan dalam fitur.
Jangan menambahkan variabel eksternal tanpa sumber data yang jelas.
Jelaskan alasan setiap fitur dibuat.
Pertahankan dataset sebelumnya.
Jangan lanjut ke pemodelan sebelum fitur dan target prediksi sudah didefinisikan dengan jelas.
Minggu 5 — Pengembangan Model Prediksi
Fokus: Machine Learning / Time Series
Workflow:
Menentukan target prediksi.
Menentukan pendekatan pemodelan.
Membuat baseline model.
Membagi data training dan testing secara kronologis.
Melakukan pelatihan model.
Menghasilkan prediksi awal.
Menyimpan model dan hasil prediksi.
Batasan:
Jangan langsung menggunakan algoritma kompleks.
Jangan melakukan pembagian data secara acak untuk time series.
Jangan menggunakan data testing untuk melatih model.
Jangan memilih model hanya karena hasilnya terlihat bagus.
Jangan mengklaim model akurat sebelum dievaluasi.
Jangan mengklaim El Niño menyebabkan suatu pola hanya dari korelasi.
Prompt minggu 5:
Lanjutkan project RainPredict ke tahap pengembangan model prediksi.
Bantu saya membangun model berdasarkan dataset yang telah melalui cleaning, EDA, dan feature engineering.
Tugas:
Tentukan target prediksi secara jelas.
Rekomendasikan algoritma time series yang sesuai.
Buat baseline model sebagai pembanding.
Bagi data training dan testing berdasarkan urutan waktu.
Lakukan pelatihan model.
Hasilkan prediksi awal.
Jelaskan cara kerja algoritma yang digunakan.
Batasan:
Jangan menggunakan algoritma kompleks tanpa alasan.
Hindari data leakage.
Jangan melakukan random split untuk data time series.
Jangan mengubah data testing untuk meningkatkan hasil.
Jangan mengklaim model sudah akurat.
Berikan alasan pemilihan algoritma berdasarkan karakteristik dataset.
Jelaskan kode dan proses pemodelan secara bertahap. Tunggu persetujuan saya sebelum mencoba algoritma tambahan.
Minggu 6 — Evaluasi Model
Fokus: mengukur kinerja prediksi
Workflow:
Menghasilkan prediksi pada data testing.
Menghitung MAE.
Menghitung RMSE.
Menghitung metrik tambahan sesuai jenis target.
Membandingkan model dengan baseline.
Memeriksa kesalahan prediksi.
Menentukan model yang paling layak.
Batasan:
Jangan hanya menampilkan satu metrik.
Jangan membandingkan model dengan data testing berbeda.
Jangan menyembunyikan hasil evaluasi yang buruk.
Jangan menyebut model terbaik tanpa pembanding.
Jangan mengubah data testing setelah melihat hasil untuk mempercantik skor.
Prompt minggu 6:
Lanjutkan project RainPredict ke tahap evaluasi model.
Bantu saya mengevaluasi kinerja model prediksi yang telah dibuat.
Tugas:
Hitung MAE dan RMSE.
Tambahkan metrik lain jika sesuai dengan jenis target prediksi.
Bandingkan hasil model dengan baseline.
Buat visualisasi nilai aktual dan prediksi.
Analisis kesalahan prediksi.
Jelaskan kelebihan dan keterbatasan model.
Batasan:
Gunakan data testing yang sudah ditentukan.
Jangan mengubah data testing.
Jangan menyembunyikan hasil evaluasi.
Jangan menyimpulkan model baik hanya berdasarkan satu metrik.
Jangan membuat angka evaluasi fiktif.
Berikan interpretasi hasil dengan bahasa yang mudah dipahami dan sesuai data aktual.
Minggu 7 — Visualisasi dan Interpretasi
Fokus: menyampaikan hasil
Workflow:
Membuat grafik historis curah hujan.
Membuat grafik perbandingan aktual dan prediksi.
Menampilkan pola bulanan dan tahunan.
Menginterpretasikan hasil prediksi.
Menjelaskan kemungkinan periode musim hujan.
Menyusun kesimpulan berdasarkan hasil.
Batasan:
Jangan memanipulasi grafik untuk membuat hasil terlihat bagus.
Jangan menyatakan tanggal awal musim hujan secara pasti jika model hanya menghasilkan estimasi.
Jangan mengklaim prediksi sebagai informasi resmi BMKG.
Jangan membuat kesimpulan di luar cakupan data.
Pisahkan fakta, hasil prediksi, dan interpretasi.
Prompt minggu 7:
Lanjutkan project RainPredict ke tahap visualisasi dan interpretasi hasil.
Bantu saya menyajikan hasil analisis dan prediksi curah hujan.
Tugas:
Buat visualisasi curah hujan historis.
Buat grafik aktual dibandingkan prediksi.
Tampilkan pola musiman.
Interpretasikan hasil prediksi.
Jelaskan estimasi periode musim hujan jika target dan definisinya sudah tersedia.
Susun kesimpulan berdasarkan hasil analisis.
Batasan:
Jangan mengarang hasil prediksi.
Jangan membuat klaim bahwa hasil merupakan prediksi resmi BMKG.
Jangan menyatakan hubungan sebab-akibat El Niño tanpa bukti yang memadai.
Bedakan data aktual dan prediksi.
Jelaskan keterbatasan hasil.
Gunakan visualisasi yang informatif dan mudah dipahami.
Minggu 8 — Finalisasi dan GitHub
Fokus: menyelesaikan project
Workflow:
Merapikan seluruh kode.
Memisahkan proses berdasarkan tahapan.
Memeriksa apakah notebook bisa dijalankan ulang.
Membuat requirements.txt.
Menyusun README.md.
Memastikan dataset sensitif atau berlisensi tidak ikut diunggah.
Melakukan commit dan push ke GitHub.
Membuat dokumentasi akhir.
Batasan:
Jangan menghapus kode penting tanpa pemeriksaan.
Jangan mengunggah API key, token, atau password.
Jangan mengunggah dataset yang tidak boleh didistribusikan.
Jangan menyatakan project selesai jika notebook belum bisa dijalankan ulang.
Jangan menghapus riwayat eksperimen yang masih dibutuhkan untuk dokumentasi.
Prompt minggu 8:
Lanjutkan project RainPredict ke tahap finalisasi.
Bantu saya merapikan project agar siap dipublikasikan di GitHub dan dipresentasikan.
Tugas:
Periksa struktur folder project.
Periksa konsistensi kode.
Pastikan notebook dapat dijalankan ulang dari awal.
Buat requirements.txt berdasarkan library yang benar-benar digunakan.
Buat README.md.
Dokumentasikan sumber dataset, tahapan analisis, algoritma, dan hasil evaluasi.
Periksa file yang tidak boleh diunggah.
Siapkan checklist publikasi GitHub.
Batasan:
Jangan menghapus file tanpa persetujuan.
Jangan mengunggah kredensial atau dataset yang lisensinya tidak mengizinkan.
Jangan mengubah hasil penelitian.
Jangan menuliskan hasil yang belum dibuktikan.
Jangan menyatakan project selesai sebelum pemeriksaan akhir.
Berikan rekomendasi perbaikan jika ditemukan masalah.
4. Aturan dan batasan selama mengerjakan RainPredict
Ini bagian yang menurut saya paling penting. Kita perlu membedakan apa yang boleh dan tidak boleh dilakukan oleh AI maupun kamu sebagai pengembang project.
Aspek
Boleh dilakukan
Tidak boleh dilakukan
Dataset
Memeriksa, membersihkan, mengolah
Mengarang atau mengubah nilai tanpa alasan
Python
Meminta bantuan penulisan kode
Menyalin kode tanpa memahami fungsinya
Cleaning
Menghapus data berdasarkan kriteria valid
Menghapus data secara sembarangan
Analisis
Menggunakan statistik dan visualisasi
Membuat kesimpulan tanpa bukti
Pemodelan
Membandingkan algoritma
Memilih model berdasarkan skor yang direkayasa
Evaluasi
Menggunakan MAE, RMSE, dan metrik sesuai target
Mengubah data testing untuk memperbaiki skor
Referensi
Menggunakan dokumentasi dan jurnal
Menggunakan referensi fiktif
GitHub
Mengunggah kode dan dokumentasi
Mengunggah token, password, dan data terlarang

Aturan khusus penggunaan AI
Saya sarankan menerapkan lima aturan berikut:
AI sebagai asisten, bukan pengambil keputusan. AI boleh memberikan rekomendasi, tetapi keputusan metode tetap harus berdasarkan tujuan dan karakteristik data.
Satu tahap diselesaikan terlebih dahulu. Jangan meminta AI mengerjakan cleaning, EDA, dan pemodelan sekaligus.
Setiap kode harus dijelaskan. Kamu harus mengetahui fungsi kode, input, output, dan alasan penggunaannya.
Hasil harus berdasarkan data aktual. AI tidak boleh mengarang jumlah data, grafik, nilai evaluasi, atau hasil prediksi.
Jangan langsung menimpa kode sebelumnya. Simpan versi sebelumnya dan lakukan perubahan setelah memahami penyebab masalah.
5. Workflow kerja harian dan GitHub
Selain target mingguan, saya menyarankan kamu menggunakan pola kerja berikut.
Aktivitas
Durasi perkiraan
Memahami materi atau metode
20 menit
Mengerjakan kode
45–60 menit
Menguji hasil kode
20 menit
Mencatat hasil dan kendala
10 menit
Commit ke GitHub
5 menit

Tidak harus dikerjakan setiap hari. Yang penting, setiap sesi menghasilkan kemajuan yang bisa diperiksa.
Aturan GitHub setiap minggu:
Setiap kali satu tahapan selesai, lakukan commit dengan pesan yang jelas.
Minggu
Contoh commit
1
Initial project setup
2
Complete data cleaning
3
Add exploratory data analysis
4
Add feature engineering
5
Implement rainfall prediction model
6
Add model evaluation
7
Add prediction visualizations
8
Finalize project documentation

6. Sistem evaluasi sebelum berpindah minggu
Saya ingin kamu menerapkan sistem checkpoint. Artinya, setiap minggu harus memenuhi kriteria tertentu sebelum lanjut ke tahap berikutnya.
Checklist progres RainPredict
Minggu 1
Minggu 1
0/4 selesai
Struktur folder sudah benar
Sumber dan dokumentasi dataset diketahui
Kolom dan satuan dipahami
Identitas stasiun sudah diperiksa
Checklist dapat kamu tandai selama sesi ini.
Reset minggu ini
7. Kondisi project kamu saat ini
Berdasarkan pengerjaan kita sejauh ini:
Posisi pengerjaan
Minggu 1–2
Fondasi dan pemeriksaan awal dataset
Membaca dataset cuaca.csv
Selesai
Mengidentifikasi 4 kolom
Selesai
Mengidentifikasi 3 SOUID
Selesai
Konversi nilai curah hujan
Sudah dilakukan
Konversi tanggal
Sudah dilakukan
Memeriksa kode kualitas
Belum diverifikasi
Memastikan stasiun yang digunakan
Belum selesai
EDA dan visualisasi
Belum
Pemodelan
Belum
Ada satu hal yang perlu kita jaga: pastikan sumber asli cuaca.csv dan dokumentasinya sudah diketahui. Jangan menganggap konversi RR menjadi RR_mm dengan pembagian 10 sudah benar sebelum satuan pada dokumentasi sumber dikonfirmasi. Begitu juga kode kualitas Q_RR;; harus diperiksa sebelum data dinyatakan valid.
8. Aturan utama kita selama project
Mulai sekarang, saya menyarankan pola kolaborasi seperti ini:
Kamu mengerjakan satu tahapan.
Kamu mengirimkan kode dan hasil output.
Saya membantu memeriksa apakah prosesnya benar.
Jika terdapat error, kita memperbaiki penyebabnya, bukan sekadar menghilangkan error.
Setelah berhasil, kita mendokumentasikan hasilnya.
Baru kemudian kita berpindah ke tahapan berikutnya.
