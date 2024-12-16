from flask import Flask, request
from werkzeug.utils import secure_filename
import os

from dotenv import load_dotenv

from services.gemini_servioe import GeminiService

load_dotenv()

temp_path = os.path.join(os.getcwd(), "temp")

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = temp_path


@app.get("/hello-world")
def hello_world():
    return {"msg": "Hello World"}


@app.post("/generate-alt-description")
def generate_alt_description():
    if "image" not in request.files:
        return {"msg": "O Campo img  não está presente na requisição"}, 400

    img_photo = request.files["image"]

    img_filename = secure_filename(img_photo.filename)

    img_path = os.path.join(temp_path, img_filename)

    img_photo.save(img_path)

    gemini_service =  GeminiService(os.getenv('GCLOUD_PROJECT_ID'), os.getenv('GCLOUD_REGION'))

    description =  gemini_service.generate_description_by_ai(img_path)


    os.remove(img_path)

    
    return {
        "alt_description": description
    }



