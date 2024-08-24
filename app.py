import csv
import os
import openai
from config import Config

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

CSV_FILE = "preferences.csv"

def save_preferences_to_csv(data):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def read_preferences_from_csv():
    preferences = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            preferences = list(reader)
    return preferences

def process_user_request(food_type, cuisine, allergies, specific_dish, language):
    # Form the request based on user preferences
    prompt = f"Give me a step-by-step recipe for {food_type} {specific_dish or 'dish'}" \
             f" in {cuisine} style, considering the following allergies: {allergies}."

    # Add language to the prompt if it's not English
    if language.lower() != "english":
        prompt = f"Please provide the recipe in {language}. " + prompt

    # Get the recipe using the ChatGPT API
    recipe = get_recipe(prompt)

    if recipe:
        # Save the result and preferences to a CSV file
        save_preferences_to_csv([food_type, cuisine, allergies, specific_dish, recipe])
        print("Recipe successfully acquired and stored.")
        return recipe
    else:
        print("Failed to get recipe.")
        return None

def main():
    # Example user data (in a real app this will be provided through a GUI)
    food_type = "vegetarian"
    cuisine = "Italian"
    allergies = "nuts"
    specific_dish = "lasagna"
    language = "english"

    # Process the user's request
    recipe = process_user_request(food_type, cuisine, allergies, specific_dish, language)

    if recipe:
        print("Here's your yummy recipe. Enjoy!!")
        print(recipe)
    else:
        print("Error while getting recipe.")

if __name__ == "__main__":
    main()