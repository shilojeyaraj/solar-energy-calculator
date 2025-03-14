from flask import Blueprint, render_template, request
from .calculations import calculate_solar_power, NASA_API_KEY

# Create Blueprint
app = Blueprint('solar', __name__, url_prefix='/solar')

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Solar index route accessed")  # Debug print
    if request.method == "POST":
        panel_location = request.form["city"]
        panel_area = float(request.form["panel_area"])
        efficiency = float(request.form["efficiency"]) / 100

        results, error = calculate_solar_power(panel_location, panel_area, efficiency, NASA_API_KEY)
        if error:
            return render_template("index.html", error=error)

        return render_template("index.html", results=results, efficiency=efficiency * 100)

    return render_template("index.html", efficiency=50)


