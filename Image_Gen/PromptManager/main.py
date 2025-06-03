from models.prompt_manager import PromptManager

user_input = (
    "Luxury Tech Conference 2025: Innovating the Future - April 10th, New York City"
)
formatted_prompt = PromptManager.format_prompt(user_input)

print("Generated Prompt:")
print(formatted_prompt)
