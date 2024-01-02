# Create a Python program for an online quiz system. Implement classes for
# quizzes, questions, and users. Include methods for taking quizzes, scoring, and
# displaying results.

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def display(self):
        print(self.text)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def is_correct(self, user_answer):
        return user_answer == self.correct_option


class TechQuiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def take_quiz(self):
        score = 0
        for question in self.questions:
            question.display()
            user_answer = int(input("Your answer: "))
            if question.is_correct(user_answer):
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        return score


class TechUser:
    def __init__(self, name):
        self.name = name

    def take_quiz(self, quiz):
        print(f"{self.name}, you are taking the {quiz.name} quiz.")
        score = quiz.take_quiz()
        print(f"{self.name}, your score: {score} out of {len(quiz.questions)}")


def main():
    # Create technology quiz questions
    question1 = Question("\nWhat is the capital of Silicon Valley?", ["San Francisco", "San Jose", "Mountain View"], 2)
    question2 = Question("\nWhich programming language is known for its use in data science?", ["Java", "Python", "C++"], 2)
    question3 = Question("\nWhat does 'API' stand for?", ["Application Programming Interface", "Advanced Program Integration", "Automated Processing Interface"], 1)

    tech_quiz = TechQuiz("Tech Knowledge", [question1, question2, question3])

    user = TechUser("\nTechEnthusiast")


    user.take_quiz(tech_quiz)


if __name__ == "__main__":
    main()
