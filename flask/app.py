from flask import Flask, flash, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'minha_chave_secreta'

# Dicionário de usuários com senha protegida
usuarios = {
    "Rychard": generate_password_hash("seila123")
}

@app.route('/')
@app.route('/home')
def home():
    if 'username' in session:
        return f"Bem-vindo, {session['username']}!"
    else:
        return "Bem-vindo ao meu sistema de Login. Por favor, faça login."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verifica o nome de usuário e a senha
        if username in usuarios and check_password_hash(usuarios[username], password):
            session['username'] = username
            flash('Login realizado com sucesso!', 'success')  # Mensagem de sucesso
            return redirect(url_for('home'))
        else:
            flash('Nome de usuário ou senha incorretos.', 'danger')  # Mensagem de erro
    
    return render_template("login.html")
        #rota para deslogar o úsuario e levar ele de volta para a home
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
