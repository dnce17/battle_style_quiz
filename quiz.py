import json

class Quiz:

    with open("questions.json") as file:
        data = json.load(file)

    # All questions and entering answers occur here
    @classmethod
    def do_quiz(cls):
        for i, question in enumerate(cls.data):
            # Ask 1 question at a time
            cls._ask_question(i, question["question"])

            # Show choices for question
            for j, choice_role in enumerate(question["choices_and_roles"]):
                choice = choice_role[0]
                cls._show_choice(j, choice)
            
            # Loop until user enters elgible answer
            while True:
                total_choices = len(question["choices_and_roles"])
                if cls._validate_ans(cls._get_ans(), total_choices) == True:
                    break

            # Add +1 to that property in User class (not yet made)


            # For simplicity in testing, will ensure things work with 1 question and its choices and role
            break

    @staticmethod
    def _ask_question(num, question):
        print(f"Q{num + 1}) {question}\n")
    
    @staticmethod
    def _show_choice(num, choice):
        print(f"{num + 1} - {choice}")

    @staticmethod
    def _get_ans():
        return input("Enter a number that corresponds with the choices: ")
            
    @staticmethod
    def _validate_ans(ans, total_choices):
        try:
            if int(ans) not in range(1, total_choices + 1):
                return False
        except ValueError:
            return False
        
        return True

class Quizzee:
    def __init__(self):
        self._attacker = 0
        self._all_rounder = 0
        self._defender = 0
        self._supporter = 0
    
    # __str__ should show the results for all battle style and tell them what role they are suited for

    # instance method to add 1 to a property above depending on quizzee input to each question


if __name__ == "__main__":
    Quiz.do_quiz()

