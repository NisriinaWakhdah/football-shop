Nama: Nisriina Wakhdah Haris
 NPM: 2406360445
 Kelas: PBP - B
link menuju app PWS: https://nisriina-wakhdah-footballshop.pbp.cs.ui.ac.id/

<details>
<Summary><b>TUGAS INDIVIDU 2</b></Summary>

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

</details>

<details>
<Summary><b>TUGAS INDIVIDU 3</b></Summary>

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

</details>

<details>
<Summary><b>TUGAS INDIVIDU 4</b></Summary>

1. Django AuthenticationForm adalah formulir autentikasi bawaan Django yang digunakan untuk memverifikasi kredensial pengguna saat login ke suatu aplikasi. Formulir autentikasi ini menangani akun pengguna, grup, izin, dan sesi pengguna berbasis cookie. Kelebihan Django AuthenticationForm adalah:
    - Autentikasi pengguna ini telah diuji secara ekstensif oleh banyak  aplikasi yang menggunakannya dalam lingkup produksi sehingga fitur ini terbukti bekerja dengan baik dalam dunia nyata
    - Sistem ini mendapat dukungan resmi langsung dari para pengelola atau komunitas Django sehingga ada jaminan perbaikan dan keamanan dari sumber resmi
    - Sistem ini fleksibel karena dibangun dengan cara yang sangat generik sehingga bisa disesuaikan dengan kebutuhan proyek dan dengan mempertimbangkan bahwa terdapat banyak pengguna yang mungkin perlu memperluas fungsionalitas aplikasinya
    - Syntaxnya cenderung simpel dan mudah dipahami karena ditulis dengan bahasa python 
Selain itu, kekurangannya adalah:
    - Django menyediakan banyak fitur dan alat bawaan untuk autentikasi dan lainnya sehingga memerlukan waktu yang lebih lama untuk dipelajari dan dipahami oleh pengembang dan tidak langsung berlaku untuk sistem autentikasi yang lain
    - Sistem autentikasi Django dibuat fleksibel dan generik (tidak spesifik untuk satu jenis aplikasi saja) sehingga tidak dapat langsung disesuaikan untuk kebutuhan tiap aplikasi sehingga pengembang harus menyesuaikannya sendiri dengan kebutuhan yang ada, hal ini bisa merepotkan
    - Sistem autentikasi yang sederhana ini bisa saja tidak cocok untuk aplikasi yang membutuhkan fitur yang lebih kompleks

2. Perbedaan autentikasi dan otorisasi adalah autentikasi berfungsi untuk memverifikasi dan mengonfirmasi kebenaran identitas pengguna atau layanan yang mencoba untuk mengakses sistem, sedangkan otorisasi bertujuan untuk memberi pengguna atau layanan izin mengakses (hak akses) data atau melakukan tindakan tertentu. Django mengimplementasikan autentikasi dengan menggunakan fungsi bawaan Django dan diimport melalui: from django.contrib.auth import authenticate, login, logout. Fitur utamanya adalah melakukan autentikasi, login, dan logout, saat user berhasil login (authenticate() + login()), Django membuat session ID yang bersifat rahasia dan menyimpannya dalam cookie di browser pengguna dan saat user melakukan logout, session ID dan cookie tersebut akan dihapus. Selain itu, Django menyediakan sistem permissions, groups dan decorators/mixins yang dapat digunakan untuk mengatrur izin akses pengguna, contoh decorator yang dapat digunakan adalah login_required dan permission_required dari sistem autentikasi Django (diimport melalui from django.contrib.auth.decorators import login_required, permission_required). Decorator ini diletakkan di atas kode fungsi yang menurut kita tidak dapat diakses oleh sembarang pengguna, di mana hanya pengguna khusus saja yang dapat diperbolehkan untuk mengaskes fungsi tersebut, misalnya pengguna yang sudah memiliki akun dan berhasil login. Decorators tidak mengubah isi kode fungsi tersebut, melainkan dapat kita gunakan untuk menambah fungsionalitas suatu fungsi

