from data_io import baca_data
from analisis import hitung_statistik
from utilitas import tampilkan_hasil, simpan_laporan


def main():
    path_data = "data/nilai_contoh.txt"
    path_output = "output/laporan_nilai.txt"

    data = baca_data(path_data)

    if not data:
        print("Tidak ada data nilai yang dapat diproses.")
        return

    statistik = hitung_statistik(data)

    tampilkan_hasil(statistik)
    simpan_laporan(statistik, path_output)


if __name__ == "__main__":
    main()