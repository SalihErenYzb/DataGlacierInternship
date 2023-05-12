from flask import*
import pickle
app = Flask(__name__)
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
model = open("flight.pkl","rb")
modl = pickle.load(model)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/PredictPrice', methods=['POST'])  
def PredictPrice():  
    stop_count = request.form['stop_count']
    class_type = request.form['class_type']
    days_left = float(request.form['days_left'])
    departure_time = request.form['departure_time']
    arrival_time = request.form['arrival_time']
    destination_city = request.form['destination_city']
    source_city = request.form['source_city']
    flight_duration = request.form['flight_duration']
    airline = request.form['airline']
    flight_duration = float(flight_duration)
    default_values = {
    'stops': 0.0,
    'class': 0.0,
    "duration":0.0,
    "days_left":0.0,
    "city_pair_Bangalore_Chennai"      :0.00,
    "city_pair_Bangalore_Delhi"        :0.00,
    "city_pair_Bangalore_Hyderabad"    :0.00,
    "city_pair_Bangalore_Kolkata"      :0.00,
    "city_pair_Bangalore_Mumbai"       :0.00,
    "city_pair_Chennai_Bangalore"      :0.00,
    "city_pair_Chennai_Delhi"          :0.00,
    "city_pair_Chennai_Hyderabad"      :0.00,
    "city_pair_Chennai_Kolkata"        :0.00,
    "city_pair_Chennai_Mumbai"         :0.00,
    "city_pair_Delhi_Bangalore"        :0.00,
    "city_pair_Delhi_Chennai"          :0.00,
    "city_pair_Delhi_Hyderabad"        :0.00,
    "city_pair_Delhi_Kolkata"          :0.00,
    "city_pair_Delhi_Mumbai"           :0.00,
    "city_pair_Hyderabad_Bangalore"    :0.00,
    "city_pair_Hyderabad_Chennai"      :0.00,
    "city_pair_Hyderabad_Delhi"        :0.00,
    "city_pair_Hyderabad_Kolkata"      :0.00,
    "city_pair_Hyderabad_Mumbai"       :0.00,
    "city_pair_Kolkata_Bangalore"      :0.00,
    "city_pair_Kolkata_Chennai"        :0.00,
    "city_pair_Kolkata_Delhi"          :0.00,
    "city_pair_Kolkata_Hyderabad"      :0.00,
    "city_pair_Kolkata_Mumbai"         :0.00,
    "city_pair_Mumbai_Bangalore"       :0.00,
    "city_pair_Mumbai_Chennai"         :0.00,
    "city_pair_Mumbai_Delhi"           :0.00,
    "city_pair_Mumbai_Hyderabad"       :0.00,
    "city_pair_Mumbai_Kolkata"         :0.00,
    'arrival_time_Afternoon': 0.0,
    'arrival_time_Early_Morning': 0.0,
    'arrival_time_Evening': 0.0,
    'arrival_time_Late_Night': 0.0,
    'arrival_time_Morning': 0.0,
    'arrival_time_Night': 0.0,
    'departure_time_Afternoon': 0.0,
    'departure_time_Early_Morning': 0.0,
    'departure_time_Evening': 0.0,
    'departure_time_Late_Night': 0.0,
    'departure_time_Morning': 0.0,
    'departure_time_Night': 0.0,
    'airline_AirAsia': 0.0,
    'airline_Air_India': 0.0,
    'airline_GO_FIRST': 0.0,
    'airline_Indigo': 0.0,
    'airline_SpiceJet': 0.0,
    'airline_Vistara': 0.0
}    
    def stopChanger(a):
        if a=="zero":
            return 0
        elif a=="one":
            return 1
        else:
            return 2
    mapping = {'Economy': 0, 'Business': 1}

    default_values = pd.Series(default_values)
    default_values.loc['airline_'+ airline]=1.0
    default_values.loc['city_pair_'+ source_city+"_"+destination_city]=1.0
    default_values.loc['departure_time_'+ departure_time]=1.0
    default_values.loc['stops']= stopChanger(stop_count)
    default_values.loc['arrival_time_'+ arrival_time]=1

    default_values.loc['class']=mapping[class_type]
    default_values.loc['duration']= flight_duration
    default_values.loc['days_left']= days_left
        

    
    # create a dictionary to map each category to an integer
    
    # replace each category with its corresponding integer
    

    
    print(default_values)
    
    if request.method=="POST":
        prediction = modl.predict(default_values.to_frame().T)
        
        prediction = prediction/82
        prediction = float(prediction)
    return render_template('request.html', y=format(prediction, '.2f'))










if __name__ == "__main__":
    app.run(debug=True)