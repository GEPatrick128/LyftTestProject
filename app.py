from flask import Flask, jsonify, render_template

app = Flask(__name__)

# home page
@app.route('/')
def homePage():
    return render_template("homepage.html")

# take every third letter of input string
@app.route('/<string_to_cut>')
def stringProcess(string_to_cut):

    res = ""
    for i in range(len(string_to_cut)):
        if (i != 0 and (i + 1) % 3 == 0):
            res += string_to_cut[i]
    return jsonify(res) # return a json object

    # shorten version
    # string_to_cut = string_to_cut[2:]
    # return string_to_cut[::3]

if __name__ == "__main__":
    app.run(debug=True)
