from flask import Flask,render_template,request
import predictions
app = Flask(__name__)

@app.route("/")
def index():
	predictions = {'Home Team Winning Probability': 0, 'Draw Probability': 0, 'Away Team Winning Probability': 0, 
	'Predicted Score 1': [0,0,0], 'Predicted Score 2': [0,0,0], 'Predicted Score 3': [0,0,0], 
	'Home Team Betting Odds': 0, 'Draw Betting Odds': 0, 'Away Team Betting Odds': 0 }
	return render_template('index.html', prediction = predictions, home='Home_team',away='Away_team')

@app.route('/submit', methods = ['POST'])
def submit():
	if request.method == 'POST':
		home = request.form.get('home')
		away = request.form.get('away')

		results = predictions.predictor(home,away)
		print(results)
		# scores = { 'score_1':[0,0],'score_2':[1,1],'score_3':[2,2]}
		return render_template("index.html",prediction = results, home=home,away=away)

if __name__ == '__main__':
   app.run(debug = True)