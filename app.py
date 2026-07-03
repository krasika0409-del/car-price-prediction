import streamlit as st
import pandas as pd
import pickle as pkl

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Car Price Prediction",
    layout="wide"
)

# ---------------- Load Model ----------------
model = pkl.load(open("model.pkl", "rb"))

# ---------------- Sidebar ----------------
st.sidebar.header("Car Details")

company = st.sidebar.selectbox(
    "Select company",
    ['Hyundai','Ford','Maruti','Skoda','Mahindra','Audi','Toyota',
     'Renault','Honda','Datsun','Mitsubishi','Tata','Volkswagen',
     'Chevrolet','Mini','BMW','Nissan','Hindustan','Fiat',
     'Force','Mercedes','Jeep','Volvo']
)

name = st.sidebar.selectbox(
    "Select name",
    [
        "Santro Xing",
        "Grand i10",
        "EcoSport Titanium",
        "Figo",
        "Eon",
        "EcoSport Ambiente",
        "Suzuki Alto",
        "Fabia Classic",
        "Suzuki Stingray",
        "Elite i20",
        "Logan",
        "Sail 1.2",
        "Manza",
        "Etios G",
        "Qualis",
        "Quanto C4",
        "i20 Select",
        "Getz",
        "Fabia",
        "Zest XM"
    ]
)

year = st.sidebar.number_input(
    "Enter year",
    min_value=2000,
    max_value=2024,
    step=1
)

kms_driven = st.sidebar.number_input(
    "Enter km driven",
    min_value=10000,
    max_value=400000,
    step=5000
)

fuel_type = st.sidebar.selectbox(
    "Select fuel type",
    ["Petrol","Diesel"]
)

predict = st.sidebar.button("Predict Price")

# ---------------- Main Page ----------------
st.title("Car Price Prediction App")

st.subheader("Predicting for")

st.write(f"**Company:** {company}")
st.write(f"**Name:** {name}")
st.write(f"**Year:** {year}")
st.write(f"**KM Driven:** {kms_driven}")
st.write(f"**Fuel Type:** {fuel_type}")

# ---------------- Prediction ----------------
if predict:

    data = [[company, name, year, kms_driven, fuel_type]]

    columns = [
        "company",
        "name",
        "year",
        "kms_driven",
        "fuel_type"
    ]

    df = pd.DataFrame(data, columns=columns)

    result = model.predict(df)

    price = round(result[0][0])

    if price > 0:
        st.success(f"Predicted Price: ₹ {price:,}")
    else:
        st.error("Unavailable")