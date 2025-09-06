questions = [
    ["Who is Shahrukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],
    ["What is the capital of France?", "Berlin", "London", "Paris", "Madrid", 3],
    ["Which planet is known as the Red Planet?",
        "Earth", "Mars", "Jupiter", "Venus", 2],
    ["Who wrote 'Hamlet'?", "Charles Dickens",
        "William Shakespeare", "Mark Twain", "Jane Austen", 2],
    ["What is the largest mammal?", "Elephant",
        "Blue Whale", "Giraffe", "Hippopotamus", 2],
    ["Which element has the chemical symbol 'O'?",
        "Gold", "Oxygen", "Silver", "Iron", 2],
    ["What is the boiling point of water?", "50°C", "100°C", "150°C", "200°C", 2],
    ["Who painted the Mona Lisa?", "Vincent Van Gogh",
        "Leonardo da Vinci", "Pablo Picasso", "Claude Monet", 2],
    ["Which country is known as the Land of the Rising Sun?",
        "China", "Japan", "Thailand", "South Korea", 2],
    ["What is the smallest prime number?", "1", "2", "3", "5", 2],
    ["What is the chemical symbol for gold?", "Au", "Ag", "Gd", "Go", 1],
    ["Who discovered gravity?", "Albert Einstein",
        "Isaac Newton", "Galileo Galilei", "Nikola Tesla", 2],
    ["Which ocean is the largest?", "Atlantic", "Indian", "Arctic", "Pacific", 4],
    ["What is the hardest natural substance?",
        "Gold", "Iron", "Diamond", "Quartz", 3],
    ["Which language is used to create Android apps?",
        "Swift", "Java", "C++", "Ruby", 2],
    ["Who is known as the father of computers?", "Charles Babbage",
        "Alan Turing", "Bill Gates", "Steve Jobs", 1],
    ["What is the tallest mountain in the world?", "K2",
        "Mount Everest", "Kangchenjunga", "Lhotse", 2],
    ["Which organ purifies blood in the human body?",
        "Heart", "Liver", "Kidney", "Lungs", 3],
    ["What is the freezing point of water?", "0°C", "32°C", "100°C", "-10°C", 1],
    ["Who invented the telephone?", "Alexander Graham Bell",
        "Thomas Edison", "Nikola Tesla", "James Watt", 1],
]

prizes = (1000, 2000, 3000, 4000, 5000, 6000, 7000, 10000, 150000, 20000)


def initalize_game():
    prize_money = 0
    c = 0
    for question in questions:
        c += 1
        print(question[0])
        print(f"a. {question[1]}")
        print(f"b. {question[2]}")
        print(f"c. {question[3]}")
        print(f"d. {question[4]}")

        try:
            user_input = int(
                input("Enter your answer: 1 for a, 2 for b, 3 for c, 4 for d :\n  "))

            if (question[5] == user_input):
                print("!!CORRECT ANSWER!!\n\n")
                print(f"------------Total Correct Answers: {c}\n\n")
                prize_money = prizes[c//2]
            else:
                print(
                    f"Incorrect Answer.. Correct Answer is: {question[question[5]]}")
                print("Exiting game...")
                break
        except Exception as e:
            print("Wrong input. Exiting Game!!")
    print(f"Congratulations.. you have won ${prize_money}")


if __name__ == "__main__":
    initalize_game()
