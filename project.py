from quiz import Quiz, Quizzee


def main():
    show_quiz_purpose()
    Quiz.show_total_questions()
    while ready() == False:
        continue

    user = Quizzee()
    Quiz.do_quiz(user)
    

def show_quiz_purpose():
    print(
        """
        Have you ever played a video game and weren't sure whether if you wanted to be an
        attacker, defender, support, or all-rounder? Well look no further because this quiz is for you! 
        """
    ) 


def ready():
    return True if input("Type and enter \"y\" to get started: ").strip().lower() == "y" else False


if __name__ == "__main__":
    main()