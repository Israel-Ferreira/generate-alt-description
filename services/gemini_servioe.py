import vertexai
from vertexai.generative_models import GenerativeModel, Image

class GeminiService:
    def __init__(self, project, location, model='gemini-1.5-pro-002'):
        self.project = project
        self.location =  location
        self.model = model



    def generate_description_by_ai(self, img_path):
        vertexai.init(project=self.project, location=self.location)


        
        vision_model = GenerativeModel(self.model)

        img =  Image.load_from_file(img_path)

        prompt = """
        Gere uma descrição da imagem
        """

        return vision_model.generate_content([prompt, img]).text

