from flask import request
import re
import cgi

# function to validate username, password, and verify testing each against 6 conditions
def validate(userinput):
  int_var = 0
  while True:   
    if(len(userinput)<=3 or len(userinput)>20):
      int_var = -1
      break
    elif re.search("\s", userinput):
      int_var = -2
      break
    elif not re.search("[a-z]", userinput): 
      int_var = -3
      break
    elif not re.search("[A-Z]", userinput): 
      int_var = -4
      break
    elif not re.search("[0-9]", userinput): 
      int_var = -5
      break
    elif re.search("[<>/]", userinput):
      int_var = -6
      break
    else:
      int_var = 0
      break

  # after error for invalid character is detected in the above conditions, cgi.escape forces html into  plain text formatting
  userinput = cgi.escape(userinput)

  # after testing each condition, return the appropriate response
  if int_var == -1:
    return userinput +  " ** (Must contain 4-20 characters) **" + "<br>"
  elif int_var == -2:
    return userinput + " ** (Cannot contain spaces) **" + "<br>"
  elif int_var == -3:
    return userinput + " ** (No lowercase characters were found) **" + "<br>"
  elif int_var == -4:
    return userinput + " ** (No uppercase characters were found) **" + "<br>"
  elif int_var == -5:
    return userinput + " ** (Use a number between 0-9) **" + "<br>"
  elif int_var == -6:
    return userinput + " ** (Invalid characters '<>/') **" + "<br>"
  else:
    return userinput + "<br>"


# seperate function for validating email, email is tested against 5 conditions
def validate_email(userinput):
  int_var = 0
  while True:
    if(len(userinput)==0):
      int_var = 0
      break
    if(len(userinput)<=3 or len(userinput)>30):
      int_var = -1
      break
    elif re.search("\s", userinput):
      int_var = -2
      break
    elif not re.search("[@]", userinput):
      int_var = -3
      break
    elif not re.search("[.]", userinput):
      int_var = -3
      break
    elif re.search("[<>/]", userinput):
      int_var = -4
      break
    else:
      int_var = 0
      break

  # after error for invalid character is detected in the above conditions, cgi.escape forces html into  plain text formatting
  userinput = cgi.escape(userinput)

  # after testing each condition, return the appropriate response
  if int_var == -1:
    return userinput + " ** (Must contain 4-30 characters) **" + "<br>"
  elif int_var == -2:
    return userinput + " ** (Cannot contain spaces) **" + "<br>"
  elif int_var == -3:
    return userinput + " ** (Missing the '@' symbol or '.com' extension) **" + "<br>"
  elif int_var == -4:
    return userinput + " ** (Invalid characters '<>/') **" + "<br>"
  else:
    return userinput + "<br>"


# funciton to test first password against the second password typed in by the user
def verify_password(password, ver_password):
  if password != ver_password:
    return " ** (Password Verification: FAILED) **" + "<br>"
  elif password == ver_password:
    return " ** (Password Verification: SUCCESS) **" + "<br>"

# function to check if all inputs are within tested conditions
def verify_all(form, uname, password, verify, email, matched): 
  # if all inputs meet the conditions, return text 'SUCCESS' to be tested after return
  if uname == request.form['uname'] + "<br>" and verify == request.form['pass'] + "<br>" and email == request.form['email'] + "<br>" and matched == " ** (Password Verification: SUCCESS) **" + "<br>":
    return "SUCCESS"
  # if one input fails to meet the conditions, display error and allow reentry
  else:
    content = form + '<div id="error">' + uname + " " + password + " " + verify + " " + matched + " " + email + "</div>"
    return content