3. Penyimpanan session adalah menyimpan data dalam pasangan kunci-nilai dalam peramban web, namun penyimpanan tersebut hanya tersedia hingga sesi tersebut aktif, di mana jika user keluar dari situs web, maka semua data yang tersimpan akan dihapus. Kelebihan penyimpanan sesi adalah:
    - Keamanan data terjamin karena data disimpan selama sesi berlangsung dan otomatis dihapus ketika sesi berakhir
    - Data yang disimpan bersifat sementara sehingga dapat meminimalkan kekacauan dan ruang penyimpanan di situs web user
    - Penyimpanan ini mudah diimplementasikan dan digunakan pada aplikasi daring karena APInya mudah dipahami
    Selain itu, kekurangannya adalah:
    - Penyimpanan sesi terbatas karena tergantung dengan webnya dan biasanya hanya memiliki batas penyimpanan dari 5 sampai 10 MB sehingga tidak sesuai untuk penyimpanan skala besar
    - User bisa saja mengalami kesulitan untuk mengakses data karena data akan dihapus ketika sesi berakhir karena penyimpanan ini bergantung pada sesi penulusuran yang sedang aktif
    - Cakupan penyimpanan seso adalah penelusuran saat ini yang tidak bisa dibagikan ke seluruh tab atau jendela aplikasi web sehingga proses berbagi data antar komponen aplikasi yang sama atau berbeda dapat menjadi masalah
Selain itu, terdapat penyimpanan cookies, yaitu file teks kecil (berisi data) yang disimpan pada perangkat pengguna ketika ia mengakses situs web untuk pertama kalinya. Kelebihan cookie antara lain adalah:
    - Cookie digunakan untuk mengigat preferensi pengguna sehingga dapat menciptakan pengalaman yang lebih personal bagi pengguna dan halaman web dapat dimuat dengan cepat
    - Menyimpan data seperti informasi login atau isi keranjang belanja sehingga dapat menyederhanakan cara user berinteraksi dengan situs web
    - Membantu meningkatkan kinerja halaman web dan menempati sedikit memori melalui penyimpanan data dalam cache dan mengurangi permintaan server
    - Mudah digunakan karena browser otomatis mengirim cookie ke server setiap request
    Berikut ini adalah kekurangan penyimpanan cookie:
    - Data yang disimpan dapat dicuri dengan serangan XXS dan disalahgunakan tanpa sepengetahuan pemiliknya sehingga keamanannya tidak terjamin
    - Jika user mematikan cookie, maka cookie mungkin tidak berfungsi secara efektif di setiap perangkat karena beberapa fitur aplikasi tidak akan jalan yang mengakibatkan pengalaman user yang tidak konsisten
    - Tidak dapat menyimpan data yang complex dan hanya bisa menyimpan data berbentuk teks biasa
    - Pengguna dapat menghapus cookie sehingga dapat kehilangan status login,kehilangan preferensi atau pengaturan, dan tidak bisa mengakses ke session lama, seperti isi keranjang belanja, draft, dll

