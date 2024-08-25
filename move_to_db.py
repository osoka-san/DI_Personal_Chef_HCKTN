import psycopg2
import csv

data_base = {
    'dbname': 'hackathon_apcm',
    'user': 'priib',
    'password': 'vbigHwNPR5r2TBumP1x5liRKLooAShQ7',
    'host': 'dpg-cr53675umphs73e05b10-a.oregon-postgres.render.com',
    'port': '5432'
}


def add_to_db_recipe(csv_file, data_base):
    try:
        connection = psycopg2.connect(**data_base)
        cursor = connection.cursor()
        
        with open(csv_file, 'r') as file:
            read = csv.reader(file)
            for row in read:
                cursor.execute('''
                    INSERT INTO all_info_from_csv (food_type, cuisine, allergies, specific_dish, recipe)
                    VALUES (%s, %s, %s, %s, %s)
                ''', row)
        connection.commit()
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Error while loading data: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def save_csv(data):
    CSV_FILE = 'preferences.csv'
    try:
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        add_to_db_recipe(CSV_FILE, data_base)
    except Exception as e:
        print(f"Error while saving CSV: {e}")
