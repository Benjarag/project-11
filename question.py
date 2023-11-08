
class Question:

    def __init__(self, question, answer):
        self.__question_str = question
        self.__answer_str = answer
 
    def get_question(self):
        return self.__question_str

    def check_answer(self, response):
        return response.lower() == self.__answer_str.lower()

    def __str__(self):
        return f"Q: {self.__question_str} A: {self.__answer_str}"
        
