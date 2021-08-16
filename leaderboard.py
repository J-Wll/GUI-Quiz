from datetime import date


sort_order = True
lambda_sort_key = 1
today = date.today()
today_2 = today.strftime("%d/%m/%Y") # Date test taken


from random import randint, choice
from string import ascii_letters


# For a button toggle, change sort order will effect is the sort is reversed or not
def sort_order_change():
  global sort_order
  if sort_order == True: sort_order = False
  elif sort_order == False: sort_order = True


# Changing the key to 0 will target the name, sorting alphabetically
def name_score_sort_change():
  global lambda_sort_key
  if lambda_sort_key == 1: lambda_sort_key = 0
  elif lambda_sort_key == 0: lambda_sort_key = 1 
  sort_order_change()


def leaderboard():
  counter = 0
  global sort_order, lambda_sort_key
  file = open("scores.txt")
  scores = file.readlines()
  file.close()

  name_score_list, neat_print = [],""

  for score in scores: # List without formatting
    name_score_list.append(score.strip().split(" "))

  type_check = int # To avoid trying to convert letters into numbers
  if lambda_sort_key == 0: type_check = str

  name_score_list = sorted(name_score_list, key=lambda num: type_check(num[lambda_sort_key]), reverse = sort_order) # Lambda sort with variables for the options

  # tab_print = []

  column_1, column_2, column_3, column_4 = " Name: \n"," Score: \n","    %:    \n","   Date:    \n"
  neat_print = neat_print + "Name" + "  " + "Score" +" "+   "%"   + " "+ "Date" + "\n"
  for score in name_score_list:    
    if counter == 10: break
    percent = int(score[1])*10
    neat_print = neat_print + (f"{score[0]}:  {score[1]} {str(percent)}% |{str(score[2])}|\n")
    column_1 = column_1 + (f"{score[0]}: \n")
    column_2 = column_2 + (f"{score[1]}\n")
    column_3 = column_3 + (f"{str(percent)}\n")
    column_4 = column_4 + (f"{str(score[2])}\n")

    # tab_print.append([score[0]] + [score[1]] + [str(percent)] + [str(score[2])])
    #  # tab print optional
    counter += 1 # Appends 10 scores to the leaderboard string neatly

  # leaderboard_headers = ["Name", "Score", "%", "Date"]
  # tab_print = tabulate(tab_print, headers = leaderboard_headers)

  return(column_1, column_2, column_3, column_4)

# populates list
# csv_append(list_pop(4), randint(0,10)) # random just for testing, normal format is csv_append(name, score)


