from flask import Flask, render_template, request
import openai
from config import Config
import csv
import os
from move_to_db import add_to_db_recipe, data_base

app = Flask(__name__)

# Set the API key for OpenAI
openai.api_key = Config.OPENAI_API_KEY

def get_recipe(prompt, max_tokens=Config.MAX_TOKENS, temperature=Config.TEMPERATURE):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",  # Use GPT-4 model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            n=1
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error requesting Chat GPT API: {e}")
        return None

def save_preferences_to_csv(data):
    with open("preferences.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    
    # After saving to CSV, update database
    add_to_db_recipe("preferences.csv", data_base)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recipe', methods=['POST'])
def get_recipe_route():
    food_type = request.form['food_type']
    cuisine = request.form['cuisine']
    allergies = request.form['allergies']
    specific_dish = request.form['specific_dish']
    language = request.form['language']
    
    prompt = f"Give me a step-by-step recipe for {food_type} {specific_dish or 'dish'} in {cuisine} style, considering the following allergies: {allergies}."

    if language.lower() != "english":
        prompt = f"Please provide the recipe in {language}. " + prompt

    recipe = get_recipe(prompt)
    
    if recipe:
        save_preferences_to_csv([food_type, cuisine, allergies, specific_dish, recipe])
        return render_template('result.html', recipe=recipe)
    else:
        return "Failed to get recipe.", 500

if __name__ == '__main__':
    app.run(debug=True)


