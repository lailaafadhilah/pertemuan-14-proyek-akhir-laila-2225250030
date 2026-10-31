# Proyek Akhir Algoritma dan Pemrograman

## Identitas Proyek

| Keterangan | Identitas |
|---|---|
| Nama | Laila Fadhilah |
| NIM | 2225250030 |
| Kelas | 3A |
| Program Studi | S1 Pendidikan Matematika |
| Mata Kuliah | Algoritma dan Pemrograman |
| Pertemuan | 14 |
| Jenis Proyek | Individu |

## Deskripsi Proyek

Program Rekap dan Analisis Nilai Matematika Kelas merupakan program sederhana yang dirancang untuk membantu proses pengolahan data nilai siswa. Program ini dapat membaca data nilai dari file, melakukan validasi nilai, menghitung statistik nilai, menentukan status kelulusan berdasarkan Kriteria Ketuntasan Minimal (KKM), serta menyimpan hasil analisis ke dalam file laporan.

## Tujuan Proyek

1. Membuat program untuk membaca data nilai dari file.
2. Melakukan validasi terhadap nilai siswa.
3. Menghitung rata-rata, nilai minimum, dan nilai maksimum.
4. Menentukan jumlah siswa yang lulus dan tidak lulus berdasarkan KKM.
5. Menyimpan hasil analisis ke dalam file laporan.

## Fitur Program

- Membaca data nilai dari file teks.
- Memvalidasi nilai agar berada pada rentang 0 sampai 100.
- Menghitung rata-rata nilai.
- Menentukan nilai minimum dan maksimum.
- Menghitung jumlah siswa yang lulus dan tidak lulus.
- Menyimpan hasil analisis ke dalam file teks.

## Struktur Folder

```text
pertemuan-14-proyek-akhir-ziana-2225250076/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    └── .gitkeep
```

## Kebutuhan Program

- Python
- Visual Studio Code
- Git
- GitHub

## Cara Menjalankan Program

1. Pastikan Python sudah terpasang pada komputer.
2. Buka folder proyek melalui Visual Studio Code.
3. Buka terminal pada folder proyek.
4. Jalankan program dengan perintah berikut:

```bash
python src/main.py
```

Jika perintah `python` tidak berfungsi, gunakan:

```bash
py src/main.py
```

## Pengujian Program

Pengujian dilakukan menggunakan beberapa skenario untuk memastikan program berjalan sesuai dengan kebutuhan.

| ID | Skenario Pengujian | Hasil yang Diharapkan |
|---|---|---|
| TC01 | Data nilai normal | Program menghitung rata-rata dengan benar |
| TC02 | Nilai batas bawah (0) | Nilai diterima |
| TC03 | Nilai batas atas (100) | Nilai diterima |
| TC04 | Nilai di luar rentang (105) | Nilai ditolak dan muncul pesan validasi |
| TC05 | File data tidak ditemukan | Program menampilkan pesan kesalahan |
| TC06 | Seluruh nilai memenuhi KKM | Jumlah siswa lulus sama dengan jumlah data |

## Status Proyek

Proyek berada pada tahap perancangan, meliputi penyusunan proposal, struktur program, pseudocode, dan test case. Tahap implementasi, pengujian, serta debugging akan dilanjutkan sesuai jadwal pengerjaan proyek.

## Repository GitHub

Nama repository: pertemuan-14-proyek-akhir-laila-2225250030

Tautan repository: https://github.com/lailaafadhilah/pertemuan-14-proyek-akhir-laila-2225250030.git
