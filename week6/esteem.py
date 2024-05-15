
def get_input(prompt, type):
    print(prompt)
    answer = input("Enter D, d, a, or A: ")
    if type:
        score_dict = {"D": 0, "d": 1, "a": 2, "A": 3}
    else:
        score_dict = {"D": 3, "d": 2, "a": 1, "A": 0}
    return score_dict[answer]
    
def compute_score(list):
    return sum(list)

def main():
    print("""
This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:
          
D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.
          """)
    
    answers = [""] * 10

    answers[0] = get_input("I feel that I am a person of worth, at least on an equal plane with others.", 1)
    answers[1] = get_input("I feel that I have a number of good qualities.", 1)
    answers[2] = get_input("All in all, I am inclined to feel that I am a failure.", 0)
    answers[3] = get_input("I am able to do things as well as most other people.", 1)
    answers[4] = get_input("I feel I do not have much to be proud of.", 0)
    answers[5] = get_input("I take a positive attitude toward myself.", 1)
    answers[6] = get_input("On the whole, I am satisfied with myself.", 1)
    answers[7] = get_input("I wish I could have more respect for myself.", 0)
    answers[8] = get_input("I certainly feel useless at times.", 0)
    answers[9] = get_input("At times I think I am no good at all.", 0)

    score = compute_score(answers)
    print(f"Score: {score}")
    if score < 15:
        print("get some help")
    else:
        print("Your fine, but tutoring is free so use it anyway.")

main()