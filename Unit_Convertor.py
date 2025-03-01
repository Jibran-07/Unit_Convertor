import streamlit as st

def length_converter(value, from_unit, to_unit):
    length_units = {
        'Metre': 1,
        'Centimetre': 0.01,
        'Kilometre': 1000,
        'Millimetre': 0.001,
        'Micrometre': 0.000001,
        'Nanometre': 0.000000001,
        'Mile': 1609.34,
        'Yard': 0.9144,
        'Foot': 0.3048,
        'Inch': 0.0254,
        'Nautical mile': 1852
    }
    result = value * length_units[from_unit] / length_units[to_unit]
    factor = length_units[from_unit] / length_units[to_unit]
    if factor > 1:
        formula = f"multiply the length value by {factor:.0f}"
    elif factor < 1:
        formula = f"divide the length value by {1/factor:.0f}"
    else:
        formula = "no conversion needed (same unit)"
    return result, formula

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1,
        'Gram': 0.001,
        'Milligram': 0.000001,
        'Pound': 0.453592,
        'Ounce': 0.0283495
    }
    result = value * weight_units[from_unit] / weight_units[to_unit]
    factor = weight_units[from_unit] / weight_units[to_unit]
    if factor > 1:
        formula = f"multiply the weight value by {factor:.0f}"
    elif factor < 1:
        formula = f"divide the weight value by {1/factor:.0f}"
    else:
        formula = "no conversion needed (same unit)"
    return result, formula

def temp_converter(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            result = (value * 9/5) + 32
            formula = f"({value}°C × 9/5) + 32 = {result:.1f}°F"
        elif to_unit == 'Kelvin':
            result = value + 273.15
            formula = f"{value}°C + 273.15 = {result:.2f}K"
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            result = (value - 32) * 5/9
            formula = f"({value}°F - 32) × 5/9 = {result:.1f}°C"
        elif to_unit == 'Kelvin':
            celsius = (value - 32) * 5/9
            result = celsius + 273.15
            formula = f"(({value}°F - 32) × 5/9) + 273.15 = {result:.2f}K"
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            result = value - 273.15
            formula = f"{value}K - 273.15 = {result:.1f}°C"
        elif to_unit == 'Fahrenheit':
            celsius = value - 273.15
            result = (celsius * 9/5) + 32
            formula = f"(({value}K - 273.15) × 9/5) + 32 = {result:.1f}°F"
    return result, formula

def volume_converter(value, from_unit, to_unit):
    volume_units = {
        'Litre': 1,
        'Millilitre': 0.001,
        'Cubic metre': 1000,
        'Gallon': 3.78541,
        'Quart': 0.946353,
        'Pint': 0.473176,
        'Cup': 0.24
    }
    result = value * volume_units[from_unit] / volume_units[to_unit]
    factor = volume_units[from_unit] / volume_units[to_unit]
    if factor > 1:
        formula = f"multiply the volume value by {factor:.0f}"
    elif factor < 1:
        formula = f"divide the volume value by {1/factor:.0f}"
    else:
        formula = "no conversion needed (same unit)"
    return result, formula

def area_converter(value, from_unit, to_unit):
    area_units = {
        'Square metre': 1,
        'Square kilometre': 1000000,
        'Square centimetre': 0.0001,
        'Square mile': 2589988.11,
        'Square yard': 0.836127,
        'Square foot': 0.092903,
        'Square inch': 0.00064516
    }
    result = value * area_units[from_unit] / area_units[to_unit]
    factor = area_units[from_unit] / area_units[to_unit]
    if factor > 1:
        formula = f"multiply the area value by {factor:.0f}"
    elif factor < 1:
        formula = f"divide the area value by {1/factor:.0f}"
    else:
        formula = "no conversion needed (same unit)"
    return result, formula

def time_converter(value, from_unit, to_unit):
    time_units = {
        'Second': 1,
        'Minute': 60,
        'Hour': 3600,
        'Day': 86400,
        'Week': 604800,
        'Month': 2628000,
        'Year': 31536000
    }
    result = value * time_units[from_unit] / time_units[to_unit]
    factor = time_units[from_unit] / time_units[to_unit]
    if factor > 1:
        formula = f"multiply the time value by {factor:.0f}"
    elif factor < 1:
        formula = f"divide the time value by {1/factor:.0f}"
    else:
        formula = "no conversion needed (same unit)"
    return result, formula

def format_number(num):
    if abs(num) < 0.01 and abs(num) > 0:
        return f"{num:.1e}"
    elif abs(num) >= 1000000:
        return f"{num:.1e}"
    elif abs(num) < 1 and abs(num) > 0:
        return f"{num:.6f}".rstrip('0').rstrip('.')
    else:
        return f"{num:.0f}"

st.title("Unit Converter")

categories = ["Length", "Area", "Mass", "Temperature", "Volume", "Time"]
category = st.selectbox("Select conversion category", categories, key="category_select")

value = st.number_input("", value=1.0, key="value_input")

if category == "Length":
    units = ['Metre', 'Centimetre', 'Kilometre', 'Millimetre', 'Micrometre', 'Nanometre', 'Mile', 'Yard', 'Foot', 'Inch', 'Nautical mile']
elif category == "Area":
    units = ['Square metre', 'Square kilometre', 'Square centimetre', 'Square mile', 'Square yard', 'Square foot', 'Square inch']
elif category == "Mass":
    units = ['Kilogram', 'Gram', 'Milligram', 'Pound', 'Ounce']
elif category == "Temperature":
    units = ['Celsius', 'Fahrenheit', 'Kelvin']
elif category == "Volume":
    units = ['Litre', 'Millilitre', 'Cubic metre', 'Gallon', 'Quart', 'Pint', 'Cup']
elif category == "Time":
    units = ['Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Year']

col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("", units, key="from_unit_select")

with col2:
    to_unit = st.selectbox("", units, key="to_unit_select")
    result_placeholder = st.empty()

if from_unit != to_unit:
    if category == "Length":
        result, formula = length_converter(value, from_unit, to_unit)
    elif category == "Area":
        result, formula = area_converter(value, from_unit, to_unit)
    elif category == "Mass":
        result, formula = weight_converter(value, from_unit, to_unit)
    elif category == "Temperature":
        result, formula = temp_converter(value, from_unit, to_unit)
    elif category == "Volume":
        result, formula = volume_converter(value, from_unit, to_unit)
    elif category == "Time":
        result, formula = time_converter(value, from_unit, to_unit)

    formatted_result = format_number(result)
    result_placeholder.write(formatted_result)

    st.markdown(f"""
        <div style='padding: 10px; border-radius: 4px; margin-top: 10px'>
            <strong style='background-color: #fff3cd; padding: 2px 6px; border-radius: 4px;'>Formula</strong> {formula}
        </div>
    """, unsafe_allow_html=True)
