def login(username, password):
  login_details = []
  file = open("login_details.txt", "r") # checks username/pw against the existing names in the login_details file
  lines = file.readlines() # .readlines() splits the file into a list in login_details
  file.close()

  for line in lines:
    line = line.strip() # removes \n and whitespace
    login_details.append(line.split(",")) # split into username/password and added to the list login_details

  for x in login_details:
    if username.lower() == x[0] and password.lower() == x[1]:
      return True
      # if username and password match the file return true
  else:
    return False