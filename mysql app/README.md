# mysqlapp

Aplikasi perpustakaan dengan dua service, yakni borrows dan customers, menggunakan RDBMS

**Customers service**


1. Menampilkan data di dalam database
    - Menampilkan semua data di dalam database Customers
      * GET localhost:5000/users
    - Menampilkan data Customers by Id
      * GET localhost:5000/user
2. Melakukan modifikasi data di dalam database
    - Melakukan insert database
      * POST localhost:5000/user/insert
    - Melakukan update database
      * POST localhost:5000/user/update
    - Melakukan Delete database
      * POST localhost:5000/user/delete
3. Request JWT
    - Melakukan request token
      * GET ocalhost:5000/user/requestToken

------------------------------------------------------------------------

**Borrows service**


1. Menampilkan data pada database peminjaman
   * GET localhost:5000/borrows
2. Melakukan insert database peminjaman
   * POST localhost:5000/borrows/insert
3. Melakukan update status peminjaman
   * POST localhost:5000/borrows/status
