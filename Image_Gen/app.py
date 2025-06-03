from controllers.image_generator_controller import ImageGeneratorController
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

image_generator_controller = ImageGeneratorController()


@app.route("/")
def index():
    return render_template("image_generator.html")


@app.route("/api/generate_image", methods=["POST"])
def generate_image():
    user_input = request.json.get("user_input")
    return image_generator_controller.generate_image(user_input)


@app.route("/api/get_images", methods=["GET"])
def get_images():
    return image_generator_controller.get_images()


if __name__ == "__main__":
    app.run(port=3000, host="0.0.0.0", debug=True)
