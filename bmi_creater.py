

import json
import pandas as pd

# data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
# { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
# { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
# { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
# {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
# {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

#send data as jason format
def calculate_bmi(data):
    
    data_list=[]
    for i in data:
        height_in_meters = i['HeightCm']/100  
        weight_in_kg = i['WeightKg']
        bmi = weight_in_kg/height_in_meters
        if bmi<=18.4:
            bmi_category = 'Underweight'
            health_risk = 'Malnutrition risk'
            
        if bmi>=18.5 and bmi<=24.9:
            bmi_category = 'Normal weight'
            health_risk = 'Low risk'
            
        if bmi>=25 and bmi<=29.9:
            bmi_category = 'Overweight'
            health_risk = 'Enhanced risk'
            
        if bmi>=30 and bmi<=34.9:
            bmi_category = 'Moderately obese'
            health_risk = 'Medium risk'
            
        if bmi>=35 and bmi<=39.9:
            bmi_category = 'Severely obese'
            health_risk = 'High risk'
            
        else:
            bmi_category = 'Very severely obese'
            health_risk = 'Very high risk'
            
        data_list.append([i['Gender'],i['HeightCm'],weight_in_kg,bmi,bmi_category,health_risk])
        
    df = pd.DataFrame(data_list,columns=['Gender','Height Cm','Weight Kg','BMI','BMI category','Health risk'])
    
    total_overweight = len(df[df['BMI category']=='Overweight'])
            
            
    return total_overweight,df

#return dataframe of bmi calculated df and total overweight
calculate_bmi(data)