4. Sebenarnya penggunaan cookie aman secara defaultnya karena hanya berupa data teks dan tidak dapat mentrasfer malware atau virus. Akan tetapi data yang disimpan di dalam cookie berisiko untuk dicuri dan disalahgunakan oleh pihak yang tidak bertanggung jawab sehingga dapat merugikan user. Hal ini dapat terjadi apabila kita tidak memberikan pengamanan pada cookie yang ada, misalnya cookie tidak dienkripsi dan tidak dikirim melalui HTTPS. Risiko potensial yang harus diwaspadai adalah kasus Cross Site Scripting (XSS) di mana seseorang bisa mencuri cookies dari pengguna yang sudah melakukan login ke sebuah website dengan cara menyuntikkan kode/script berbahaya yang digunakan untuk mencuri cookie user. Selain itu, terdapat kasus pembajakan sesi (session hijacking) di mana hacker dapat mencegat cookie yang dikirimkan melalui jaringan yang tidak aman, seperti wi-fi publik, dan juga terdapat kasus Cross-site Request Forgery (CSRF) di mana hacker melakukan request autentikasi atau cookie pengguna kepada user yang sedang mengakses aplikasi web tersebut untuk mendapatkan informasi penting yang dimiliki user. Cara Django menangani hal ini adalah dengan mengatur keamanan cookie menggunakan beberapa settings bawaan, seperti SESSION_COOKIE_SECURE = True (hanya dikirim lewat HTTPS), SESSION_COOKIE_HTTPONLY = True (mencegah skrip sisi klien mengakses cookie), SESSION_COOKIE_SAMESIT (Membantu mencegah kebocoran informasi, menjaga privasi pengguna , dan memberikan perlindungan terhadap serangan CSRF), CSRF_COOKIE_SECURE = True, dan CSRF_COOKIE_HTTPONLY = True untuk melindungi token CSRF. Oleh karena itu, aman atau tidaknya suatu cookie tergantung pada bagaimana cookie tersebut dikelola dan diamankan. Jika cookie disimpan dengan benar dan diberikan perlindungan khusus, maka risiko pencurian data cookie dapat diminimalisir dibandingkan dengan cookie yang tidak diberi proteksi sama sekali.

5. Cara saya mengimplementasikan checklist tersebut adalah:
    - Pertama saya membuka folder football-shop dan membuat fungsi untuk registrasi, login, dan logout pada file views.py. Setelah membuat fungsi-fungsi tersebut, saya membuka urls.py pada folder main dan melakukan import fungsi2 yang sudah dibuat di views.py untuk menambahkan urlPatterns agar user dapat mengakses fungsi2 tersebut. Selain itu, pada file views.py saya menambahkan import datetime, HttpResponseRedirect, dan reverse agar dapat menggunakan dan menyimpan cookie yang berisi timestamp terkahir kali pengguna melakukan login. Setelah itu, menambahkan key-value baru, yaitu last_login pada fungsi show_main ke dalam variabel context agar dapat mengakses data di cookie yang sudah terdaftar dan agar informasi last_login dapat ditampilkan di halaman utama aplikasi. Saya juga menambahkan dekorator pada fungsi show_main, show_product, dan add_product agar halaman utama dan product hanya bisa diakses oleh pengguna yang sudah terautentikasi
    - Membuat template dengan tipe html untuk fungsi regitrasi, login, dan logout yang akan ditampilkan di halaman web. Selain itu, pada template registasi.html saya menambahkan button untuk mereset input yang dimasukkan pengguna agar user dapat menghapusnya sekaligus saat ada kesalahan dalam menuliskan username atau password saat regitrasi
    - Setelah berhasil membuat fungsi2 tersebut dan templatenya, saya membuka file models.py yang berada di folder main dan melakukan import User. Setelah berhasil mengimport User ke dalam model, saya menambahkan kode user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) pada class Product dan kode ini berfungsi untuk menghubungkan suatu product dengan user. Setelah itu menambahkan beberapa kode pada add_product agar setiap product yang dibuat akan otomatis terhubung dengan pengguna yang membuatnya dan menambahkan kode yang berguna untuk memfilter produk pada fungsi show_main sesuai dengan request dari user, dan menambahkan tombol untuk memfilter produk pada halaman uatama di file main.html dan juga menambahkan nama penjual produk pada file detail_product.html
    - Melakuka python makemigrations dan migrate agar perubahan pada model dapat disimpan dan diperbarui
    - Menjalankan program secara lokal dan membuat 2 akun pengguna dan setiap pengguna menjual 3 barang (dummy data) untuk mengetes apakah kode berjalan dengan baik
    - Setelah kode dipastikan dapat berjalan dengan baik, saya melakukan add, commit, dan push ke GitHub dan push ke PWS



    username: soKlin
    pass : dijaminBersih7

    username: maruko.chan
    pass: chibihaha22
</details>