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

def list_universities_by_state(data, state_name):
    universities = []
    for record in data:
        if record['university']['state'] == state_name:
            universities.append(record['university']['name'])
    if universities:
        print("Universities in",state_name,":")
        for uni in universities:
            print(uni)
    else:
        print("No universities found in",state_name)

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

def adoptions_csv(data):

    adoptions = []
    for i in data:
        for j in i['adoptions']:
            adoptions.append({
                "Adoption ID": i['id'],
                "ID": j['id'],
                "Date": j['date'],
                "Quantity ": j['quantity'],
                "Book ID": j['book']['id'],
                "isbn10": j['book']['isbn10'],
                "isbn13": j['book']['isbn13'],
                "title": j['book']['title'],
                "Category": j['book']['category']
            })

    adoptions = pd.DataFrame(adoptions)
    adoptions.to_csv('adoptions.csv')
    print("csv file created")


def messages_csv(data):

    messages = []
    for i in data:
        for j in i['messages']:
            messages.append({
                "Adoption ID": j['id'],
                "ID": j['id'],
                "Date": j['date'],
                "Content": j['content'],
                "Category": j['category']
            })

    messages = pd.DataFrame(messages)
    messages.to_csv('messages.csv')
    print("csv file created")

def universities_state(data, state):

    universities = []
    for i in data:
        if i['university']['state'] == state:
            universities.append(i['university']['name'])

    print(f"Universities in {state} :")
    for i in universities:
        print(i)


def books_category(data):

    categories = []
    for i in data:
        for j in i['adoptions']:
            if j['book']['category'] in categories:
                continue
            else:
                categories.append(j['book']['category'])
    print("Categories:")

    for i in categories:
        print(i)
    user_choice = input("Enter the category you want: ")

    book_titles = []
    for i in data:
        for j in i['adoptions']:
            if j['book']['category'] == user_choice:
                book_titles.append(j['book']['title'])

    with open(f"{user_choice}.txt", 'w') as text_file:
        for i in book_titles:
            text_file.write(f"{i}\n")
    print(f"Books have been saved to {user_choice}.txt")



books_category(json_data)