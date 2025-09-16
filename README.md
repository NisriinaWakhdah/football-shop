Nama: Nisriina Wakhdah Haris
NPM: 2406360445
Kelas: PBP - B
link menuju app PWS: https://nisriina-wakhdah-footballshop.pbp.cs.ui.ac.id/

1. Cara saya mengimplementasikan daftar checklist yang harus dikerjakan adalah, sebagai berikut:
    - Hal pertama yang saya lakukan adalah membaca tutorial 0 dan 1 agar saya benar-benar paham fungsi setiap langkah yang harus dilakukan
    - Selain membaca tutorial, saya juga menonton video di youtube yang berkaitan dengan cara membuat proyek pada Django untuk pemula
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
![alt text](https://github.com/NisriinaWakhdah/football-shop/blob/master/django_77d5263d13.webp?raw=true)
sumber gambar: https://www.biznetgio.com/news/django

    Penjelasan:
    - Client mengirimkan request ke server melalui browser, misalnya dengan mengakses sebuah URL
    - Setelah server mendapatkan url dr client, Django akan mecocokan request dengan pola URL (URL Configuration) yang sudah didefiniskan di dalam urls.py pada level proyek
    - Jika pola tersebut cocok dengan url.py yang berada di level proyek, maka akan dilanjutkan ke file urls.py level aplikasi untuk mecocokan pola yang ada di dalam aplikasi
    - Lalu, jika terdapat kecocokan pola pada file level aplikasi tersebut, maka Django akan memanggil fungsi yang sesuai pada file views.py
    - Jika fungsi pada views.py membutuhkan data, maka akan berinteraksi dengan model yang menyimpan data-data tersebut di dalam database
    - views.py akan mengambil data dari model dengan cara melakukan Query dan database akan mengembalikan hasil query tersebut ke model yg akan disalurkan kembali ke view.py
    - Setelah request client diproses dan data tersedia, maka view akan memilih template HTML yang sesuai untuk dirender
    - Hasil akhirnya adalah Django akan mengirimkan HTTP response dalam bentuk HTML ke browser yang akan ditampilkan di web browser client

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


TUGAS INDIVIDU 3

1. Dalam mengimplementasikan sebuah platform, kita memerlukan data delivery agar data dapat diakses, diproses, dan didistribusikan secara efisien dan tepat waktu. Selain itu, data delivery memiliki peran penting dalam memastikan akurasi data, mendekteksi kesalahan, menjaga kualitas data, dan memastikan data memenuhi suatu kriteria tertentu. Oleh karena itu, data delivery dapat meningkatkan efisiensi operasional, mempercepat pengambilan keputusan, dan memastikan bahwa semua orang yang terlibat memiliki akses ke informasi yang sama dan konsisten sehingga dapat mengurangi kesalahan dalam penggunaan data

2. Menurut saya, JSON lebih baik daripada XML karena hasil data yang diperoleh menggunakan format JSON lebih mudah dibaca dan ringkas jika dibandingkan dengan format XML. Namun, bukan berarti format XML tidak lebih baik daripada format JSON karena perbadingan antara kedua format tersebut disesuaikan oleh tujuan dan kebutuhan sistem atau pengguna. Alasan JSON lebih populer daripada XML adalah hasil data yang diperoleh menggunakan format JSON lebih ringkas dan sederhana serta mudah dibaca dan dipahami oleh pengguna. Selain itu, JSON menggunakan memori yang lebih sedikit, proses penguraiannya lebih cepat dan aman, dan syntax yang digunakan lebih mudah ditulis.

3. Pada Django, method is_valid() berfungsi untuk memvalidasi formulir. Metode tersebut akan memeriksa data yang dikirim dalam formulir apakah sesuai dengan persyaratan yang telah didefinisikan dalam kelas formulir atau tidak sebelum diproses lebih lanjut atau disimpan ke dalam database. Jika data yang diperiksa tidak valid, maka method tersebut akan menghasilkan nilai False dan mengirimkan pesan mengenai kesalahan pada data yang dikrim atau error kepada pengguna untuk diperbaiki

4. Token CSRF (csrf_token) adalah nilai rahasia, unik dan tidak dapat diprediksi, yang dibuat aplikasi pada sisi server untuk melindungi pengguna dari serangan berbahaya. Token ini merupakan langkah keamanan unik yang dirancang untuk melidungi aplikasi web dari permintaan yang tidak sah atau berbahaya. Hal yang akan terjadi jika kita tidak menambahkan csrf_token adalah situs web akan rentan terhadap serangan Cross-Site Request Forgery (CSRF)yang memungkinkan penyerang/hacker melakukan tindakan atas nama pengguna tanpa sepengetahuan mereka. Kondisi seperti ini dapat dimanfaatkan oleh hacker dengan mencoba untuk membuat pengguna yang terautentikasi melakukan aksi yang tidak diinginkan di website tanpa sepengetahuan mereka, seperti membuat pengguna mengirim uang atau mengubah email di akun mereka hanya dengan mengklik link yang tampaknya tidak berbahaya dan hacker dapat mengakses data sensitif pengguna, seperti email, alamat, nomor telepon, dll. Selain itu, dari sisi pengembang web, hal ini dapat memengaruhi reputasi mereka sehingga dapat kehilangan kepercayaan dari pengguna.

5.  Cara saya mengimplementasikan checklist di atas adalah pertama saya membuka file views.py pada folder main dan membuat 4 funsgi untuk melihat objek dalam format XML, JSON, XML by ID, dan JSON by ID dan menambahkan try-exception pada fungsi XML by ID dan JSON by ID untuk menangkap error saat ID dari product tidak ada. Setelah itu, saya membuka urls.py dan mengimport keempat fungsi teserbut dari views.py. Setelah fungsi2 tersebut berhasil diimport, saya menambahkan path baru pada urlPatterns agar client dapat mengakses url tersebut dan menampilkan logika fungsi yang sudah dibuat pada file views.py. Lalu, saya mencoba menjalankan server localhost untuk mengetes apakah path yang ditambahkan sudah dapat diakses. Setelah berhasil membuat 4 fungsi tersebut, saya membuat folder template pada direktori utama dan membuat base.html yang digunakan sebagai template untuk file html yang lain. Setelah itu, saya mengubah file main.html pada folder main agar dapat meng-extend template base.html. Sesudah itu, saya membuat file bernama forms.py pada folder main yang mengimport model dari kelas Product yang sudah dibuat pada file models.py dan membuat struktur form yang dapat menambahkan produk baru dan mengindetifikasi atribut apa saja yang dapat dimasukkan saat menambahkan produk. Setelah itu, membuka file views.py dan mengimport form yang telah dibuat pada file forms.py serta model produk yang telah dibuat pada file models.py, membuat fungsi add_product untuk menghasilkan form yang dapat menambahkan produk baru dan membuat file add_product.html yang meng-extend base.html agar dapat menampilkan form pada aplikasi web dan menambahkan kode pada main.html untuk menampilkan tombol "Add Product" yang akan mengarahkan langsung ke halaman form. Setelah itu, saya menambahkan path pada urlPatterns di file urls.py agar client dapat mengakses halaman form untuk menambahkan objek. Setelah berhasil membuat halaman form, saya membuat fungsi show_product pada file views.py yang bertujuan untuk melihat details dari produk yang ditambahkan dan membuat file detail_product.html yang juga meng-extend base.html dan berfungsi sebagai struktur dari tampilan yang akan dihasilkan saat pengguna ingin melihat detail objek. Menambahkan path baru yang dapat menampilkan fungsi show_product pada urlPatterns di file urls.py yang berada di direktori main\templates.

6. Terima kasih kepada asdos yang sudah bersedia dan fast response untuk menjawab pertanyaan-pertanyaan dan membantu saya selama mengerjakan tugas individu 3.

- Screenshoot akses url XML
![alt text](https://github.com/NisriinaWakhdah/football-shop/blob/master/Screenshot%202025-09-14%20204423.png?raw=true)

- Screenshoot akses url JSON
![alt text](https://github.com/NisriinaWakhdah/football-shop/blob/master/Screenshot%202025-09-14%20204500.png?raw=true)

- Screenshot akses url XML by ID
![alt text](https://github.com/NisriinaWakhdah/football-shop/blob/master/Screenshot%202025-09-14%20204702.png?raw=true)

- Screenshot akses url JSON by ID
![alt text](https://github.com/NisriinaWakhdah/football-shop/blob/master/Screenshot%202025-09-14%20204639.png?raw=true)