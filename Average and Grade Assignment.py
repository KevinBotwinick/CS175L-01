#CS-175L-01
#Kevin Botwinick
#Average and Grade Assignment
def main():
    score1 = float(input("Enter score 1: "))
    score2 = float(input("Enter score 2: "))
    score3 = float(input("Enter score 3: "))
    score4 = float(input("Enter score 4: "))
    score5 = float(input("Enter score 5: "))
    return [score1, score2, score3, score4, score5]


def determine_grade(num):
    if 90 <= num <= 100:
        letter_grade = "A"
    elif 80 <= num <= 89:
        letter_grade = "B"
    elif 70 <= num <= 79:
        letter_grade = "C"
    elif 60 <= num <= 69:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade


def calc_average(grades):
    average = sum(grades) / len(grades)
    grade = determine_grade(average)
    print("Average Score: \t {:.1f}  \t\t\t {}".format(average, grade))



def show_letters(num, letter_grade):

    print("Score: \t\t {:.1f} \t\t\t {}".format(num, letter_grade))

def repeat():
        restart = input("Enter (yes) if you would like to do another calculation: ")
        while restart == "yes":
            score1 = float(input("Enter score 1: "))
            score2 = float(input("Enter score 2: "))
            score3 = float(input("Enter score 3: "))
            score4 = float(input("Enter score 4: "))
            score5 = float(input("Enter score 5: "))
            return calc_average(grades)
            return determine_grade(num)
        else:
            if restart == "no":
                print("Goodbye")
                return
            
            
            
    


lst = main()
print("\nScore \t\t Numeric Grade \t\t Letter Grade")
print("--------------------------------------------------------")
for n in lst:
    show_letters(n, determine_grade(n))
print("--------------------------------------------------------")
calc_average(lst)
repeat()


        
    




































































