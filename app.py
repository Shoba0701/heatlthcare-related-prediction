# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:52:20 2021

@author: Shoba
"""
from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

model_diabetes=pickle.load(open("Diabetes_RF.pkl","rb"))
model_heart=pickle.load(open("heart_randomized_knn.pkl","rb"))
model_cancer=pickle.load(open("Cancer.pkl","rb"))

app=Flask (__name__)

@app.route("/" ,methods=['GET'])
def main():
    return render_template('index.html')

#Diabetes
@app.route('/diabetes.html' , methods=['GET'])
def diabetes():
    return render_template('diabetes.html')


@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes():

    pregnancy=int(request.form['pregnancy'])
    glucose=int(request.form['glucose'])
    presure=int(request.form['presure'])
    skin=np.log(int(request.form['skin']))
    insulin=np.log(int(request.form['insulin']))
    bmi=float(request.form['bmi'])
    DiabetesPedigreeFunction=np.log(float(request.form['DiabetesPedigreeFunction']))
    age=np.log(int(request.form['age']))
    
    array_diabetes=np.array([[skin,insulin,DiabetesPedigreeFunction,age,pregnancy,glucose,presure,bmi]])
    pred_diabetes=model_diabetes.predict(array_diabetes)
    return render_template('after_diabetes.html', data= pred_diabetes)

#Heart_disease

@app.route('/heart.html',methods=['GET'])
def heart():
    return render_template('heart.html')

scaling=StandardScaler()

@app.route('/predict_heart', methods=['POST'])
def predict_heart():
    if request.method == "POST":
        
        age=int(request.form['age'])
        trestbps=int(request.form['trestbps'])
        chol=int(request.form['chol'])
        thalach=int(request.form['thalach'])
        oldpeak=float(request.form['oldpeak'])
        
        numerical_variables=np.array((age,trestbps,chol,thalach,oldpeak))
        numerical_variables_reshape=numerical_variables.reshape(-1,1)
        numerical_variables_reshape_scaling= scaling.fit_transform(numerical_variables_reshape)
        numerical_variables_scaling_reshape=numerical_variables_reshape_scaling.reshape(1,5)
        
        sex=request.form['sex']
        if (sex =="1"):
            sex_1=1
        else:
            sex_1=0
        
        chestpain=request.form['chestpain']
        if (chestpain =="1"):
            cp_1=1
            cp_2=0
            cp_3=0
        elif(chestpain =="2"):
            cp_1=0
            cp_2=1
            cp_3=0
        elif(chestpain =="3"):
            cp_1=0
            cp_2=0
            cp_3=1
        else:
            cp_1=0
            cp_2=0
            cp_3=0
        
        fbs=request.form['fbs']
        if (fbs =="1"):
            fbs_1=1
        else:
            fbs_1=0
            
        restecg=request.form['restecg']
        if (restecg =="1"):
            restecg_1=1
            restecg_2=0
        elif (restecg=="2"):
            restecg_1=0
            restecg_2=1
        else:
            restecg_1=0
            restecg_2=0
        
        exang=request.form['exang']
        if (exang =="1"):
            exang_1=1
        else:
            exang_1=0
        
        slope=request.form['slope']
        if (slope =="1"):
            slope_1=1
            slope_2=0
        elif (slope =="2"):
            slope_1=0
            slope_2=1
        else:
            slope_1=0
            slope_2=0
            
        ca=request.form['ca']
        if (ca =="1"):
            ca_1=1
            ca_2=0
            ca_3=0
            ca_4=0
        elif (ca =="2"):
            ca_1=0
            ca_2=1
            ca_3=0
            ca_4=0
        elif (ca =="3"):
            ca_1=0
            ca_2=0
            ca_3=1
            ca_4=0
        elif (ca =="4"):
            ca_1=0
            ca_2=0
            ca_3=0
            ca_4=1
        else:
    
            ca_1=0
            ca_2=0
            ca_3=0
            ca_4=0
            
        thal=request.form['thal']
        if (thal =="1"):
            thal_1=1
            thal_2=0
            thal_3=0
        elif (thal =="2"):
            thal_1=0
            thal_2=1
            thal_3=0
        elif (thal =="3"):
            thal_1=0
            thal_2=0
            thal_3=1
        else:
            thal_1=0
            thal_2=0
            thal_3=0
            
        categorical_variables=np.array((sex_1,cp_1,cp_2, cp_3, fbs_1, restecg_1, restecg_2, exang_1, slope_1,
                                        slope_2, ca_1, ca_2, ca_3, ca_4, thal_1, thal_2,thal_3))
        categorical_variables_reshape=categorical_variables.reshape(1,17)
        
        input_array_heart=np.concatenate((numerical_variables_scaling_reshape, categorical_variables_reshape),
                                         axis=1)
                  
        pred_heart=model_heart.predict(input_array_heart)
        return render_template('after_heart.html', data=pred_heart)
    
    else:
        return render_template('heart.html')

#Breast_cancer

@app.route('/cancer.html',methods=['GET'])
def cancer():
    return render_template('cancer.html')


@app.route('/predict_cancer', methods=['POST'])
def predict_cancer():
    if request.method == "POST":
        
        radius_worst=float(request.form['radius_worst'])
        concave_points_worst=float(request.form['concave_points_worst'])
        concave_points_mean=float(request.form['concave_points_mean'])
        area_worst=float(request.form['area_worst'])
        perimeter_worst=float(request.form['perimeter_worst'])
        concavity_mean=float(request.form['concavity_mean'])
        area_se=float(request.form['area_se'])
        perimeter_mean=float(request.form['perimeter_mean'])
        radius_mean=float(request.form['radius_mean'])
        concavity_worst=float(request.form['concavity_worst'])
        area_mean=float(request.form['area_mean'])
        compactness_mean=float(request.form['compactness_mean'])
        
        cancer_array=np.array([[radius_worst, concave_points_worst, concave_points_mean, area_worst,
                                perimeter_worst, concavity_mean, area_se,perimeter_mean, radius_mean,
                                concavity_worst, area_mean, compactness_mean]])
        
        pred_cancer=model_cancer.predict(cancer_array)
        return render_template('after_cancer.html', data=pred_cancer)
    else:
        return render_template('cancer.html')
    
if __name__ == "__main__":
    app.debug = True
    app.run()

  

