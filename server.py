from flask import Flask, render_template, session, request, redirect
app=Flask(__name__)
app.secret_key= 'boise'

@app.route('/')
def index():
	if 'view' not in session:
		session['view']=1
	else:
		session['view']+=1
	return render_template('index.html')
# adds 1 to count for every refresh

@app.route('/addtwo', methods=['POST'])
def process():
	session['view']+=1
	return redirect ('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['view']=0
	return redirect('/')

app.run(debug=True)