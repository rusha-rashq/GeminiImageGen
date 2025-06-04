from flask import jsonify
from services.image_generator_service import ImageGeneratorService


class ImageGeneratorController:
    def __init__(self):
        api_key = "insert_your_api_key_here"
        self.image_generator_service = ImageGeneratorService(api_key)

    def generate_image(self, user_input):
        if not user_input:
            return {"error": "Missing input"}, 400
        try:
            base64_image = self.image_generator_service.generate_image(user_input)
            return {"image": base64_image}
        except Exception as e:
            return {"error": str(e)}, 500

    def get_images(self):
        images = self.image_generator_service.get_all_images()
        return jsonify({"images": images})
