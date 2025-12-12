## Daftar Endpoint API

| Method | Endpoint | Deskripsi | Body (JSON) |
| :--- | :--- | :--- | :--- |
| **GET** | `/` | Cek server berjalan | - |
| **GET** | `/users` | Ambil semua data user | - |
| **GET** | `/users/<id>` | Ambil detail satu user | - |
| **POST** | `/users` | Tambah user baru | `{"name": "...", "email": "...", "password": "..."}` |
| **PUT** | `/users/<id>` | Update data user | `{"name": "...", "email": "...", "password": "..."}` |
| **DELETE** | `/users/<id>` | Hapus user | - |
