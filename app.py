from flask import Flask, request, render_template

from processing import calculate_sd

app = Flask(__name__)
app.config["DEBUG"] = True

inputs = []

@app.route("/", methods=["GET", "POST"])
def sd_page():
    errors = ""
    if request.method == "POST":
        try:
            inputs.append(float(request.form["number"]))
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number"])

        if request.form["action"] == "Standard Deviation":
            result = calculate_sd(inputs)
            inputs.clear()
            return '''
                <html>
                    <body>
                        <p>{result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)

    if len(inputs) == 0:
        numbers_so_far = ""
    else:
        numbers_so_far = "<p>Numbers so far:</p>"
        for number in inputs:
            numbers_so_far += "<p>{}</p>".format(number)

    return render_template("index.html").format(numbers_so_far=numbers_so_far, errors=errors)

if __name__ == "__main__":
    app.run(debug=True)


