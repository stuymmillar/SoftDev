from flask import Flask, render_template, request, session

app = Flask(__name__)
user_name = "john"
user_pass = "doe"
errors = []

@app.route('/')
def render_test():
    if session.get("john") != None:
        return "Welcome, John"
    #elif (request.args.get("username") =="john") and (request.args.get("password") =="doe"):
        #session["john"] = "doe"
        #return "Welcome, John"
    else:
        return render_template("login.html")

@app.route('/auth', methods=["GET", "POST"])
def authenticate():
    errors = []
    print(request.form)
    print(request.args)
    u_name = request.form.get("username")
    u_pass = request.form.get("password")
    print(errors)
    #print(u_name + ":username")
    #print(u_pass + ":password")
    if u_name != user_name:
        errors.append("Incorrect username")
    if u_pass != user_pass:
        errors.append("Incorrect password")
    if errors is not None:
        return render_template("login.html", errors=errors)
    else:
        session.add(u_name)
        return redirect(url_for('render_test'))

'''@app.route('/logout')
def logout():
    return "Success"
   ''' 
    
if __name__ == '__main__':
    app.debug = True
    app.run()
