class PromptManager:

    @classmethod
    def load_base_prompt(cls, file_path: str = "data/image_prompt_template.txt") -> str:
        try:
            with open(file_path, "r") as f:
                return f.read()
        except Exception as e:
            print(f"Error loading prompt template: {e}")
            return (
                "# ROLE\nYou are a professional graphic designer.\n\n"
                "# THEME\n{user_input}\n\n"
                "# TASK\nPlease generate a beautiful banner.\n"
            )

    @classmethod
    def format_prompt(cls, user_input: str) -> str:
        base_prompt = cls.load_base_prompt()
        return base_prompt.format(user_input=user_input)
