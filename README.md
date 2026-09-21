# Module Integration Odoo 16 - Google Sheets API, Query Deluxe & Embed External Dashboard

Repository ini berisi kode sumber untuk modul kustom Odoo 16 yang dirancang untuk mengintegrasikan data dari Odoo langsung ke Google Sheets secara otomatis menggunakan Google Sheets API (`gspread`), memanfaatkan eksekusi kueri terintegrasi melalui modul **Query Deluxe**, serta menampilkan **External Dashboard** (seperti Looker Studio, Metabase, atau Grafana) secara terembed langsung di dalam antarmuka Odoo.

---

## 📌 Deskripsi Proyek

Proyek ini dikembangkan untuk mempermudah ekstraksi data operasional Odoo menggunakan kueri PostgreSQL, melakukan sinkronisasi/pembaruan data ke lembar kerja Google Sheets secara efisien, dan menyediakan visualisasi *Business Intelligence* melalui penayangan dasbor eksternal langsung dari antarmuka ERP Odoo.

---

## 🚀 Fitur Utama

- **Integrasi Google Sheets API:** Pengiriman dan pembaruan data otomatis ke Google Sheets.
- **Dukungan Query Deluxe:** Eksekusi kueri kustom berbasis database Odoo untuk fleksibilitas ekstraksi data.
- **Embedded External Dashboard:** Penayangan dasbor analitik eksternal (misalnya Looker Studio, Google Sheets View, atau platform BI lain) langsung pada menu tampilan Odoo via IFrame/client action.
- **Fungsi Pembaruan Data:** Menggunakan pustaka `gspread` untuk menangani eksekusi pembaruan data Odoo ke spreadsheet.
- **Konfigurasi Akses & Navigasi:** Pengaturan kredensial Service Account Google Cloud Platform (GCP) serta navigasi menu terpusat untuk fungsi operasional dan administratif.

---

## 🛠️ Prasyarat & Modul Dependensi

### 1. Sistem & Modul Odoo
- **Odoo ERP:** Versi 16.0
- **Modul Dependensi:** [Query Deluxe versi 16.0](https://apps.odoo.com/apps/modules/16.0/query_deluxe)

### 2. Python Environment
- **Python:** 3.8+ (Standar Odoo 16)
- **Pustaka Python Terikat (Versi Khusus):**
  - `google-auth==1.35.0`
  - `gspread==5.7.2`

---

## 💻 Instalasi Dependensi Python

Sebelum menginstal modul pada Odoo 16, pastikan pustaka Python terpasang sesuai versi spesifik berikut pada virtual environment Odoo Anda:

```bash
pip install google-auth==1.35.0 gspread==5.7.2
```

---

## 📂 Struktur Repositori

```text
└── addons/
    └── odoo16-custom-addons/
        ├── add_external_dashboard/
        └── query_deluxe_inherit/
            ├── models/             # Logika bisnis dan fungsi eksekusi kueri / update_google_sheet
            ├── views/              # Tampilan XML (Form, Tree, Menu Konfigurasi, & Embedded Dashboard)
            ├── security/           # File IR Model Access & Hak Akses Pengguna
            ├── data/               # Data awal / Konfigurasi bawaan
            ├── static/             # Aset statis (CSS, JS, Web View untuk embedded dashboard)
            ├── __manifest__.py     # Manifest modul Odoo (Dependensi: query_deluxe)
            └── __init__.py         # Inisialisasi package Python
```

---

## ⚙️ Cara Instalasi & Konfigurasi

1. **Unduh Modul Dependensi**
   - Unduh dan pasang modul **Query Deluxe** untuk Odoo 16 dari [Odoo Apps Store](https://apps.odoo.com/apps/modules/16.0/query_deluxe).
   - Pastikan modul `query_deluxe` berada di folder `addons` Odoo Anda.

2. **Clone Repositori Ini**
   Pindahkan folder modul integrasi ini ke direktori `addons`:
   ```bash
   cd /path/to/odoo/addons
   git clone https://github.com/sholah15/odoo16_custom_addons.git
   ```

3. **Perbarui Daftar Modul & Instal**
   - Aktifkan **Developer Mode** di Odoo 16.
   - Buka menu **Apps** > Klik **Update Apps List**.
   - Cari modul Looker Studio dan PostgreSQL Query Deluxe - Googlesheets dan klik **Install** (modul `query_deluxe` akan otomatis terdeteksi sebagai dependensi).

4. **Konfigurasi Kredensial GCP**
   - Masuk ke menu Konfigurasi Modul Query Deluxe di Odoo.
   - Copy-paste isi dari Service Account JSON dari Google Cloud Console.
   - Bagikan (*share*) berkas Google Sheets target ke alamat email Service Account GCP Anda.
   - Masukkan URL Semat (*Embed URL*) dari dasbor eksternal Anda pada menu Konfigurasi Dasbor di Modul Looker Studio Odoo.

---

## 📊 Penggunaan Embedded Dashboard

1. Masukkan URL Semat (*Embed URL*) dari dasbor eksternal Anda dan centang aktif pada menu Konfigurasi Dasbor di Modul Looker Studio Odoo.
2. Buka menu **Dashboard** pada di Modul Looker Studio Odoo.
3. Sistem akan memuat visualisasi dasbor interaktif secara langsung tanpa perlu meninggalkan antarmuka Odoo.

---

## 🔗 Referensi

- [Query Deluxe - Odoo App Store (v16.0)](https://apps.odoo.com/apps/modules/16.0/query_deluxe)
- [Dokumentasi gspread Python](https://docs.gspread.org/)

---
