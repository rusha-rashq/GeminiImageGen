from io import BytesIO
from types import SimpleNamespace

from models.image_manager import ImageManager
from PIL import Image

image_manager = ImageManager()

image = Image.new("RGB", (100, 100), color="red")

buffer = BytesIO()
image.save(buffer, format="JPEG")
image_data = buffer.getvalue()
fake_image_data = SimpleNamespace(image=SimpleNamespace(image_bytes=image_data))

prompt = (
    "Luxury Tech Conference 2025: Innovating the Future - April 10th, New York City"
)

result = image_manager.add_image(prompt, fake_image_data)
print("Image Added Successfully:")
print(result)
print("\nAll Stored Images:")
print(image_manager.get_images())
