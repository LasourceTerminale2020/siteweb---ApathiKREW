from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config["DEBUG"] = True



@app.route("/")
def hello():
    # version 1 : les constantes a, b et c sont fixes
    #             les valeurs axe_X et axe_Y sont calculées offline sous excel
    legend = 'f(x) = 3x² + 2x -10'
    return render_template("home.html", message_bienvenue = "ISN - La Source - Ts", legend=legend)

@app.route("/next")
def suite():
    # version 1 : les constantes a, b et c sont fixes
    #             les valeurs axe_X et axe_Y sont calculées offline sous excel
    legend = 'f(x) = 3x² + 2x -10'
    axe_Y = [-10,  -9,  -8,  -7,  -6,  -5,  -4,  -3,  -
             2,  -1,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
    axe_X = [160,  125,  94,  67,  44,  25,  10,  -1,  -8,  -11,  -
             10,  -5,  4,  17,  34,  55,  80,  109,  142,  179,  220]
    return render_template('page_1.html', values=axe_X, labels=axe_Y, legend=legend)

# impossible d appeller une autre page
# malgres le contact du support Pythonanywhere
#@app.route("/next2")
# def suite2():
#    return render_template("page_2.html")

if __name__ == '__main__':
    app.run()
