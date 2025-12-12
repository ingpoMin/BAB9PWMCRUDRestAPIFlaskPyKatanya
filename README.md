## Cara Instalasi dan Menjalankan

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di lokal komputer Anda:

### 1. Clone Repositori
```bash
git clone https://github.com/ingpoMin/BAB9PWMCRUDRestAPIFlaskPyKatanya.git
cd BAB9PWMCRUDRestAPIFlaskPyKatanya

```
atau anda bisa mendownload zip-nya dan ekstrak secara manual

### 2. Buat Virtual Environment
Disarankan menggunakan virtual environment agar *package* tidak bercampur.

**Untuk Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Untuk Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*Jika file `requirements.txt` belum ada, pastikan Anda menginstall: `flask`, `flask-sqlalchemy`, `mysqlclient` (atau driver mysql lainnya).*

### 4. Konfigurasi Database
1. Buat database baru di MySQL (misal: `db_toko`).
2. Sesuaikan file `config.py` (atau bagian config di `__init__.py`) dengan database Anda.

### 5. Jalankan Aplikasi
```bash
flask run
```
Aplikasi akan berjalan di `http://localhost:5000`.



## Daftar Endpoint API

| Method | Endpoint | Deskripsi | Parameter (JSON) |
| :--- | :--- | :--- | :--- |
| **GET** | `/` | Cek server berjalan | - |
| **GET** | `/users` | Ambil semua data user | - |
| **GET** | `/users/<id>` | Ambil detail satu user | - |
| **POST** | `/users` | Tambah user baru | `{"name": "...", "email": "...", "password": "..."}` |
| **PUT** | `/users/<id>` | Update data user | `{"name": "...", "email": "...", "password": "..."}` |
| **DELETE** | `/users/<id>` | Hapus user | - |
