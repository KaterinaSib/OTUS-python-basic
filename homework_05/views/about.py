from flask import Blueprint, render_template

app_about = Blueprint(
    "app_about",
    __name__,
    url_prefix="/",
)


@app_about.route("/about/", endpoint="about")
def about():
    return render_template("about.html")
