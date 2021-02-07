import os
import time
import random
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_folder='public', template_folder='views')

QUESTION = []
ANSWER = []
numq = 0

def newQ():
  global numq
  numq = random.randint(0, 65) #UPDATE AS QUESTIONS ARE ADDED

def fillList():
    global QUESTION
    global ANSWER
  
    f = open("Questions.txt","r")  
    a = open ("answers.txt", "r")
    
    wholefilef = f.read()
    wholefilea = a.read()
    
    QUESTION = wholefilef.split("\n")
    ANSWER = wholefilea.split("\n")
    
    print(QUESTION)
        
    f.close()
    a.close()
  
@app.route('/question', methods=['GET', 'POST'])    
def findQuestion():
  global QUESTION
  newQ()
  fillList()
  thisQ = QUESTION[numq]
  return thisQ

@app.route('/answer1', methods = ['GET', 'POST'])
def findAnswer1():
    global ANSWER
    global numq
    fillList()
    print(numq)
    thisA1 = ANSWER[4*numq]
    return thisA1
  
@app.route("/answer2", methods = ["GET", "POST"])
def findAnswer2():
    global ANSWER
    global numq
    fillList()
    thisA2 = ANSWER[4*numq+1]
    return thisA2
  
@app.route("/answer3", methods = ["GET", "POST"])
def findAnswer3():
    global ANSWER
    global numq
    fillList()
    thisA3 = ANSWER[4*numq+2]
    return thisA3
  
@app.route("/answer4", methods = ["GET", "POST"])
def findAnswer4():
    global ANSWER
    global numq
    fillList()
    thisA4 = ANSWER[4*numq+3]
    return thisA4
  
@app.route("/wait", methods = ["GET", "POST"])
def sleep():
    time.sleep(1)
    return ""

@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
