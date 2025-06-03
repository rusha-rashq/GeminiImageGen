from controllers.image_generator_controller import ImageGeneratorController

controller = ImageGeneratorController()


try:
    response = controller.generate_image("Semiconductor technology")
    if "error" in response:
        print(f"Error: {response['error']}")
    else:
        print("Generated Image:")
        print(response["image"])
except Exception as e:
    print(f"Error generating image: {str(e)}")


empty_response = controller.generate_image("")
try:
    print("\nError Test:")
    print(f"Status Code: {response[1]}")
    print(f"Response: {response[0]}")
except Exception as e:
    print(f"Error generating image: {str(e)}")
