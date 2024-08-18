import xml.sax
from quiz import *
from enum import Enum, unique

@unique
class QuizParserState(Enum):
    IDLE = 0
    PARSE_QUIZ = 1
    PARSE_DESCRIPTION = 2
    PARSE_QUESTION = 3
    PARSE_QUEST_TEXT = 4
    PARSE_ANSWER = 5

class QuizParser(xml.sax.ContentHandler):

    def __init__(self):
        self.new_quiz = Quiz()
        self.new_quiz.description = ''  # Ensure description is initialized
        self._parse_state = QuizParserState.IDLE
        self._current_question = None
        self._current_answer = None

    def parse_quiz(self, quizpath):
        quiz_text = ''

        with open(quizpath, 'r') as file:
            if file.mode == 'r':
                quiz_text = file.read()
        
        xml.sax.parseString(quiz_text, self)

        return self.new_quiz
    
    def startElement(self, tagname, attrs):
        if tagname == "QuizML":
            self._parse_state = QuizParserState.PARSE_QUIZ
            self.new_quiz.name = attrs.get('name', '')

        elif tagname == "Description":
            self._parse_state = QuizParserState.PARSE_DESCRIPTION

        elif tagname == "Question":
            self._parse_state = QuizParserState.PARSE_QUESTION
            if attrs.get('type') == 'multichoice':
                self._current_question = QuestionMCQs()
            elif attrs.get('type') == 'tf':
                self._current_question = QuestionTF()
            try:
                self._current_question.points = int(attrs.get('points', 0))
            except Exception as e:
                print(f"Error parsing points: {e}")
            self.new_quiz.total_point += self._current_question.points

        elif tagname == "QuestionText":
            self._parse_state = QuizParserState.PARSE_QUEST_TEXT
            self._current_question.correct_answer = attrs.get('answer', '')
    
        elif tagname == "Answer":
            self._current_answer = Answer()
            self._current_answer.name = attrs.get('name', '')
            self._parse_state = QuizParserState.PARSE_ANSWER
    
    def endElement(self, tagname):
        if tagname == "QuizML":
            self._parse_state = QuizParserState.IDLE

        elif tagname == "Description":
            self._parse_state = QuizParserState.PARSE_QUIZ

        elif tagname == "Question":
            if self._current_question:
                self.new_quiz.questions.append(self._current_question)
            self._parse_state = QuizParserState.PARSE_QUIZ

        elif tagname == "QuestionText":
            self._parse_state = QuizParserState.PARSE_QUESTION

        elif tagname == "Answer":
            if self._current_question:
                self._current_question.answers.append(self._current_answer)
            self._parse_state = QuizParserState.PARSE_QUESTION
             
    def characters(self, chars):
        if self._parse_state == QuizParserState.PARSE_DESCRIPTION:
            self.new_quiz.description += chars

        elif self._parse_state == QuizParserState.PARSE_QUEST_TEXT:
            if self._current_question:
                self._current_question.text += chars

        elif self._parse_state == QuizParserState.PARSE_ANSWER:
            if self._current_answer:
                self._current_answer.text += chars
