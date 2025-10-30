# Import library pihak ketiga
from flask import Flask, render_template
from flask_mysqldb import MySQL

# Inisialisasi aplikasi utama
app = Flask(__name__)

# Konfigurasi database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskmysql'

# Inisialisasi koneksi MySQL
mysql = MySQL(app)

# Route utama (halaman home)
@app.route('/')
def home():
    # Membuat cursor untuk koneksi MySQL
    cur = mysql.connection.cursor()
    # Menjalankan query
    cur.execute("SELECT * FROM users")
    # Mengambil semua hasil query
    data = cur.fetchall()
    # Menutup koneksi cursor
    cur.close()
    # Mengirim data ke template home.html
    return render_template('home.html', users=data)

# Menjalankan aplikasi dengan mode debug
if __name__ == '__main__':
    app.run(debug=True)
