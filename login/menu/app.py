from flask import Flask, render_template, request, redirect, url_for, flash
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Chave secreta para o uso de flash messages

# Caminho completo para o diretório de modelos (templates)
template_dir = os.path.join(os.path.dirname(__file__), "templates")
app.template_folder = template_dir

# Configuração do Flask-Uploads
photos = UploadSet("photos", IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = "uploads"  # Pasta onde as imagens serão armazenadas
configure_uploads(app, photos)

def save_text_fields(company, title, content, video, folder_path):
    # Salvar os outros campos de texto como um arquivo TXT
    text_data = f"Empresa: {company}\nTítulo: {title}\nConteúdo: {content}\nVídeo: {video}"
    file_path = os.path.join(folder_path, "info.txt")
    with open(file_path, "w") as file:
        file.write(text_data)

def get_unique_folder_name(base_folder, company):
    # Obter um nome de pasta único
    folder_name = company
    count = 1
    while os.path.exists(os.path.join(base_folder, folder_name)):
        folder_name = f"{company}{count}"
        count += 1
    return folder_name

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    try:
        # Obter dados do formulário
        company = request.form["company"]
        title = request.form["title"]
        content = request.form["content"]
        image = request.files["image"]
        video = request.form["video"]

        # Criar uma pasta com um nome único para a empresa
        folder_path = os.path.join(app.config["UPLOADED_PHOTOS_DEST"], get_unique_folder_name(app.config["UPLOADED_PHOTOS_DEST"], company))
        os.makedirs(folder_path, exist_ok=True)

        # Salvar a imagem dentro da mesma pasta que as informações
        if image:
            filename = photos.save(image, folder=company)
            flash("Upload da imagem bem-sucedido!", "success")
        else:
            flash("Falha no upload da imagem!", "error")

        # Salvar os outros campos de texto como um arquivo TXT
        save_text_fields(company, title, content, video, folder_path)

        flash("Upload completo!", "success")

    except Exception as e:
        print(f"Erro durante o upload: {str(e)}")
        flash("Ocorreu um erro durante o upload!", "error")

    # Redirecionar para a página inicial
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
