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
                    quizzee._add_role_pts(*role_arr)
                    break
        
        quizzee._show_results()
        print()
    
    # NONPRIVATE METHODS
    @classmethod
    def show_total_questions(cls):
        print(f"Total Questions: {len(cls.data)}")   

    # Get max total of each role
    @classmethod
    def get_max_roles_total(cls):
        # If there is more role types than you initially put in, there is a typo in question.json somewhere
        roles = {}
        for _, question in enumerate(cls.data):
            for _, choice_role in enumerate(question["choices_and_roles"]):
                # [1:] b/c some choice linked with > 1 roles
                for role in choice_role[1:]:
                    if role not in roles:
                        roles[role] = 1
                    else:
                        roles[role] += 1

        return dict(sorted(roles.items()))
    
    @classmethod
    def show_max_roles_total(cls):
        print(cls.get_max_roles_total())
    
    @classmethod
    def show_all_roles(cls):
        roles = [role for role in cls.get_max_roles_total()]
        print(roles)

    # PRIVATE METHODS
    @staticmethod
    def _ask_question(num, question):
        print(f"\nQ{num + 1}) {question}")
    
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
    def _add_role_pts(self, *roles):
        for role in roles:
            role = role.strip().lower()
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
    
    def _show_results(self):
        results_list = sorted(vars(self).items(), key=lambda role: role[1], reverse=True)
        print("\nRESULTS:")
        for role in dict(results_list):
            print(f"{role.lstrip('_').title().replace('_', '-')}: {vars(self)[role]}")