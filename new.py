import pathlib

import PIL
from google import genai
from google.genai import types
from IPython.display import Image, Markdown, display

client = genai.Client(api_key="GOOGLE_API_KEY")

MODEL_ID = "gemini-2.0-flash-preview-image-generation"


def display_response(response):
    for part in response.candidates[0].content.parts:
        if part.text is not None:
            display(Markdown(part.text))
        elif part.inline_data is not None:
            mime = part.inline_data.mime_type
            print(mime)
            data = part.inline_data.data
            display(Image(data=data))


def save_image(response, path):
    for part in response.candidates[0].content.parts:
        if part.text is not None:
            continue
        elif part.inline_data is not None:
            _ = part.inline_data.mime_type
            data = part.inline_data.data
            pathlib.Path(path).write_bytes(data)


contents = "Create an image of a car"  # @param {type:"string"}

response = client.models.generate_content(
    model=MODEL_ID,
    contents=contents,
    config=types.GenerateContentConfig(response_modalities=["Text", "Image"]),
)

display_response(response)
save_image(response, "car.png")

text_prompt = "could you edit this image to make it look like a bike instead of a car"  # @param {type:"string"}

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[text_prompt, PIL.Image.open("car.png")],
    config=types.GenerateContentConfig(response_modalities=["Text", "Image"]),
)

display_response(response)
save_image(response, "bike.png")

contents = "Show me a burnt basque cheesecake with image."  # @param {type:"string"}

response = client.models.generate_content(
    model=MODEL_ID,
    contents=contents,
    config=types.GenerateContentConfig(response_modalities=["Text", "Image"]),
)

display_response(response)
save_image(response, "cheesecake.png")

chat = client.chats.create(
    model=MODEL_ID,
    config=types.GenerateContentConfig(response_modalities=["Text", "Image"]),
)

message = "create a cartoon image of batman"  # @param {type:"string"}

response = chat.send_message(message)
display_response(response)
save_image(response, "batman.png")
