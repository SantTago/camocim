from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Aqui você pode processar os dados do formulário
        nome_empresa = request.form['company']
        titulo = request.form['title']
        conteudo = request.form['content']
        imagem = request.files['image']
        video = request.form['video']

        # Aqui você pode fazer o que quiser com os dados, por exemplo, enviá-los por email, armazenar em um banco de dados, etc.

        return 'Formulário enviado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
