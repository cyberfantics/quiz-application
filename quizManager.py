import os.path
import os
import quizParser
import datetime

class QuizManager:
    def __init__(self, quizfolder):
        self.quizfolder = quizfolder

        # TODO: The most recently selected quiz
        self.thequiz = None 

        # TODO: InitiliZe the collection of quizes 
        self.quizzes = dict()

        # TODO: Store the result of most recent quizzes
        self.results = None

        # TODO: The name of the person taking quiz
        self.quiz_taker = None

        # TODO: Make sure the quiz folder exist
        if os.path.exists(self.quizfolder) == False:
            raise FileNotFoundError("The Quiz Folder Does Not exists")
        
        # TODO: Build the list of quizzes
        self._build_quiz_list()

    def _build_quiz_list(self):
        dircontects = os.scandir(self.quizfolder)

        # TODO: Parse the XML File in the directory
        for i, f in enumerate(dircontects):
            if f.is_file():
                parser = quizParser.QuizParser()
                self.quizzes[i+1] = parser.parse_quiz(f)

    
    # TODO: Print a list of currently installed quizzes
    def list_quizzes(self):
        
        for key, value in self.quizzes.items():
            print(f'{key}: {value.name}')
           


    # TODO: Start the given quiz for the user and return the result
    def take_quiz(self, quizid, username):
        pass

    # TODO: Print the result of most recently taken quizzes
    def print_results(self):
        pass

    # TODO: Save the result of most recently taken quiz to a file.
    def save_result(self):
        pass 


if __name__=="__main__":
    quiz = QuizManager("Quizzes")
    quiz.list_quizzes()