from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

@app.route('/')
def the_greet():
    return render_template("hello.html")
# route to handle the landing page of a website.
@app.route('/next')
def show_game_form():
    person = request.args.get("person")
    return render_template("compliment.html",person=person)


#create a function called show_game_form to route to the url path /game
@app.route('/game')
def game_form():
    confirmplay = request.args.get("confirmplay")
    if confirmplay == "True":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_mad_lib():
    madlibcolor = request.args.get("madlibcolor")
    madlibnoun = request.args.get("madlibnoun")
    person = request.args.get("nickname")
    madlibadjective = request.args.get("madlibadjective")
    return render_template("madlib.html",madlibcolor=madlibcolor, madlibnoun=madlibnoun, person=person, madlibadjective=madlibadjective )


# # route to display a simple web page
# @app.route('/hello')
# def say_hello():
#     return render_template("hello.html")

# @app.route('/greet')
# def greet_person():
#     player = request.args.get("person")
 
    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    # compliment = choice(AWESOMENESS)

    # # return render_template("compliment.html", person=player, compliment=compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
