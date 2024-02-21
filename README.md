# Battle Style/Role Quiz

## Function
This quiz can help people figure out what role (all-rounder, attacker, defender, supporter) to pick in games that include them such as Pokemon Unite and League of Legends.

## How to run/test
To run, type and enter the following in terminal:
1. source .venv/bin/activate
    * activates the virtual env
2. python project.py
    * lets you take the battle style quiz

To test: 
* pytest test_project.py
    * If configurations are made to this program, run this to ensure certain functions still work properly

## Technologies Used
* Python
* JSON

## Info on Key Files
* project.py
    * simply runs the entirety of the quiz process
* quiz.py
    * contains the classes imported to project.py
    * The Quiz class contains the related methods to select an answer and display questions, answers, and results, most of which are called inside the do_quiz method to run the quiz process
    * The Quizzee class contains properties of the items that are to be tracked. It contains a method to match the tracked items to an answer choice when picked and update the points of the properties accordingly. It also has a function to show the results after the quiz the done. Both functions are called in the do_quiz method of the Quiz class.
* test_project.py
    * tests Quiz class's _validate_ans method and Quizzee class's _add_role_pts method
* questions.json
    * contains all the questions, answer choices, and items linked with each choice
* requirements.txt
    * Python packages to install for the quiz program to run properly

## How to Configure
<b>UPDATE</b>: After this project's completion, I developed a more user-friendly tool called [PDF to Survey/Quiz Converter](https://github.com/dnce17/pdf_to_survey_quiz). This tool allows processing of PDF-formatted surveys/quizzes made in a text processor for others to take, making it easier to create personalized surveys/quizzes since code does not have to be modified. 

You can use this tool as an alternative to the instructions provided below for configuring this quiz.
<hr>

This quiz can be used as a template for answers that are associated with something, in which you may want to keep track of that.  

For example, if all questions had 3 answer choices and low, medium, and high risk are associated with each choice respectively, this quiz can be altered to track how many times the user picks a choice linked with each of those risk levels.

For this quiz program, each question does **not** need to have the same amount of choices. Each choice can also have more than 1 item associated with it too.

### To configure it...
* questions.json
    * replace the questions with your own
    * in the key named "choices_and_roles", the value is an array whose 1st item should be 1 answer choice; the 2nd item onwards can be whatever is associated with that answer choice
* project.py
    * Adjust the string printed in show_quiz_purpose()
* quiz.py
    * For the Quizzee class
        * adjust properties in the init function as needed to track all items associated with answer choices
        * for the _add_role_pts method, adjust it accordingly based on those tracked items
        * OPTIONAL: find and replace the word "role" or "roles" with the category of what you're tracking (e.g. risk level, personality)
* test_project.py
    * adjust the test_add_role_pts() function based on your tracked items
    * adjust the numbers in the assert statements if selecting an answer choice does not only increase that tracked item by 1 point (e.g. a choice that increases docile personality level by 2 and hasty by 4)

## Project Inspiration
I wanted to do a project that focuses on using classes, so I can practice object-oriented programming. Alongside that, I also wanted to practice creating functions that do only one thing and making more readable, organized code. While brainstorming, I remembered that I sometimes have trouble deciding what role to pick in games that include them, so this idea came to mind.