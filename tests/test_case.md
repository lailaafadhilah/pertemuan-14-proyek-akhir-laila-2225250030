## Test Case

## Program Rekap dan Analisis Nilai Matematika Kelas

| ID | Kategori | Input/Kondisi | Expected Result | Status |
|---|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata nilai adalah 80 | Berhasil |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid | Berhasil |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid | Berhasil |
| TC04 | Invalid | Nilai 105 | Ditolak dengan pesan validasi | Berhasil |
| TC05 | Invalid | File tidak ditemukan | `FileNotFoundError` ditangani dengan pesan kesalahan | Berhasil |
| TC06 | Normal | Semua nilai lebih besar atau sama dengan KKM | Jumlah siswa tuntas sama dengan jumlah data nilai | Berhasil |

## Definition of Done

- [ ] Semua fitur wajib berjalan dengan baik.
- [ ] Semua test case wajib lulus.
- [ ] Program tidak berhenti karena error yang sudah diprediksi.
- [ ] Output program mudah dibaca dan dipahami.
- [ ] README menjelaskan cara menjalankan program.
- [ ] Commit proyek menunjukkan kontribusi setiap anggota tim.