import os
import time
from googletrans import Translator
from flask import Flask, render_template ,flash, request
from wtforms import Form
#from wtforms.fields import StringField
from wtforms import  TextAreaField, SubmitField
import wtforms
from googletrans import Translator
#from wtforms.widgets import TextArea
#from flask_wtf.csrf import CSRFProtect, CSRFError
app = Flask(__name__)
#csrf = CSRFProtect(app)
from flask import request




class MyForm(Form):
	inp = TextAreaField('INPUT')
	op = TextAreaField('OUTPUT')


@app.route('/')
def front():
	form=MyForm()
	return render_template('front.html',form=form)

@app.route('/', methods=["POST"])
def front2():
    form=MyForm()
    inp1=request.form['inp']
    f = open('test.txt', 'r+') 
    input_list=[]
    input_list.append(inp1)
    ip = f.readlines()
    for i in ip:
      input_list.append(i)
    f.seek(0,0)
    f.write(inp1+"\n")
    f.close()
    os.system('th translate.lua -model en-ml-final-epoch.t7 -src test.txt -output result.txt')
    f=open('result.txt', "r")
    if f.mode == 'r':
        op2 =f.readlines()
	translated=[]
	for x in op2:
		x=x.decode('utf-8')
		translated.append(x)
    return render_template('front.html',form=form,inp1=input_list,op2=translated)
    
@app.route('/gg', methods=["GET", "POST"])
def front3():
	if request.method == 'GET':
	    form=MyForm()
	    return render_template('front1.html',form=form)
	else:
		form=MyForm()
		inp1=request.form['inp']
		f = open('input.txt', 'w')  
		f.write(inp1)
		f.close()
    	f = open('input.txt', 'r') 
    	translator = Translator()
    	if f.mode == 'r':
    	    new =f.read()
    	s = translator.translate(inp1, dest='ml') 
    	op2=s.text;
    	time.sleep(2)
    	return render_template('front1.html',form=form,inp1=inp1,op2=op2)

if __name__ == '__main__':
	 app.run(debug = True)

