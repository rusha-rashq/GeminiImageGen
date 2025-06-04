import base64
from io import BytesIO

from PIL import Image


class ImageManager:
    def __init__(self):
        self.images = []

    def add_image(self, prompt, image_data):
        image_base64 = self.image_to_base64(image_data)
        image_entry = {
            "id": len(self.images),
            "prompt": prompt,
            "image_base64": image_base64,
        }
        self.images.append(image_entry)
        return image_base64

    def get_images(self):
        return self.images

    def image_to_base64(self, image_data):
        try:
            # If image_data is already a PIL Image:
            if isinstance(image_data, Image.Image):
                buffered = BytesIO()
                image_data.save(buffered, format="JPEG")
                return base64.b64encode(buffered.getvalue()).decode("utf-8")
            # Otherwise, if you ever change to pass raw bytes:
            #   image = Image.open(BytesIO(image_data))
            #   buffered = BytesIO()
            #   image.save(buffered, format="JPEG")
            #   return base64.b64encode(buffered.getvalue()).decode("utf-8")

            # (You can add more branches here if needed.)
            raise RuntimeError("Unsupported image_data type in image_to_base64()")
        except Exception as e:
            raise RuntimeError(f"Error processing image: {str(e)}")
