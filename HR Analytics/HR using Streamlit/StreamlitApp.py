import pandas as pd
import numpy as np
import joblib
import pickle
import streamlit as st

# import multiprocessing
# pool = multiprocessing.Pool(processes=4)

model = open("G:\ML\Projects\HR analytics\HR Analytics\Grid_Search.pkl", "rb")
gs_model = joblib.load(model)

process = open("G:\ML\Projects\HR analytics\HR Analytics\processing.pkl", "rb")
processing = pickle.load(process)

def model_predict(data):
    df = processing(data)
    pred = gs_model.predict(df)
    return pred

def run():
    # print("Hello this is SHUBHAM")
    st.title("HR Analytics For Promotion")
    html_temp = """
    """
    st.markdown(html_temp)

    ### All the columns
    emp_name = st.text_input("Enter Name")
    emp_id = st.text_input("Employee ID number")

    # dataframe creating
    data = pd.DataFrame({
        "employee_name": [str(emp_name)],
        "employee_id": [str(emp_id)]
    })

    ## data columns
    dept = ['Analytics', 'Finance', 'HR', 'Legal', 'Operations', 'Procurement', 'R&D', 'Sales & Marketing', 'Technology']
    department = st.selectbox("Department", dept)
    data["department"] = [str(department)]

    locality = ["region_"+str(i) for i in range (1, 35)]
    region = st.selectbox("Region", locality)
    data["region"] = [str(region)]

    degree = ["Bachelor's", 'Below Secondary', "Master's & above", None]
    education = st.selectbox("Education", degree)
    data["education"] = [str(education)]

    sex = ["f", "m"]
    gender = st.selectbox("Gender", sex)
    data["gender"] = [str(gender)]

    recruit = ['other', 'referred', 'sourcing']
    recruitment_channel = st.selectbox("Recruitment Channel", recruit)
    data["recruitment_channel"] = [str(recruitment_channel)]

    train_exp = np.arange(1, 10)
    no_of_training = st.selectbox("Number of Years Experience", train_exp)
    data["no_of_trainings"] = [str(no_of_training)]

    survive = np.arange(20, 61)
    age = st.selectbox("Age", survive)
    data["age"] = [int(age)]

    rating = [ 1.,  2.,  3.,  4.,  5., None]
    previous_year_rating = st.selectbox("Previous Years Rating", rating)
    data["previous_year_rating"] = [float(previous_year_rating)]

    duty = np.arange(1, 35)
    length_of_service = st.selectbox("Length of Service", duty)
    data["length_of_service"] = [int(length_of_service)]

    kpi = [0, 1]
    KPIs_met = st.selectbox("KPIs met >80%", kpi)
    data["KPIs_met >80%"] = [(kpi)]

    award = [0, 1]
    awards_won = st.selectbox("Awards won", award)
    data["awards_won?"] = [int(awards_won)]

    score = np.arange(1, 101)
    avg_training_score = st.selectbox("Average Training Score", score)
    data["avg_training_score"] = [int(avg_training_score)]

    is_promoted = ""

    if st.button("Is Promoted"):

        ans = model_predict(data)
        # pool.close()
        # pool.join()

        if 1 in ans:
            is_promoted += "Congrutalions, you are promoted to next level."
        else:
            is_promoted += "OOPs, better luck try next time."

    st.success(f"Employe {emp_name} with Employee Id {emp_id}'s {is_promoted}")




if __name__ == "__main__":
    run()

