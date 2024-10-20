import os
import json

def load_json():

    try:
        dir = input("Enter the name of the JSON file directory: ")
        json_file = "musthak_shaik_adoptions.json" 
        file_path = os.path.join(dir, json_file)
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Json file is not found in directory")
    except Exception as e:
        print("error occurred:",e)

json_data = load_json()

import pandas as pd

def contacts_csv(data):

    contacts = []
    for i in data:
        for j in i['contacts']:
            contacts.append({
                "Adoption ID": i['id'],
                "Order": j['order'],
                "Gender": j['gender'],
                "First Name": j['firstname'],
                "Last Name": j['lastname']
            })

    contacts = pd.DataFrame(contacts)
    contacts.to_csv('contacts.csv')
    print("csv file created")

def universities_csv(data):

    universities = []
    for i in data:
            if 'address' not in i['university']:
                universities.append({
                "Adoption ID": i['id'],
                "University ID": i['university']['id'],
                "Name": i['university']['name'],
                "Address": "NA",
                "City": i['university']['city'],
                "State": i['university']['state'],
                "Website": i['university']["website"],
                "ZIP": i['university']['zip'],
                "Longitude": i['university']['longitude'],
                "Latitude": i['university']['latitude'],
                "Classification": i['university']['classification']
                })

            elif 'website' not in i['university']:
                universities.append({
                "Adoption ID": i['id'],
                "University ID": i['university']['id'],
                "Name": i['university']['name'],
                "Address": i['university']['address'],
                "City": i['university']['city'],
                "State": i['university']['state'],
                "Website": "NA",
                "ZIP": i['university']['zip'],
                "Longitude": i['university']['longitude'],
                "Latitude": i['university']['latitude'],
                "Classification": i['university']['classification']
                })

            else:
             universities.append({
                "Adoption ID": i['id'],
                "University ID": i['university']['id'],
                "Name": i['university']['name'],
                "Address": i['university']['address'],
                "City": i['university']['city'],
                "State": i['university']['state'],
                "Website": i['university']["website"],
                "ZIP": i['university']['zip'],
                "Longitude": i['university']['longitude'],
                "Latitude": i['university']['latitude'],
                "Classification": i['university']['classification']
             })

    universities = pd.DataFrame(universities)
    universities.to_csv('universties.csv')
    print("csv file created")