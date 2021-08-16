from guizero import App, Text,TextBox, PushButton, Box, Window
from leaderboard import leaderboard, name_score_sort_change, sort_order_change
from questions import question_func, button_press, csv_append
from username_password import login
from random import randint
from question_list import question_list

counter = 1
used_questions = []
max_questions = len(question_list) - 1

def open_login():
  app.hide()
  login_window.show()


def close_login(guest = False):
  global username
  if (guest == True) or login(user_textbox.value, pass_textbox.value) == True  :
    username = user_textbox.value
    if guest == True: username = "guest"
    app.visible = True
    login_window.hide()
    first_question = randint(0,max_questions)
    used_questions.append(first_question)
    question_func(question_text, answer_1_but, answer_2_but, answer_3_but, answer_4_but, first_question, score_text) # CHANGE LAST NUMBER FOR DIF question
  else: output_text.value = "Invalid details"


def open_leaderboard():
  leaderboard_window.show()
  leaderboard_up()


def close_leaderboard():
  leaderboard_window.hide()


def leaderboard_up():
  leaderboard_text_1.value, leaderboard_text_2.value, leaderboard_text_3.value, leaderboard_text_4.value = leaderboard()
  

def leaderboard_name_change():
  name_score_sort_change()
  if name_sort_but.bg == "green": name_sort_but.bg = "#F5F5DC"
  else: name_sort_but.bg = "green"
  leaderboard_up()
  

def leaderboard_sort_change():
  sort_order_change()
  if sort_order_but.bg == "green": sort_order_but.bg = "#F5F5DC"
  else: sort_order_but.bg = "green"
  leaderboard_up()


def quiz_button_press(answer):
  button_press(answer, answer_1_but, answer_2_but, answer_3_but, answer_4_but, score_text)
  disable_toggle()
  answer_1_but.after(1000, quiz_button_reset) # 100 for testing, 2000 for finished?


def quiz_button_reset():
  global username
  disable_toggle()
  global counter
  if counter < 10:
    current_question = randint(0,max_questions)
    while current_question in used_questions:
      current_question = randint(0,max_questions)
    used_questions.append(current_question)
    question_func(question_text, answer_1_but, answer_2_but, answer_3_but, answer_4_but, current_question, score_text)
    counter += 1 
    question_count.value = (f"Question {counter}/10")
    answer_1_but.bg = "#F5F5DC"
    answer_2_but.bg = "#F5F5DC"
    answer_3_but.bg = "#F5F5DC"
    answer_4_but.bg = "#F5F5DC"
  elif counter == 10:
    csv_append(username)
    disable_toggle()
	  

def disable_toggle():
  if answer_1_but.enabled == True:
    answer_1_but.disable(); answer_2_but.disable(); answer_3_but.disable(); answer_4_but.disable()
  else: answer_1_but.enable(); answer_2_but.enable(); answer_3_but.enable(); answer_4_but.enable()

  
# I think each window needs a unique name and open/close function
# Needs = since you're changing the value of parameters, capital T in title caused error
app = App(title = "Quiz", width = 500, height = 400, visible = False, bg="#F5F5DC")
login_window = Window(app, title="Login window", width = 400, height = 220, bg="#F5F5DC") 
leaderboard_window = Window(app, title="Leaderboard window", width = 500, height = 400, bg="#F5F5DC") 
close_leaderboard()


# Login window
output_text = Text(login_window, text = " ")
box_textbox = Box(login_window, border = True, layout = "grid")
user_textbox = TextBox(box_textbox, width = 20, grid = [1,0])
user_text = Text(box_textbox, text = "Username:", grid = [0,0])
pass_text = Text(box_textbox, text = "Password:", grid = [0,2])
pass_textbox = TextBox(box_textbox, width = 20, grid = [1,2], hide_text=True)
user_textbox.bg = "white"
pass_textbox.bg = "white"
close_login_button = PushButton(login_window, text = "Login", command = close_login, width = 13)
guest_login_button = PushButton(login_window, text = "Guest login", command = lambda:close_login(True), width = 13)
login_open_leader_button = PushButton(login_window, text = "Leaderboard", command = open_leaderboard, width = 13)


# Quiz
score_text = Text(app, text = "\n\nScore: 0 | 0%")
question_count = Text(app, text = "Question 1/10:")
question_text = Text(app,text = "")
answer_1_but = PushButton(app, text = "Answer 1", command = lambda:quiz_button_press("1"))
answer_2_but = PushButton(app, text = "Answer 2", command = lambda:quiz_button_press("2"))
answer_3_but = PushButton(app, text = "Answer 3", command = lambda:quiz_button_press("3"))
answer_4_but = PushButton(app, text = "Answer 4", command = lambda:quiz_button_press("4"))
main_open_leader_button = PushButton(app, text = "Leaderboard", command = open_leaderboard, align = "bottom")


# Leaderboard
# Creates new text object and fills with the return of the leaderboard function
leaderboard_options = Box(leaderboard_window, border = True)
# leaderboard_up_box = Box(leaderboard_window, border = True)
leaderboard_box = Box(leaderboard_window, border = True)
leaderboard_text_1 = Text(leaderboard_box, align = "left")
leaderboard_text_2 = Text(leaderboard_box, align = "left")
leaderboard_text_3 = Text(leaderboard_box, align = "left")
leaderboard_text_4 = Text(leaderboard_box, align = "left")
leaderboard_text_1.value, leaderboard_text_2.value, leaderboard_text_3.value, leaderboard_text_4.value = leaderboard()


name_sort_but = PushButton(leaderboard_options, text = "Sort by name", command = leaderboard_name_change, align = "left")
sort_order_but = PushButton(leaderboard_options, text = "Reverse sort order", command = leaderboard_sort_change, align = "left")
# update_leaderboard_but = PushButton(leaderboard_up_box, text = "Update leaderboard", command = leaderboard_up, align = "bottom")


close_leaderboard_button = PushButton(leaderboard_window, text = "Close", command = close_leaderboard)


app.display()
open_login()