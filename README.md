Nama: Nisriina Wakhdah Haris
NPM: 2406360445
Kelas: PBP - B
link menuju app PWS: https://nisriina-wakhdah-footballshop.pbp.cs.ui.ac.id/

1. Cara saya mengimplementasikan daftar checklist yang harus dikerjakan adalah, sebagai berikut:
- Hal pertama yang saya lakukan adalah membaca tutorial 0 dan 1 agar saya benar-benar paham fungsi setiap langkah yang harus dilakukan
- Selain membaca tutorial, saya juga menonton video di youtube yang berkaitan dengan cara membuat proyek pada Django untuk pemula, saya menonton channel youtube bernama Kelas Terbuka
- Setelah saya paham langkah-langkahnya, saya mulai menyiapkan virtual enviroment dan membuat file requirements.txt yang berisi dependecies berkaitan dengan proyek yg akan dibuat lalu menginstall seluruh dependecies yang dibutuhkan
- Membuat proyek Django, repositori untuk menyimpan proyek tsb di git, dan file .env.prod yang berisi krendesial database dan mengisi file .env dg PRODUCTION=False 
- Membuat project baru pada web PWS dan mengganti remote URL pws dengan link project yang baru, menggunakan perintah git remote set-url pws <link>
- Menambahkan domain pada ALLOWED_HOSTS yang ada di file settings.py
- Melakukan add, commit, dan push ke repostiori yang sudah dibuat di git dan melakukan push ke pws master
- Setelah membuat proyek Django, saya membuat aplikasi bernama main lalu membuat model untuk aplikasi pada file models.py
- Pada file views.py, saya membuat fungsi show_main untuk menampilkan output yang berisi nama aplikasi, nama, dan npm saya. Fungsi tersebut saya hubungkan dengan file template bernama main.html yang sudah saya buat pada folder templates
- Membuat model dan fitur-fiturnya pada file models.py
- Menjalankan perintah python manage.py makemigration dan python manage.py migrate untuk menyimpan perubahan model pada database
- Membuat file urls.py pada folder main lalu menambahkan URLPattern untuk melakukan routing URL aplikasi main, di sini saya menambahkan url untuk memanggil fungsi show_main yang sudah dibuat pada file views.py (level aplikasi)
- Menambahkan rute URL untuk  mengarahkan path URL '' ke rute yang sudah dibuat pada file urls.py yang ada di folder main. Hal ini dilakukan pada file urls.py yg ada di dalam folder football_shop untuk mengatur rute URL pada level proyek
- Melakukan push ke repositori git untuk menyimpan perubahan2 tsb dan push ke pws master
2. Berikut ini adalah bagan request client ke aplikasi web berbabasis Django
![alt text]
sumber gambar: https://www.biznetgio.com/news/django

3. Peran settings.py adalah:
- Untuk mengonfigurasi proyek Django secara keseluruhan
- Mengelola daftar aplikasi yang teritegrasi dalam proyek, hal ini dapat dilakukan pada INSTALLED_APPS. Dalam kasus tugas individu ini, kita membuat app bernama main. Setelah membuat app tsb, kita perlu menambahkan aplikasi bernama 'main' ke dalam daftar aplikasi yang ada (INSTALLED_APPS) agar dapat terhubung dengan proyek Django
- Mengelola pengaturan terkait bahasa dan zona waktu (LANGUAGE_CODE dan TIME_ZONE)
- Mengatur daftar domain yang diizinkan untuk mengakses website melalui ALLOWED_HOSTS
- Menentukan database yang dipakai melalui DATABASES
4.  Cara kerja migrasi database di Django adalah dengan menjalankan perintah makemigration dan migrate, di mana perintah makemigartion berfungsi untuk membuat file migrasi yang berisi perubah pada model, sedangkan perintah migrate berfungsi untuk mengaplikasikan perubahan pada model yang sudah ada pada file migrasi tsb ke dalam database. Berikut ini adalah urutan pengerjaannya:
- Buka file models.py pada direktori aplikasi yang kita buat
- Membuat atau mengubah model dari proyek yang berada pada aplikasi
- Setelah mengisi file models.py jalankan perintah python manage.py makemigrations untuk membuat file migrasi yang merekam perubahan
- Untuk mengaplikasikan perubahan model ke dalam database lokal, jalankan perintah python manage.py migrate
5. Django dijadikan sebagai permulaan pembelajaran karena:
- Django memiliki konsep yang terstruktur karena menerapkan pola arsitektur MTV. Hal ini dikarenakan Django memisahkan logika bisnis (model), logika presentasi (template), dan view.
- Django menggunakan bahasa python yang syntaxnya relatif mudah dimengerti dan tidak terlalu panjang  dibanding bahasa yang lain (misalnya Java, C, dll) sehingga cocok untuk pemula
- Django memiliki fitur bawaan yang lengkap sehingga pemula tidak perlu meng-install library tambahan dan tidak perlu membuat dari nol
- Hasilnya bisa cepat dilihat melalui broweser
- Django merupakan salah satu framework yang open source dan banyak digunakan. Oleh karena itu, terdapat banyak sumber belajar yang dapat diakses jika kita mengalami kesulitan
6.  Feedback untuk kakak asdos di Tutorial 1 adalah: terima kasih sudah fast respon saat saya bertanya di forum diskusi discord, sudah stand-by dan hadir untuk membantu kami saat mengalami kendala, dan terima kasih juga karena telah membuatkan langkah-langkah tutorial yang jelas dan mudah dimengerti sehingga saya dapat mengikutinya dengan baikk