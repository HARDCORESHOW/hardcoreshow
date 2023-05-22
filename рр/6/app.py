from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    if 'username' in session:
        return redirect('/admin')
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Проверка логина и пароля (ваша логика авторизации)
    if username == 'admin' and password == 'password':
        session['username'] = username
        return redirect('/admin')
    else:
        return 'Неправильный логин или пароль'


@app.route('/admin')
def admin():
    if 'username' in session:
        return render_template('admin.html')
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == '__main__':
    app.run()
 
