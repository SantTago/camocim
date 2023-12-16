from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder=os.path.abspath('templates'))

# Função para ler usuários e senhas do arquivo
def ler_usuarios():
    usuarios = {}
    with open(os.path.join(os.path.dirname(__file__), 'usuarios.txt'), 'r') as arquivo:
        for linha in arquivo:
            usuario, senha = linha.strip().split(':')
            usuarios[usuario] = senha
    return usuarios

# Usuários e senhas definidos
usuarios = ler_usuarios()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']

    if usuario in usuarios and usuarios[usuario] == senha:
        return render_template('acesso_permitido.html', usuario=usuario)
    else:
        return render_template('acesso_negado.html')

if __name__ == '__main__':
    app.run(debug=True)
