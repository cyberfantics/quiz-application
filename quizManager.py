import os.path
import os
import quizParser
import datetime

# ANSI escape codes for colors
COLORS = {
    'info': '\033[94m',    # Blue
    'success': '\033[92m', # Green
    'warning': '\033[93m', # Yellow
    'error': '\033[91m',   # Red
    'endc': '\033[0m'      # End color
}

class QuizManager:
    def __init__(self, quizfolder):
        self.quizfolder = quizfolder

        # The most recently selected quiz
        self.thequiz = None 

        # Initialize the collection of quizzes 
        self.quizzes = dict()

        # Store the result of most recent quizzes
        self.results = None

        # The name of the person taking the quiz
        self.quiz_taker = None

        # Make sure the quiz folder exists
        if not os.path.exists(self.quizfolder):
            raise FileNotFoundError(f'{COLORS["error"]}The Quiz Folder Does Not Exist{COLORS["endc"]}')
        
        # Build the list of quizzes
        self._build_quiz_list()

    def _build_quiz_list(self):
        dircontents = os.scandir(self.quizfolder)

        # Parse the XML files in the directory
        for i, f in enumerate(dircontents):
            if f.is_file():
                parser = quizParser.QuizParser()
                self.quizzes[i+1] = parser.parse_quiz(f)

    # Print a list of currently installed quizzes
    def list_quizzes(self):
        if not self.quizzes:
            print(f'{COLORS["warning"]}No quizzes available.{COLORS["endc"]}')
            return
        
        print(f'{COLORS["info"]}Available Quizzes:{COLORS["endc"]}')
        for key, value in self.quizzes.items():
            print(f'{COLORS["info"]}{key}: {value.name}{COLORS["endc"]}')

    # Start the given quiz for the user and return the result
    def take_quiz(self, quizid, username):
        if quizid not in self.quizzes:
            print(f'{COLORS["error"]}Quiz ID not found.{COLORS["endc"]}')
            return

        self.quiz_taker = username
        self.thequiz = self.quizzes[quizid]
        self.results = self.thequiz.take_quiz()

    # Print the result of most recently taken quiz
    def print_results(self):
        if not self.thequiz:
            print(f'{COLORS["warning"]}No quiz has been taken yet.{COLORS["endc"]}')
            return

        self.thequiz.print_result(self.quiz_taker)

    # Save the result of the most recently taken quiz to a file
    def save_result(self):
        if not self.thequiz:
            print(f'{COLORS["warning"]}No quiz has been taken yet.{COLORS["endc"]}')
            return

        today = datetime.datetime.today()
        file_name = f'Quiz_{today.year}_{today.month}_{today.day}.txt'

        count = 1
        while os.path.exists(file_name):
            file_name = f'Quiz_{today.year}_{today.month}_{today.day}_{count}.txt'
            count += 1

        with open(file_name, 'w') as file:
            self.thequiz.print_result(self.quiz_taker, file)

if __name__ == "__main__":
    quiz = QuizManager("Quizzes")
    quiz.list_quizzes()
