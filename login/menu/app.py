from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

# Configuração do Flask-Uploads
photos = UploadSet("photos", IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = "uploads"  # Pasta onde as imagens serão armazenadas
configure_uploads(app, photos)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    # Obter dados do formulário
    company = request.form["company"]
    title = request.form["title"]
    content = request.form["content"]
    image = request.files["image"]
    video = request.form["video"]

    # Salvar a imagem na pasta configurada
    if image:
        filename = photos.save(image)
        image_path = f"uploads/{filename}"
    else:
        image_path = None

    # Processar os dados como desejado (por exemplo, salvar no banco de dados)

    # Redirecionar para a página inicial
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
