import time

questions = [
    "What is the largest planet in our solar system?",
    "In what year did the Titanic sink?",
    "What is the capital city of Japan?",
    "Which element has the chemical symbol 'O'?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the tallest mountain in the world?",
    "Which continent is the Sahara Desert located on?",
    "How many continents are there on Earth?",
    "What is the smallest country in the world by land area?",
    "Who painted the Mona Lisa?"
]

answer_options = [
    "a) Mars    b) Earth    c) Jupiter    d) Venus",
    "a) 1905    b) 1910    c) 1912    d) 1915",
    "a) Beijing    b) Seoul    c) Bangkok    d) Tokyo",
    "a) Hydrogen    b) Oxygen    c) Carbon    d) Nitrogen",
    "a) Charles Dickens    b) Jane Austen    c) William Shakespeare    d) Mark Twain",
    "a) K2    b) Mount Kilimanjaro    c) Mount Fuji    d) Mount Everest",
    "a) Asia    b) Africa    c) South America    d) Australia",
    "a) Six    b) Seven    c) Five    d) Eight",
    "a) Monaco    b) Malta    c) Vatican City    d) San Marino",
    "a) Vincent van Gogh    b) Pablo Picasso    c) Leonardo da Vinci    d) Claude Monet"
]

answers = [
    "Jupiter",
    "1912",
    "Tokyo",
    "Oxygen",
    "William Shakespeare",
    "Mount Everest",
    "Africa",
    "Seven",
    "Vatican City",
    "Leonardo da Vinci"
]

def quiz():
    marks_obtained = 0

    print("A wild wizard appears!")
    time.sleep(2.5)
    print('"You will be graded."\n')
    time.sleep(2)

    for i in range(len(questions)):
        print(f"{questions[i]} \n {answer_options[i]}")
        user_ans = input("Your answer? ")

        if user_ans == answers[i]:
            print("+1\n\n")
            marks_obtained += 1
        else:
            print("lol noob\n\n")
        
        time.sleep(2)

    print(f"Total Marks: {marks_obtained}")
    if marks_obtained >= 7:
        print("Your stick is bigger than mine")
    elif marks_obtained >= 5:
        print("ur bad")
    elif marks_obtained >= 1:
        print("go back to school")
    
quiz()
