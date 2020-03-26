import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Hosp_info=pd.read_csv('/home/iceboy/Documents/dataframe/HospInfo.csv')
def Data_clean():
    delt = Hosp_info[(Hosp_info['Hospital overall rating']=='Not Available') | (Hosp_info['Efficient use of medical imaging national comparison']=='Not Available') | (Hosp_info['Patient experience national comparison']=='Not Available') | (Hosp_info['Mortality national comparison']=="Not Available") | (Hosp_info['Safety of care national comparison']=="Not Available")].index
    Hosp_info.drop(delt, inplace=True)
    Hosp_info.drop(["Timeliness of care national comparison footnote","Hospital overall rating footnote","Mortality national comparison footnote","Safety of care national comparison footnote","Readmission national comparison footnote","Patient experience national comparison footnote","Effectiveness of care national comparison footnote","Timeliness of care national comparison footnote","Efficient use of medical imaging national comparison footnote","Location"],axis = 1,inplace=True)
def By_State(name):
    Stat=Hosp_info[Hosp_info.State==name][['Hospital Name','Hospital Type','Hospital Ownership','Hospital overall rating','Phone Number','Address']]
    print(Stat)
def draw_graph():
    State_wise=Hosp_info.groupby('State').count()[['Provider ID']].plot(kind='bar')
    plt.show()
if __name__ == "__main__":
    Data_clean()
    ma=input("Enter the state Initial:  ")
    By_State(ma)
    draw_graph()