from tkinter import *
import tkinter.font as font
import random

root = Tk()
root.title("Rock Paper Scissors")
app_font = font.Font(size = 12)
root.config(bg = '#FFFFFF')
root.geometry('700x300')

player_score = 0
computer_score = 0
options = [('rock', 0), ('paper', 1), ('scissors', 2)]

Label(text = 'Rock Paper Scissors', font = font.Font(size = 20), bg = '#FFFFFF').pack()

def player_choice(player_input):
    global player_score, computer_score

    computer_input = get_computer_choice()

    player_choice_label.config(text = 'You : ' + player_input[0])
    computer_choice_label.config(text = 'Computer : ' + computer_input[0])

    if player_input == computer_input:
        winner_label.config(text = "Tie")
    elif (player_input[1]-computer_input[1]) % 3 == 1:
        player_score += 1
        winner_label.config(text="You Won!!!")
        player_score_label.config(text = 'You : ' + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text="Computer Won!!!")
        computer_score_label.config(text='Computer : ' + str(computer_score))

def get_computer_choice():
    return random.choice(options)

winner_label = Label(text = "Select anyone to start...", bg = '#FFFFFF', font = font.Font(size = 13), pady = 8)
winner_label.pack()

input_frame = Frame(root, bg = '#FFFFFF')
input_frame.pack()

player_options = Label(input_frame, text = "Your Options : ", font = app_font, fg = 'grey', bg = '#FFFFFF')
player_options.grid(row = 0, column = 0, pady = 8)

rock_btn = Button(input_frame, text = 'Rock', width = 15, bd = 0, bg = 'pink', pady = 5, command = lambda: player_choice(options[0]))
rock_btn.grid(row = 1, column = 1, padx = 8, pady = 5)

paper_btn = Button(input_frame, text = 'Paper', width = 15, bd = 0, bg = 'silver', pady = 5, command = lambda: player_choice(options[1]))
paper_btn.grid(row = 1, column = 2, padx = 8, pady = 5)

scissors_btn = Button(input_frame, text = 'Scissors', width = 15, bd = 0, bg = 'light blue', pady = 5, command = lambda: player_choice(options[2]))
scissors_btn.grid(row = 1, column = 3, padx = 8, pady = 5)

score_label = Label(input_frame, text = 'Score : ', font = app_font, fg = 'grey', bg = '#FFFFFF')
score_label.grid(row = 2, column = 0)

player_choice_label = Label(input_frame, text = 'You : ---', font = app_font, bg = '#FFFFFF')
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(input_frame, text = 'You : 0', font = app_font, bg = '#FFFFFF')
player_score_label.grid(row = 3, column = 2, pady = 5)

computer_choice_label = Label(input_frame, text = 'Computer : ---', font = app_font, fg = 'black', bg = '#FFFFFF')
computer_choice_label.grid(row = 4, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = 'Computer : 0', font = app_font, fg = 'black', bg = '#FFFFFF')
computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)

root.mainloop()