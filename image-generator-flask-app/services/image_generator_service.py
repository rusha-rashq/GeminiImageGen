from io import BytesIO

from google import genai
from google.genai import types
from models.image_manager import ImageManager
from models.prompt_manager import PromptManager
from PIL import Image as PILImage


class ImageGeneratorService:
    def __init__(self, api_key: str):
        self.image_manager = ImageManager()
        self.gemini_client = genai.Client(api_key=api_key)
        self.model_id = "gemini-2.0-flash-preview-image-generation"

    def generate_image(self, user_input: str) -> str:
        prompt = PromptManager.format_prompt(user_input)
        try:
            response = self.gemini_client.models.generate_content(
                model=self.model_id,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["Text", "Image"]
                ),
            )

            image_data = None
            for part in response.candidates[0].content.parts:
                if part.inline_data:
                    image_data = part.inline_data.data
                    break

            if not image_data:
                raise ValueError("No image returned in response.")

            image = PILImage.open(BytesIO(image_data))
            return self.image_manager.add_image(prompt, image)

        except Exception as e:
            raise RuntimeError(f"Error generating image: {str(e)}")

    def get_all_images(self):
        return self.image_manager.get_images()
