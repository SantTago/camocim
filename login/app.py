from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dicionário de usuários (substitua com os seus próprios dados)
usuarios = {
    'tiago': '1',
    'usuario2': 'senha2',
    'usuario3': 'senha3'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username_input = request.form.get('username')
    password_input = request.form.get('password')

    if username_input in usuarios and usuarios[username_input] == password_input:
        return jsonify({'redirect': '/usuarios.html'})
    else:
        return jsonify({'error': 'Usuário ou senha incorretos'})

if __name__ == '__main__':
    app.run(debug=True)
