from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        lat = request.form.get("lat")
        lon = request.form.get("lon")
        alt = request.form.get("alt", 0)
        form_url = request.form.get("form_url")
        # Redirect to Google Form with JS injection
        return render_template("index.html", lat=lat, lon=lon, alt=alt, form_url=form_url)
    return render_template("index.html", lat="", lon="", alt="", form_url="")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
