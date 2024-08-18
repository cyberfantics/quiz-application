import datetime
import sys
import random

# ANSI escape codes for colors
COLORS = {
    'header': '\033[95m',  # Magenta
    'info': '\033[94m',    # Blue
    'success': '\033[92m', # Green
    'warning': '\033[93m', # Yellow
    'error': '\033[91m',   # Red
    'endc': '\033[0m'      # End color
}

# Implement Question Class
class Question:
    def __init__(self):
        # Define the Question Fields
        self.points = 0
        self.correct_answer = ''
        self.text = ''
        self.is_correct = False

# Inherit Question Class Into True False Class
class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while True:
            print(f'{COLORS["info"]}(T)rue or (F)alse: {self.text}{COLORS["endc"]}')
            response = input("? ")

            # Check to see if no response was entered
            if len(response) == 0:
                print(f'{COLORS["warning"]}Not a valid Response, Continue{COLORS["endc"]}')
                continue

            # Check to see if either T or F was given
            if response[0].lower() not in ('t', 'f'):
                print(f'{COLORS["warning"]}Not a valid Response, Continue{COLORS["endc"]}')
                continue

            # Mark this question as correct, if answered correctly
            if response[0].lower() == self.correct_answer:
                self.is_correct = True

            break

# Inherit Question Class Into MCQs Class
class QuestionMCQs(Question):
    def __init__(self):
        super().__init__()
        # Define the answer for asking question
        self.answers = []

    def ask(self):
        while True:
            print(f'{COLORS["info"]}{self.text}{COLORS["endc"]}')
            for a in self.answers:
                print(f"({a.name}). {a.text}")
            response = input("? ")

            # Check to see if no response was entered
            if len(response) == 0:
                print(f'{COLORS["warning"]}Not a valid Response, Continue{COLORS["endc"]}')
                continue

            # Mark this question as correct, if answered correctly
            if response[0].lower() == self.correct_answer:
                self.is_correct = True

            break

# Answer Class For Multiple Choice Question
class Answer():
    def __init__(self):
        self.text = ''
        self.name = ''

# Implement Quiz Class
class Quiz():
    def __init__(self):
        # Define the quiz properties
        self.name = ''
        self.description = ''
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_point = 0
        self.completiontime = 0

    def print_header(self):
        print(f'''
        {COLORS["header"]}
        ----------------------------------------------------
               Quiz Name: {self.name}
        Quiz Description: {self.description}
               Questions: {len(self.questions)}
            Total Points: {self.total_point}
        ----------------------------------------------------
        {COLORS["endc"]}
        ''')

    def print_result(self, quiztaker, fileToSave=sys.stdout):
        print(f'''
            {COLORS["success"]}
            *********************************************************************
            RESULTS FOR {quiztaker}
            Date: {datetime.datetime.today()}
            Elapsed Time: {self.completiontime}
            Questions: {self.correct_count} OUT of {len(self.questions)} correct
            SCORE: {self.score} points out of possible {self.total_point} points        
            **********************************************************************
            {COLORS["endc"]}
            ''', file=fileToSave, flush=True)

    def take_quiz(self):
        # Initialize the quiz state
        self.score = 0
        self.correct_count = 0
        for q in self.questions:
            q.is_correct = False

        # Print the header
        self.print_header()

        # Randomize the questions
        random.shuffle(self.questions)

        # Start quiz
        start_time = datetime.datetime.now()

        # Execute each question and record the result
        for q in self.questions:
            q.ask()
            if q.is_correct:
                self.correct_count += 1
                self.score += q.points

        print(f'{COLORS["info"]}-----------------------------------{COLORS["endc"]}\n')

        # End time
        end_time = datetime.datetime.now()

        # Ask if user wants to retry wrong questions
        if self.correct_count != len(self.questions):
            redo = input(f'{COLORS["warning"]}Looks like you missed some questions,\nWant to redo? (y/n){COLORS["endc"]}')
            if redo[0].lower() == 'y':
                wrong_q = [q for q in self.questions if not q.is_correct]

                # Execute each wrong question and record the result
                for q in wrong_q:
                    q.ask()
                    if q.is_correct:
                        self.correct_count += 1
                        self.score += q.points

                print(f'{COLORS["info"]}-----------------------------------{COLORS["endc"]}\n')
                # End time
                end_time = datetime.datetime.now()

        self.completiontime = end_time - start_time
        self.completiontime = datetime.timedelta(seconds=round(self.completiontime.total_seconds()))
        # Return the result
        return (self.score, self.correct_count, self.total_point)
