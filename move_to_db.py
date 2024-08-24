import psycopg2
import csv
data_base = {
    'dbname': 'hackathon',
    'user': 'postgres',
    'password': '1739',
    'host': 'localhost',
    'port': '5432'
}

 
def add_to_db_recipe(csv_file,data_base):
    try: 
        connection = psycopg2.connect(**data_base)
        cursor = connection.cursor()
        
        with open(csv_file,'r') as file:
            read = csv.reader(file)
            for row in read:
                cursor.execute('''
INSERT INTO all_info_from_csv (food_type, cuisine, allergies, specific_dish, recipe) VALUES (%s,%s,%s,%s,%s)
''',row)
        connection.commit()
        print("Data loaded.")
    except Exception as e:
        print(f"Error{e}")

    finally:
        cursor.close()
        connection.close()

add_to_db_recipe('preferences.csv',data_base)
def save_csv(data):
    CSV_FILE = 'preferences.csv' 
    with open(CSV_FILE,mode = 'a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    add_to_db_recipe(CSV_FILE,data_base)
