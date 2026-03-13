from flask import Flask, jsonify
import thermal_model

app = Flask(__name__)

@app.route("/")
def home():
    return "Thermal API Running"

@app.route("/thermal")
def thermal():

    result = {
        "heat_sink_resistance": thermal_model.R_hs,
        "total_thermal_resistance": thermal_model.R_total,
        "junction_temperature": thermal_model.Tj
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)