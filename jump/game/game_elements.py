#game elements 
#game elements 
import random

word = ["the","bird","antelope"]

word= random.choice(word)
print()
for letter in range (0,len(word)):
    jumpman_word = []
    letter = "_ "
    print (letter, end='')
    jumpman_word.append(letter)


selected_word = word
print()
player_choice = input("What letter do you want to choose? ")
print()

# if player_choice in word:
#     print("correct")
#     jumpman_word.append(player_choice)
# else: 
#     print ("incorrect")

# print(jumpman_word)



# index_value = selected_word.index(player_choice)
# if index_value == selected_word.index(player_choice):
#     if player_choice in selected_word:
#         print("correct")
# elif player_choice not in selected_word:
#     print("incorrect")