class Exam:
    def __init__(self):
        self.__questions = []
        self.__points = 0

    def add_question(self, question):
        self.__questions.append(question)

    def take(self):
        for question in self.__questions:
            print(question.get_question())
            response = input()
            if question.check_answer(response):
                print("True\n")
                self.__points += 1
            else:
                print("False\n")

    def get_points(self):
        return self.__points

    def get_num_questions(self):
        return len(self.__questions)

    def __repr__(self):
        return f"Exam({self.__questions!r})"

    def __str__(self):
        questions_str = "\n".join(str(question) for question in self.__questions)
        return f"{questions_str}\n"

    def some_other_method(self):
        pass
