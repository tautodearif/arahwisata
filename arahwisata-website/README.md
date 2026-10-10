# ArahWisata — Website lengkap

Website ekowisata dan kemitraan masyarakat, dengan dokumentasi asli Leuweung Bobojong, logo ArahWisata, dan KEPOTA. Bahasa utama: Indonesia.

## Membuka website

1. Ekstrak ZIP ini.
2. Buka `dist/index.html` di browser. Navigasi, kalkulator, galeri, penjelajah, dan formulir email dapat berjalan tanpa instalasi.
3. Untuk pengujian melalui HTTP, dari folder ini jalankan `python3 -m http.server 8080 --directory dist`, lalu buka `http://localhost:8080`.
4. Untuk hosting statis, unggah **seluruh isi folder dist/** ke document root. `index.html` harus berada pada tingkat teratas, diikuti CSS, JavaScript, dan folder `assets/`.

Tidak memerlukan Node, npm, framework, atau proses build untuk membuka dan mengunggah versi website yang disertakan. Python hanya diperlukan jika ingin membangun ulang halaman dari generator.

## Isi direktori

- `dist/`: seluruh website yang diunggah ke hosting.
- `dist/index.html`: beranda.
- `dist/program.html`: tiga pengalaman, itinerary, biaya, ketentuan kelompok, FAQ.
- `dist/kawasan.html`: kawasan, ilustrasi bentang 3D/datar, inventaris yang bisa dicari, galeri dokumentasi.
- `dist/produk.html`: KEPOTA, jumlah pesanan, cerita asal, portofolio produk pengembangan.
- `dist/mitra.html`: layanan pengelola/CSR/produsen/agen/ritel, ruang lingkup enam bulan, formulir minat.
- `dist/rencanakan.html`: permintaan wisata/produk, perhitungan kelompok, uang muka, ekspor teks, email.
- `dist/monitoring.html`: transaksi, stok, kapasitas, dampak, status tindak lanjut, ekspor/impor lokal.
- `dist/paspor.html`: pengamatan pribadi berbasis penglihatan, suara, jejak, atau habitat.
- `dist/tentang.html`: cerita, tim, prinsip, sumber.
- `dist/ketentuan.html`: syarat permintaan, etika, privasi, penyimpanan.
- `dist/404.html`: navigasi kembali ketika halaman tidak ditemukan.
- `dist/config.js`: kontak dan konfigurasi merek.
- `dist/data.js`: nama program, tarif, kapasitas, itinerary, dan bentang alam.
- `dist/taxa.js`: 37 taksa yang digunakan halaman kawasan dan paspor.
- `dist/core.js`: perhitungan, sanitasi, format CSV, validasi data impor.
- `dist/app.js`: interaksi website.
- `dist/styles.css`: identitas visual dan layout responsif.
- `dist/assets/`: aset lokal, termasuk foto yang sudah disiapkan untuk web.
- `build.py`: generator HTML untuk pengembangan berikutnya.
- `taxa.json`: sumber inventaris untuk generator.
- `asset-sources.json` dan `docs/SUMBER-ASET.md`: asal dokumentasi.
- `docs/PANDUAN-PENGELOLA.md`: pengelolaan konten dan penggunaan fitur.
- `docs/CAKUPAN-DAN-INTEGRASI.md`: kemampuan yang tersedia dan integrasi yang belum aktif.
- `checks/verify.py`, `checks/core.test.cjs`: pemeriksaan tautan/aset dan perhitungan.

## Status operasional

Website dapat dipublikasikan sebagai katalog, pengenalan program, dan kanal permintaan melalui email. Formulir membuka email terisi; pengunjung tetap harus mengirim email sendiri. Jadwal, persediaan, rincian layanan, harga akhir, dan pembayaran dikonfirmasi tim. Tidak ada notifikasi palsu “pesanan berhasil”.

Monitoring Deck dan paspor menyimpan data di browser perangkat pengguna. Bukan portal multiakun atau database bersama. Tersedia ekspor; tidak ada sinkronisasi, persetujuan administrator, pembayaran otomatis, atau pengingat otomatis. Lihat dokumen cakupan sebelum mengoperasikan layanan bersama.

## Mengubah konten

- Ubah kontak di `dist/config.js` dan konten kontak statis pada `build.py`, lalu jalankan `python3 build.py`.
- Program dan itinerary: `dist/data.js`.
- Warna, tipografi, dan responsive breakpoints: `dist/styles.css`.
- Konten halaman: `build.py`, lalu jalankan `python3 build.py`.
- Inventaris: `taxa.json`, lalu jalankan `python3 build.py`.
- Foto: `dist/assets/`; pertahankan nama berkas atau perbarui referensinya.
- Harga produk berada pada halaman di `build.py` dan kalkulator di `dist/app.js`. Perbarui keduanya bersamaan.

Versi publik tidak menampilkan proyeksi usaha sebagai hasil aktual. Sabun pohpohan dan minuman daun pinus ditandai sebagai pengembangan. Tidak ada klaim bahwa produk pengembangan telah dipasarkan atau memperoleh izin.

## Pemeriksaan

Jalankan dari folder proyek:

```sh
python3 build.py
node checks/core.test.cjs
python3 checks/verify.py
node --check dist/app.js
```

Browser QA tidak dijalankan pada lingkungan pembuatan karena kontrol browser untuk Sites tidak tersedia. Periksa tampilan pada perangkat sasaran dan aplikasi email sebelum distribusi publik. Layout menyediakan breakpoint 600, 850, dan 1100 px; interaksi mengikuti preferensi pengurangan gerak.
