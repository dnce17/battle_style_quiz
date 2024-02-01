def main():
    show_quiz_purpose()
    while start_quiz() == False:
        continue

    # General idea of how program will operate (subject to change)
    # ask_questions()
    # get_answers()
    # update_points()
    # tally_points()
    # show_results


def show_quiz_purpose():
    print(
        """
        Have you ever played a video game and weren't sure whether if you wanted to be an
        attacker, defender, support, or all-rounder? Well look no further because this quiz is for you! 
        """
    ) 


def start_quiz():
    return True if input("Type and enter \"y\" to get started: ").strip().lower() == "y" else False