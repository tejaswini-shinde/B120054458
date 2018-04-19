from flask import *

app = Flask(__name__)

@app.route('/')

def fun():
	return render_template('index.html',msg="")

@app.route('/check', methods=['POST'])
def check():
	a=checker(request.form['string'])
	return render_template('index.html',msg=a)

def checker(str1):
	file_data=""
	with open ("data.txt","rt") as f:
		file_data=f.read()

	
	unwanted=":',!*&@^!"
	for char in unwanted:
		file_data=file_data.replace(char,"")
		str1=str1.replace(char,"")

	a=file_data.split(".")
	a=a[:-1]
	print "a:",a
	b=str1.split(".")
	a_dict={}
	b_dict={}
	for a_i in a:
		try:
			a_dict[a_i]+=1
		except KeyError:
			a_dict[a_i]=1
	print "a_dict",a_dict
	for b_i in b:
		try:
			b_dict[b_i]+=1
		except KeyError:
			b_dict[b_i]=1
	print b_dict

	counter=0
	for b_keys in b_dict.keys():
		if b_keys in a_dict.keys():
			counter+=b_dict[b_keys]

	percentage = str(float(counter)/(len(b)-1)*100.0)+"%"
	return percentage
			
if __name__ == "__main__":
	app.run()
