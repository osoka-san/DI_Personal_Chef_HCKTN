from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def site():
    return render_template('site.html')
@app.route('/get_recipe', methods=['POST'])
def get_reecipe():
    food_type = request.form['food_type']
    cuisine = request.form['cuisine']
    allergies = request.form['allergies']
    specific_dish = request.form['specific_dish']
    recipe = "YOUR RECIPE"
    return render_template('site_2.html', recipe=recipe)
if __name__ == '__main__':
    app.run(debug=True)
