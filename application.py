from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def landing_page():
    """Shows a landing page."""

    return render_template("landing.html")
    # Renders landing.html as a homepage

    #################################################################
    # I created a landing.html template that includes a link to the next
    # page by using a Jinja template that extends from a base.html template.
    # This replaces the hard-coded HTML that was original in the return
    # line. 

@app.route("/application_form")
def application_form():
    """Show the application form"""

    return render_template("application-form.html")
    # Renders application-form.html

    ##################################################################
    # This serves the template application-form.html at the route 
    # /application-form. As instructed, I used application-form.html created 
    # in the HTML-CSS assessment.  

@app.route("/application", methods=["POST"])
def application():
    """Show submission confirmation"""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.form.get("salary")
    desired_role = request.form.get("desiredrole")
    # Used the form.get method for POST to retrieve the entries made on 
    # /application_form

    return render_template("confirmation.html", 
                                    first_name=first_name,
                                    last_name=last_name,
                                    salary=salary,
                                    desired_role=desired_role)
    # Renders confirmation.html; Jinja template variables set immediately 
    # after the .html file name

    ##################################################################
    # The confirmation.html template extends from the base.html template

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

