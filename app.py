from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion functions
def convert_length(value, from_unit, to_unit):
    factors = {
        'millimeter': 0.001,
        'centimeter': 0.01,
        'meter': 1,
        'kilometer': 1000,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34
    }
    meters = value * factors[from_unit]
    return round(meters / factors[to_unit], 6)

def convert_weight(value, from_unit, to_unit):
    factors = {
        'milligram': 0.001,
        'gram': 1,
        'kilogram': 1000,
        'ounce': 28.3495,
        'pound': 453.592
    }
    grams = value * factors[from_unit]
    return round(grams / factors[to_unit], 6)

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return round((value * 9/5) + 32, 2)
        elif to_unit == 'Kelvin':
            return round(value + 273.15, 2)
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return round((value - 32) * 5/9, 2)
        elif to_unit == 'Kelvin':
            return round((value - 32) * 5/9 + 273.15, 2)
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return round(value - 273.15, 2)
        elif to_unit == 'Fahrenheit':
            return round((value - 273.15) * 9/5 + 32, 2)
    return round(value, 2)

# Routes
@app.route('/')
def index():
    return render_template('length.html')

@app.route('/length', methods=['GET', 'POST'])
def length_converter():
    result = None
    if request.method == 'POST':
        input_value = float(request.form['input_value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_length(input_value, from_unit, to_unit)
    return render_template('length.html', result=result)

@app.route('/weight', methods=['GET', 'POST'])
def weight_converter():
    result = None
    if request.method == 'POST':
        input_value = float(request.form['input_value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_weight(input_value, from_unit, to_unit)
    return render_template('weight.html', result=result)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature_converter():
    result = None
    if request.method == 'POST':
        input_value = float(request.form['input_value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_temperature(input_value, from_unit, to_unit)
    return render_template('temperature.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
