import pickle
import streamlit as st 

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


def predict_note_authentication(Age,Experience,Income,Family,CCAvg,Education,Mortgage,Securities Account,CD Account,Online,CreditCard):
    prediction=classifier.predict([[Age,Experience,Income,Family,CCAvg,Education,Mortgage,Securities Account,CD Account,Online,CreditCard]])
    print(Personal Loan)
    return Personal Loan

def main():
    st.title("Loan Approval")
    Age = st.text_input("Age")
    Experience = st.text_input("Experience")
    Income = st.text_input("Income")
    Family = st.text_input("Family")
    CCAvg = st.text_input("CCAvg")
    Education = st.text_input("Education")
    Mortgage = st.text_input("Mortgage")
    Securities Account = st.text_input("Securities Account")
    CD Account = st.text_input("CD Account")
    Online = st.text_input("Online")
    CreditCard = st.text_input("CreditCard")
    
    
    result=""
    if st.button("Personal Loan"):
        result=predict_note_authentication(Age,Experience,Income,Family,CCAvg,Education,Mortgage,Securities Account,CD                         Account,Online,CreditCard)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()
    
    