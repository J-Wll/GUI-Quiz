from datetime import date
from question_list import question_list


today = date.today()
today_2 = today.strftime("%d/%m/%Y") # Date test taken
score = 0

def question_func(question_text, answer_1_but, answer_2_but, answer_3_but, answer_4_but, question, score_text, question_list = question_list, score = 0, ):
  global correct
  correct = question_list[question][2][0]
  
  question_text.value = question_list[question][0][0]
  answer_1_but.text = question_list[question][1][0]
  answer_2_but.text = question_list[question][1][1]
  answer_3_but.text = question_list[question][1][2]
  answer_4_but.text = question_list[question][1][3]


def button_press(answer, answer_1_but, answer_2_but, answer_3_but, answer_4_but, score_text):
  # answer 1 2 3 or 4
  if answer == "1": answer_check(answer_1_but, "A",answer_1_but, answer_2_but, answer_3_but, answer_4_but, score_text)
  if answer == "2": answer_check(answer_2_but, "B",answer_1_but, answer_2_but, answer_3_but, answer_4_but, score_text)
  if answer == "3": answer_check(answer_3_but, "C",answer_1_but, answer_2_but, answer_3_but, answer_4_but, score_text)
  if answer == "4": answer_check(answer_4_but, "D",answer_1_but, answer_2_but, answer_3_but, answer_4_but, score_text)


def answer_check(button, letter, answer_1_but, answer_2_but, answer_3_but, answer_4_but, score_text):
  global score
  if letter == correct:
    button.bg = "green"
    score += 1
    score_text.value = f"Score: {score} | {score*10}%"
  else:
    button.bg = "red"
    score_text.value = f"Score: {score} | {score*10}%"


def csv_append(player_name):
  global score
  file = open("scores.txt", "a")
  to_write = player_name + " " + str(score) + " " + str(today_2) + "\n"
  file.write(to_write)
  file.close()
  # Opens csv, appends name and score with correct formatting