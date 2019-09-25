from flask import Flask, request, render_template
# validate pulls in the functions required to validate all userinputs
from validate import validate, validate_email, verify_password, verify_all
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['GET'])
def index():
  # this displays the form from the templates/base.html file and removes html from error returns
  encoded_error = request.args.get("error")
  form = render_template("init.html", error=encoded_error and cgi.escape(encoded_error, quote=True))
  return form


@app.route("/", methods=['POST'])
def index_post():
  # after clicking submit, request.form pulls userinput from form input id, validate functions enforces userinput rules, cgi.escape limits html within userinput, the return validation and escape is passed to named variable 
  form = render_template("init.html")
  uname = validate(request.form['uname'])
  email = validate_email(request.form['email'])
  password = validate(request.form['pass'])
  verify = validate(request.form['verify'])
  matched = verify_password(password, verify)
  # calls functin that tests each input for validity, all must pass
  if verify_all(form, uname, password, verify, email, matched) == "SUCCESS":
    return welcome()
  # this is if they dont
  if verify_all(form, uname, password, verify, email, matched) != "SUCCESS":
    verify_all_fail = verify_all(form, uname, password, verify, email, matched)
    return verify_all_fail
  
# the welcome page, all inputs must be verified to reach this page
@app.route("/welcome")
def welcome():
  uname = request.form['uname']
  return "<p>WELCOME <b>" + uname + "</b></p>" + "<br>" + "*your account has been created successfully!*"

# default local host server for running webpage at http://127.0.0.1:8080
app.run(host='0.0.0.0', port=8080)