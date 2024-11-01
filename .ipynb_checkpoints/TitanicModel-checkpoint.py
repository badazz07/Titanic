import streamlit as st
import joblib

# load the pre-trained model
model = joblib.load('Titanic_Logistic.model')

# Set the title of the Streamlit app
st.title("Titanic Survival Prediction")

# Create two columns for input fields
col1, col2 = st.columns(2)

# Collect user input through the input fields
Pclass = col1.number_input(label="Enter the Passenger's class", min_value=1, max_value=3)
Sex = col2.number_input(label="Enter the Passenger's sex (0 for Female and 1 for Male)", min_value=0, max_value=1)
Number_of_Siblings = col1.number_input(label="Enter the number of siblings/spouses per passenger", min_value=0, max_value=6)
Parch = col2.number_input(label="Enter the number of parents/children per passenger", min_value=0, max_value=6)
Embarked = col1.number_input(label="Enter the city the passenger is embarking from (0, 1, 2)", min_value=0, max_value=2)
Age = col2.number_input(label="Enter the Age of the passenger", min_value=0, max_value = 80)
Fare = col1.number_input(label="Enter the Fare the passenger paid", min_value=-0.6)

# Define a button to submit the input and predict the result
if st.button("Predict"):
    # Use the model to make a prediction
    prediction = model.predict([[Pclass, Sex, Number_of_Siblings, Parch, Embarked, Age, Fare]])
    
    # Display the prediction result
    if prediction == 1:
        st.success("The model predicts that the passenger would have survived.")
    else:
        st.warning("The model predicts that the passenger would not have survived.")