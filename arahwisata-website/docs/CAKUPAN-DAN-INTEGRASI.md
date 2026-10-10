# Cakupan dan integrasi

## Berfungsi di paket ini

- 10 halaman utama dan halaman 404, responsif.
- Logo, dokumentasi kawasan, produk KEPOTA, serta ilustrasi produk pengembangan.
- Tiga itinerary lengkap dan aturan harga kelompok.
- Permintaan pelanggan melalui email, unduhan ringkasan, salin rincian.
- Kanal kemitraan melalui email.
- Penjelajah bentang ilustratif dengan mode 3D/datar dan lima titik interaktif.
- Pencarian dan filter 37 taksa, galeri modal dengan keyboard Escape.
- Paspor lokal, hapus, ekspor CSV.
- Monitoring lokal, empat jenis catatan, status, hapus, JSON/CSV, impor JSON tervalidasi.
- Pencegahan injeksi HTML pada input yang ditampilkan dan formula CSV.
- Situs dapat dibuka langsung; font memiliki fallback lokal.

## Belum terhubung

- Akun pelanggan, mitra, dan administrator dengan autentikasi serta izin peran.
- Database pusat, sinkronisasi lintas perangkat, reservasi kuota secara atomik.
- Payment gateway, webhook, rekonsiliasi pembayaran, invoice fiskal, dan refund otomatis.
- Stok bersama yang otomatis berkurang saat pembelian.
- Email/WhatsApp otomatis, pengingat tujuh hari, pelaporan terjadwal.
- Tinjauan catatan pemandu/administrator dan persetujuan katalog.
- QR ketertelusuran per batch: data produsen, komposisi, nomor produksi, masa simpan nyata belum tersedia. Tidak dibuat ID batch palsu.

## Jika sistem transaksi penuh akan diaktifkan

Pertahankan tampilan ini dan hubungkan ke backend dengan penyimpanan persisten serta autentikasi peran. Tabel minimum: users, partner_profiles, programs, departure_slots, bookings, booking_participants (data minimum), products, production_batches, inventory_movements, orders, order_items, payments, partner_payouts, observations, observation_reviews, impact_records, consent_records, audit_logs.

Gunakan otorisasi di server untuk semua operasi mitra/admin. Lokasi satwa sensitif tidak masuk endpoint publik. Pemesanan dan perubahan stok harus atomik, pembayaran diverifikasi melalui webhook bertanda tangan, dan transaksi idempoten. Endpoint email harus memakai pembatasan laju, validasi, dan perlindungan spam. Kunci layanan ditempatkan di environment server; jangan taruh rahasia di config.js.

Pengaktifan memerlukan pilihan hosting backend, akun penyedia pembayaran, kredensial, kontak operasional, dan kebijakan bisnis yang disetujui pemilik. Paket ini tidak berpura-pura bahwa integrasi tersebut sudah aktif.
