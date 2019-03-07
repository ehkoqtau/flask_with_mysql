from web_flask import app
from flaskext.mysql import MySQL
from flask_bcrypt import Bcrypt
from flask import render_template, request, redirect, url_for, session, flash

bcrypt = Bcrypt(app)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'flask_1'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('sp_validateLogin',(self.username,))
        data = cursor.fetchall()

        if len(data) > 0:
            if bcrypt.check_password_hash(str(data[0][3]),self.password):
                session['nama'] = data[0][1]
                session['username'] = data[0][2]
                return redirect(url_for('dashboard'))
            else:
                flash('Password salah')
                return redirect(url_for('login'))
        else:
            flash('Username atau password salah')
            return redirect(url_for('login'))
        cursor.close()
        con.close()

class Register:
    def __init__(self, nama, username, password):
        self.nama = nama
        self.username = username
        self.password = password

    def register(self):
        #Proses pemanggilan di Mysql
        conn = mysql.connect()
        cursor = conn.cursor()
        hashed_password = bcrypt.generate_password_hash(self.password)
        cursor.callproc('sp_createUser',(self.nama,self.username,hashed_password))
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            flash('Register berhasil')
            return redirect(url_for('register'))
        else:
            flash('Register gagal')
            return redirect(url_for('register'))
        cursor.close() 
        conn.close()