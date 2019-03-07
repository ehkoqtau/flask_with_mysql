"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for, session, flash
from web_flask import app

from .include.rumus_mtk import Lingkaran


#config
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

@app.after_request
def apply_config(response):
    response.headers['server'] = "Python @ehkoqtau"
    return response

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.route('/')
@app.route('/home')
@app.route('/home/<int:number>')
def index(number = 1):
    m_rumus_mtk = Lingkaran()
    m_rumus_mtk.setRadius(number)
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        m_rumus_mtk = m_rumus_mtk
    )

@app.route('/dashboard')
def dashboard():
    if session.get('username'):
        data = {
                'nama' : session.get('nama'),
                'username' : session.get('username')
            }
        return render_template(
            'dashboard.html',
            title='Dashboard',
            year=datetime.now().year,
            data = data
        )
    else:
        flash('Anda belum masuk')
        return render_template(
                'login.html',
                title='Login',
                year=datetime.now().year
            )

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.values.get('username')
		password = request.values.get('password')

		#if request.values.get('username') == 'ehkoqtau' and request.values.get('password') == '234':
		if username and password:
			from .include.mysql import Login
			c = Login(username, password)
			return c.login()
		else:
			flash('User atau password salah')
			return render_template(
                'login.html',
                title='Login',
                year=datetime.now().year
            )
	else:
		flash('Halaman Login')
		return render_template(
            'login.html',
            title='Login',
            year=datetime.now().year
        )

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
        # read the posted values from the UI
		nama = request.form['nama']
		username = request.form['username']
		password = request.form['password']

		if nama and username and password:
			from .include.mysql import Register
			c = Register(nama, username, password)
			return c.register()
		else:
			flash('Tidak ada data pendaftaran yang diterima')
			return redirect(url_for('register'))
	else:
		flash('Halaman Register')
		return render_template(
            'register.html',
            title='Register',
            year=datetime.now().year
        )



@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('index'))