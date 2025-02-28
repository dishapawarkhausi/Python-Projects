from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Conversion logic
def convert_units(category, from_unit, to_unit, value):
    conversions = {
        "Length": {
            "meters": 1,
            "kilometers": 0.001,
            "centimeters": 100,
            "millimeters": 1000,
            "miles": 0.000621371,
            "yards": 1.09361,
            "feet": 3.28084,
            "inches": 39.3701
        },
        "Weight": {
            "kilograms": 1,
            "grams": 1000,
            "pounds": 2.20462,
            "ounces": 35.274
        },
        "Temperature": {
            "Celsius": lambda x: x,
            "Fahrenheit": lambda x: (x * 9/5) + 32,
            "Kelvin": lambda x: x + 273.15
        }
    }
    
    if category == "Temperature":
        return conversions[category][to_unit](value)
    else:
        return value * (conversions[category][to_unit] / conversions[category][from_unit])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    category = data['category']
    from_unit = data['from_unit']
    to_unit = data['to_unit']
    value = float(data['value'])
    
    result = convert_units(category, from_unit, to_unit, value)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
