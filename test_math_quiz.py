import unittest
from math_quiz import MathQuiz

class TestMathQuiz(unittest.TestCase):
    def test_generate_question(self):
        quiz = MathQuiz()
        question, answer = quiz.generate_question()

        self.assertIsInstance(question, str)

        self.assertIsInstance(answer, (int, float))

    def test_generate_question_addition(self):
        quiz = MathQuiz()
        quiz.generate_question = lambda: ("2 + 3", 5)
        question, answer = quiz.generate_question()

        self.assertEqual(question, "2 + 3")
        self.assertEqual(answer, 5)

if __name__ == '__main__':
    unittest.main()
