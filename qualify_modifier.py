import pathlib
import time
from io import BytesIO

from google import genai
from google.genai import types
from PIL import Image as PILImage

API_KEY = "AIzaSyAYSSTqkfZ2mTDGGSkaE3Ar1ADOlTGVOEg"
MODEL_ID = "gemini-2.0-flash-preview-image-generation"


client = genai.Client(api_key=API_KEY)

# Prompts with increasing detail
prompts = [
    "A majestic mountain range in the style of an oil painting in 4K resolution.",
    "A beautiful landscape, watercolor style, high definition.",
    "A portrait of a woman, make it digital art and sketch style, use entry-level and high definition quality",
    "Create an abstract art painting with photorealistic styling and watercolor accents, high-detail.",
]


def save_image_from_response(response, timestamp):
    for part in response.candidates[0].content.parts:
        if part.text:
            continue
        elif part.inline_data:
            image_data = part.inline_data.data
            image = PILImage.open(BytesIO(image_data))

            output_dir = "static/images"
            pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

            image_filename = f"image_{timestamp}.png"
            image_path = f"{output_dir}/{image_filename}"
            image.save(image_path)
            return image_filename
    return None


def save_prompt(prompt, timestamp):
    output_dir = "static/images"
    prompt_filename = f"image_{timestamp}.txt"
    prompt_path = f"{output_dir}/{prompt_filename}"
    with open(prompt_path, "w") as f:
        f.write(prompt)


# Generate and save images
for prompt in prompts:
    try:
        print(f"Generating image for prompt: {prompt}")
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=types.GenerateContentConfig(response_modalities=["Text", "Image"]),
        )

        timestamp = int(time.time() * 1000)
        image_file = save_image_from_response(response, timestamp)

        if image_file:
            save_prompt(prompt, timestamp)
            print(f"Saved: {image_file} and its prompt.")
        else:
            print("No image found in response.")
    except Exception as e:
        print(f"Error generating image for prompt '{prompt}': {e}")
