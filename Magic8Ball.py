#Magic8Ball.py
#Name: Miguel Alvarado
#Date: 1/29/2026
#Assignment: Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
 print("Magic 8 Ball")
  #Prompt the user for their question.
 print("Hello" +"!")
 print("Ask me any question and I'll decide your fate")
 input("")
 
 answers = ["nah", "are we serious right now bro?", "As I see it, yes", "You may rely on it","maybe",
             "mmmm I'll think about it later","Very doubtful", "Yesss bro", "Noooooooo", 
             "don't get your hopes up bud", "Most likely", "Most likely not"]

  #Answer question randomly with one of the options from your earlier list.
 response = random.choice(answers)
 print(response)

if __name__ == '__main__':
  main()
