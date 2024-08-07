from flask import Blueprint, render_template

app_about = Blueprint(
    "app_about",
    __name__,
    url_prefix="/about",
)


@app_about.route("/", endpoint="about")
def about():
    return render_template("about.html")
