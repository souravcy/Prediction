import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('pt.pkl','rb'))

def predict(aqi):
    prediction = model.predict(aqi)
    result = (prediction)
    return result

def main():
    style = """
              <h1 style='color:black'>Air Pollution Prediction App</h1>
       </div>"""
    st.markdown(style, unsafe_allow_html=True)
    st.write("Enter the AQI value of last 5 days: ")

    left, right = st.columns((4,4))
    aqi1=[]
    aqi2=[]
    aqi3=[]
    aqi4=[]
    aqi5=[]
    aqi1.append(left.number_input('First Day: ',
                                  step =1.0, format="%.2f", value=0.0))
    aqi2.append(right.number_input('Second Day: ',
                                  step=1.0, format='%.2f', value= 0.0))
    aqi3.append(left.number_input('Third Day: ',
                                           step=1.0, format='%.2f', value=0.0))
    aqi4.append(right.number_input('Fourth Day: ',
                                     step=1.0, format='%.2f', value=0.0))
    aqi5.append(left.number_input('Fifth Day: ',
                                       step=1.0, format='%.2f', value=0.0))
    list2=[]
    list2.append(aqi1)
    list2.append(aqi2)
    list2.append(aqi3)
    list2.append(aqi4)
    list2.append(aqi5)
    list3=[]
    list3.append(list2)
    aqi=np.array(list3)

    button = st.button('Predict')
    
    # if button is pressed
    if button:
        
        # make prediction
        result = predict(aqi)
        st.success(f'The Predicted AQI value is {result[0][0]}')

main()



