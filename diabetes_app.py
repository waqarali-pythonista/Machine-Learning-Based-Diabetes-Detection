import streamlit as st
import joblib

def main():
    # CSS styles for customizing the appearance
    st.markdown(
        """
        <style>
        .title {
            font-family: Arial, sans-serif;
            color: #FF5733; /* Change title font color */
            font-size: 36px; /* Increase title font size */
        }
        body {
            background-color: #F0F8FF; /* Change background color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title with custom CSS class
    st.markdown('<p class="title">Diabetes Predictor</p>', unsafe_allow_html=True)

    # Load the trained model
    model = joblib.load('model_diabetes')

    # Input fields
    pregnancies = st.number_input("Pregnancies", min_value=0, step=1, value=0)
    glucose = st.number_input("Glucose", min_value=0.0, step=1.0, value=0.0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0.0, step=1.0, value=0.0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0.0, step=1.0, value=0.0)
    insulin = st.number_input("Insulin", min_value=0.0, step=1.0, value=0.0)
    bmi = st.number_input("BMI", min_value=0.0, step=0.1, value=0.0)
    pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, step=0.01, value=0.0)
    age = st.number_input("Age", min_value=0, step=1, value=0)

    new_data = [(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, pedigree_function, age)]

    # Output button
    if st.button("Predict Diabetes"):
        prediction = model.predict(new_data)
        if prediction[0] == 0:
            st.write("Non-Diabetic")
        else:
            st.write("Diabetic")

if __name__ == "__main__":
    main()
