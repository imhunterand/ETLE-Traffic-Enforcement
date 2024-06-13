
# Electronic Traffic Law Enforcement (ETLE)
Sistem Penegakan Hukum Lalu Lintas Elektronik Berbasis Deteksi Kendaraan dan Pelanggaran Menggunakan Pembelajaran Mesin dan Komputer Visi

## Judul Proposal
Sistem Penegakan Hukum Lalu Lintas Elektronik (ETLE): Deteksi Kendaraan dan Pelanggaran Berbasis Pembelajaran Mesin dan Komputer Visi
"Implementasi Sistem Penegakan Hukum dan Tata Tertib Lalu Lintas Berbasis Elektronik (Electronic Traffic Law Enforcement - ETLE) dengan Teknologi Pengolahan Citra dan Pembelajaran Mesin untuk Meningkatkan Keamanan Jalan Raya dan Efektivitas Penegakan Hukum di Kota Metropolitan"

## Deskripsi Project
ETLE adalah sistem penegakan hukum dan tata tertib lalu lintas secara digital yang menggunakan teknologi deteksi kendaraan dan pelanggaran berbasis komputer visi dan pembelajaran mesin. Sistem ini dapat mendeteksi berbagai jenis pelanggaran lalu lintas seperti melanggar batas kecepatan, melanggar lampu merah, dan jenis kendaraan yang melanggar aturan.


### Struktur Direktori Proyek
```
ETLE_Project/
│
├── app/
│ ├── init.py
│ ├── config.py
│ ├── database.py
│ ├── camera_manager.py
│ ├── report_generator.py
│ ├── user_manager.py
│ ├── capture_video.py
│ ├── detect_vehicles.py
│ ├── detect_violations.py
│ ├── detect_vehicle_type.py
│ ├── speed_analysis.py
│ ├── email_notification.py
│ ├── model_training.py
│ ├── data_preprocessing.py
│ ├── routes.py
│ ├── models.py
│ ├── utils/
│ │ ├── init.py
│ │ ├── image_utils.py
│ │ ├── video_utils.py
│ │ ├── pdf_utils.py
│ ├── api/
│ │ ├── init.py
│ │ ├── views.py
│ │ ├── urls.py
│
├── tests/
│ ├── test_capture_video.py
│ ├── test_detect_vehicles.py
│ ├── test_detect_violations.py
│ ├── test_database.py
│ ├── test_email_notification.py
│ ├── test_user_manager.py
│ ├── test_camera_manager.py
│ ├── test_report_generator.py
│ ├── test_api.py
│
├── requirements.txt
├── run.py
└── README.md
```

### Deskripsi File dan Fitur Tambahan
- **app/routes.py**: Mengatur rute aplikasi web.
- **app/models.py**: Definisi model database untuk pelanggaran dan pengguna.
- **app/database.py**: Manajemen basis data.
- **app/camera_manager.py**: Manajemen kamera untuk pemantauan lalu lintas.
- **app/report_generator.py**: Pembuatan laporan pelanggaran dalam format PDF.
- **app/user_manager.py**: Manajemen pengguna aplikasi.
- **app/capture_video.py**: Menangkap video dari sumber daya kamera.
- **app/detect_vehicles.py**: Deteksi kendaraan dalam video rekaman.
- **app/detect_violations.py**: Deteksi pelanggaran lalu lintas dalam video.
- **app/detect_vehicle_type.py**: Mengklasifikasikan jenis kendaraan dalam rekaman video.
- **app/speed_analysis.py**: Analisis kecepatan kendaraan dari rekaman video.
- **app/email_notification.py**: Mengirim notifikasi email untuk pelanggaran yang terdeteksi.
- **app/model_training.py**: Melatih model pembelajaran mesin untuk deteksi pelanggaran.
- **app/data_preprocessing.py**: Pra-pemrosesan data gambar untuk pelatihan model.
- **app/config.py**: Konfigurasi aplikasi termasuk pengaturan database dan email.
- **app/utils/**: Utilitas tambahan untuk pemrosesan gambar, video, dan PDF.
- **app/api/**: API untuk mendapatkan data pelanggaran.

### Dokumentasi Proyek
Proyek ini menggabungkan teknologi deteksi komputer visi dan pembelajaran mesin untuk meningkatkan efisiensi penegakan hukum lalu lintas. Dengan fitur-fitur seperti deteksi kendaraan, deteksi pelanggaran, analisis kecepatan, dan pembuatan laporan otomatis, ETLE memungkinkan penerapan aturan lalu lintas secara lebih efektif dan akurat.

### Tata Cara Penggunaan
1. **Persiapan Lingkungan**
   - Install dependensi dengan menjalankan `pip install -r requirements.txt`.
   - Sesuaikan konfigurasi di `app/config.py`.
   - Buat basis data dengan menjalankan `python -m app.database`.

2. **Menjalankan Aplikasi**
   - Mulai server dengan `python run.py`.

3. **Interaksi dengan Aplikasi**
   - Tambahkan kamera menggunakan endpoint `/add_camera`.
   - Hapus kamera menggunakan endpoint `/remove_camera`.
   - Lihat pelanggaran dengan mengakses `/violations`.

4. **Menangkap Video dan Analisis**
   - Gunakan `python -m app.capture_video` untuk menangkap video dari kamera.
   - Deteksi kendaraan dengan `python -m app.detect_vehicles`.
   - Deteksi pelanggaran dengan `python -m app.detect_violations`.
   - Analisis kecepatan dengan `python -m app.speed_analysis`.

5. **Penggunaan Lainnya**
   - Kirim notifikasi email dengan `python -m app.email_notification`.
   - Latih model dengan `python -m app.model_training`.
   - Pra-pemrosesan data dengan `python -m app.data_preprocessing`.

Pastikan untuk menyesuaikan bagian-bagian spesifik seperti konfigurasi email dan jalur data sesuai dengan kebutuhan proyek Anda.
