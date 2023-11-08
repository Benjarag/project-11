

class ChoiceQuestion:

    def __init__(self, question):
        self.__question_str = question
        self.choices = []

    def add_choice(self, choice, is_correct):
        self.choices.append((choice, is_correct))

    def get_question(self):
        choices_str = "\n".join([f"{i}. {choice}" for i, (choice, _) in enumerate(self.choices, start=1)])
        return f"{self.__question_str}\n{choices_str}"
    
    def check_answer(self, response):
        try:
            response_num = int(response)
            if 1 <= response_num <= len(self.choices):
                # Check if the selected choice is correct
                return self.choices[response_num - 1][1]  # Adjust index for 0-based list
        except ValueError:
            pass

        return False
    
    def get_correct_choice(self):
        for i, (choice, is_correct) in enumerate(self.choices, start=1):
            if is_correct:
                return str(i)  # Convert the correct choice number to a string

    def __str__(self):
        correct_choice = self.get_correct_choice()
        return f"Q: {self.__question_str} A: {correct_choice}"