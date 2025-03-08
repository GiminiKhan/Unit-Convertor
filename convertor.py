#Project 01: Unit Convertor
#Build a Google Unit Convertor using Python and Streamlit:

import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp {
        background:linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton>button{
        background: linear-gradient(45deg, #0b5394, #351c75);
        color:white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow:0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: black;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background-color: #2e2e4a;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
        margin-top: 20px;
        margin-bottom: 20px;
        color: white;
        transition: 0.3s;
    }
    .result-box:hover {
        transform: scale(1.05);
        background-color: #351c75;
        color: black;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
        cursor: pointer;
    }
    .footer{
        text-align:center;
        margin-top: 50px;
        font-size:14px;
        color: black;
    }
    </style>    
    """,
    unsafe_allow_html=True
)

st.markdown("<h1> Unit Converter using Python & Streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of measurement like length, weight, temperature, etc.")

conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["length", "weight", "temperature"])
value = st.sidebar.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "length":
    with col1:
        from_unit = st.selectbox("From Unit", ["meters", "kilometers", "miles", "yards", "feet", "inches"])
    with col2:
        to_unit = st.selectbox("To Unit", ["meters", "kilometers", "miles", "yards", "feet", "inches"])
elif conversion_type == "weight":
    with col1:
        from_unit = st.selectbox("From Unit", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
    with col2:
        to_unit = st.selectbox("To Unit", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
elif conversion_type == "temperature":
    with col1:
        from_unit = st.selectbox("From Unit", ["celsius", "fahrenheit", "kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit", ["celsius", "fahrenheit", "kelvin"])


def length_converter(value, from_unit, to_unit):
    length_units = {
        'meters': 1, 'kilometers': 0.001, 'miles': 0.000621371, 'yards': 1.09361, 'feet': 3.28084, 'inches': 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]


def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'kilograms': 1, 'grams': 1000, 'milligrams': 1000000, 'pounds': 2.20462, 'ounces': 35.27396
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]


def temperature_converter(value, from_unit, to_unit):
    if from_unit == "celsius":
        return (value * 9/5 + 32) if to_unit == "fahrenheit" else (value + 273.15) if to_unit == "kelvin" else value
    elif from_unit == "fahrenheit":
        return ((value - 32) * 5/9) if to_unit == "celsius" else ((value - 32) * 5/9 + 273.15) if to_unit == "kelvin" else value
    elif from_unit == "kelvin":
        return (value - 273.15) if to_unit == "celsius" else ((value - 273.15) * 9/5 + 32) if to_unit == "fahrenheit" else value
    return value

if st.button("Convert"):
    if conversion_type == "length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "temperature":
        result = temperature_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Developed by Quratulain <a href='https://github.com/GiminiKhan'>@GiminiKhan</a></div>", unsafe_allow_html=True)

if st.button("Clear"):
    st.cache_data.clear()
    st.rerun()
