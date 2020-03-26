import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Hosp_info=pd.read_csv('/home/iceboy/Documents/dataframe/HospInfo.csv')
def Data_clean():
    delt = Hosp_info[(Hosp_info['Hospital_rating']=='Not Available') | (Hosp_info['Efficient use of medical imaging national comparison']=='Not Available') | (Hosp_info['Patient experience national comparison']=='Not Available') | (Hosp_info['Mortality national comparison']=="Not Available") | (Hosp_info['Safety of care national comparison']=="Not Available")].index
    Hosp_info.drop(delt, inplace=True)
    Hosp_info.drop(["Timeliness of care national comparison footnote","Hospital overall rating footnote","Mortality national comparison footnote","Safety of care national comparison footnote","Readmission national comparison footnote","Patient experience national comparison footnote","Effectiveness of care national comparison footnote","Timeliness of care national comparison footnote","Efficient use of medical imaging national comparison footnote","Location"],axis = 1,inplace=True)
def By_Types(type):
    Types=Hosp_info[Hosp_info.Hospital_Ownership==type][['Hospital Name','Hospital Type','Hospital_rating','Phone Number','Address','State']]
    print(Types)
    draw_graph()
def draw_graph():
    State_wise=Hosp_info.groupby('Hospital_Ownership').count()[['Provider ID']].plot(kind='bar')
    plt.show()
if __name__ == "__main__":
    Data_clean()
    type=int(input("Enter 1 for Government \n 2 for Propietary \n 3 for voluntary(church) \n 4 for Voluntary(Private) \n 5 for Voluntary(others) \n 6 for Physician \n 7 for Govt(local) \n 8 for Govt(state) \n 9 for Tribal \n 10 for Govt(Federal)    :"))
    if type==1:
       type = "Government - Hospital District or Authority"
       By_Types(type)
    elif type == 2:
        type= "Proprietary"
        By_Types(type)
    elif type == 3:
        type= "Voluntary non-profit - Church"
        By_Types(type)
    elif type == 4:
        type= "Voluntary non-profit - Private"
        By_Types(type)
    elif type == 5:
        type= "Voluntary non-profit - Other"
        By_Types(type)
    elif type == 6:
        type = "Physician"
        By_Types(type)
    elif type == 7:
        type = "Government - Local"
        By_Types(type)
    elif type == 8:
        type = "Government - State"
        By_Types(type)
    elif type == 9:
        type = "Tribal"
        By_Types(type)
    elif type == 10:
        type = "Government - Federal"
        By_Types(type)
    else:
        print("Wrong input")