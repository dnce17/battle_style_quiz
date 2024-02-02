import json
import sys


class Quiz:
    with open("questions.json") as file:
        data = json.load(file)

    # All questions and entering answers occur here
    @classmethod
    def do_quiz(cls, quizzee):
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
                ans = cls._get_ans()
                if cls._validate_ans(ans, total_choices) == True:
                    # Creates arr to consider the choices linked with more than 1 role
                    role_arr = question["choices_and_roles"][int(ans) - 1][1:]
                    quizzee._add_role_point(*role_arr)
                    break

            # For simplicity in testing, will ensure things work with 1 question and its choices and role
            # break
        
        # Show user their results and tell them what role they are

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

    # Add 1 to property/ies above depending on quizzee input to each question
    # Unpacking the roles arr
    def _add_role_point(self, *roles_arr):
        for role in roles_arr:
            if role == "attacker":
                self._attacker += 1
            elif role == "all-rounder":
                self._all_rounder += 1
            elif role == "defender":
                self._defender += 1
            elif role == "supporter":
                self._supporter += 1
            else:
                sys.exit("ERROR: no role match")
        
        # Test purposes - display all properties
        # print(vars(self))
    
    # show_results instead of __str__ actually cause func name is clear
    def _show_results(self):
        results_list = sorted(vars(self).items(), key=lambda role: role[1], reverse=True)
        for role in dict(results_list):
            print(f"{role.lstrip('_').title().replace('_', '-')}: {vars(self)[role]}")


if __name__ == "__main__":
    user = Quizzee()
    Quiz.do_quiz(user)
    user._show_results()

