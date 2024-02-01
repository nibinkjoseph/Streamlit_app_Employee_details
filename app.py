import streamlit as st
import pandas as pd
import os
# Define the form
def create_form():
    st.title("Employee Verification Form")

    company_name = st.text_input("Company or employer name:")
    company_address = st.text_input("Company or employer address:")
    employee_name = st.text_input("Employee name:")
    employee_address = st.text_input("Employee address:")
    is_employee = st.radio("Is or was this person your employee?", ("Yes", "No"))

    if is_employee == "No":
        st.stop()

    date_first_check = st.date_input("Date of first check:")
    date_hired = st.date_input("Date hired:")
    job_type = st.text_input("What type of job does or did this person have?")
    job_status = st.multiselect("This job is or was (mark all that apply):", ("Full Time", "Part Time"))
    avg_hours = st.number_input("Average hours per pay period:")
    rate_of_pay = st.number_input("Rate of pay:")
    pay_frequency = st.selectbox("How often paid:", ("Hour", "Day", "Once a week", "Once a month", "Daily", "Twice a month"))
    overtime_pay = st.radio("Does or did this person get overtime pay?", ("Yes", "No"))
    fica_withheld = st.radio("FICA or FIT withheld?", ("Yes", "No"))
    leave_without_pay = st.radio("Is or was this person on leave without pay?", ("Yes", "No"))
    if leave_without_pay == "Yes":
        pay_period_end = st.date_input("Date pay period ended:")

    health_insurance = st.radio("Does your company offer health insurance?", ("Yes", "No"))
    if health_insurance == "Yes":
        start_date_leave = st.date_input("Start date of leave:")
        end_date_leave = st.date_input("End date of leave:")

    pension_plan = st.radio("Does this person have a profit sharing or pension plan?", ("Yes", "No"))
    if pension_plan == "Yes":
        enrolled = st.radio("This person is:", ("Not enrolled", "Enrolled with family members"))
        if enrolled == "Enrolled with family members":
            insurance_company = st.text_input("Name of insurance company:")

    changes_expected = st.radio("Do you expect any changes to the facts above within the next few months?", ("Yes", "No"))
    if changes_expected == "Yes":
        change_date = st.date_input("Date:")
        change_month = st.selectbox("Month:", ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"))

    st.write("On this chart, list all money this person got from jobs or training:")
    job = st.text_input("Job:")
    other_pay = st.number_input("Other pay (include tips, commissions and bonuses):")
    reason_for_separation = st.text_input("Reason for separation:")

    employer_sign = st.text_input("Employer - sign here:")
    st.write("I confirm that this information is true and correct to the best of my knowledge:")

    return {
        "company_name": company_name,
        "company_address": company_address,
        "employee_name": employee_name,
        "employee_address": employee_address,
        "is_employee": is_employee,
        "date_first_check": date_first_check,
        "date_hired": date_hired,
        "job_type": job_type,
        "job_status": job_status,
        "avg_hours": avg_hours,
        "rate_of_pay": rate_of_pay,
        "Reason": reason_for_separation
    }


if __name__ == "__main__":
   form_data= create_form()


button_style = """
    <style>
    div.stButton > button:first-child {
        background-color: green;
        color: white;
        width: 150px; /* Optional: Set width */
        height: 40px; /* Optional: Set height */
        font-size: 16px; /* Optional: Set font size */
        border-radius: 10px; /* Optional: Set border radius */
    }
    </style>
"""

st.markdown(button_style, unsafe_allow_html=True)
if st.button('Submit'):
        st.write('Button Clicked!')
        filename = "employee_detail.xlsx"
        if os.path.isfile(filename):
            # If file exists, append to it
            df = pd.read_excel(filename)
            df = pd.concat([df, pd.DataFrame([form_data])], ignore_index=True)
        else:
            # If file doesn't exist, create a new DataFrame
            df = pd.DataFrame([form_data])
        
        # Save DataFrame to Excel
        df.to_excel(filename, index=False)
        st.success("Form data saved successfully as employee_details.xlsx")   