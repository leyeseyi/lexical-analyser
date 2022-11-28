import re

import nltk

from flask import Flask, request, render_template

# Create the app object
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyse',methods=['POST'])
def analyse():

    #Get Input from frontend
    linecode = request.form['code']
    
    #Tokenize inputs
    linecode_tokens = nltk.wordpunct_tokenize(linecode)

    #Token Classifier or Dictionary
    RE_Keywords = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|include"
    RE_Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
    RE_Numerals = "^(\d+)$"
    RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
    RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
    RE_Headers = "([a-zA-Z]+\.[h])"


    #To Categorize The Tokens
    token_class = {}
    for token in linecode_tokens:
        if(re.findall(RE_Keywords,token)):
            token_class[token] =" Keyword"
            print(token , "-------> Keyword")

        elif(re.findall(RE_Operators,token)):
            token_class[token] = " Operator"
            print(token, "-------> Operator")

        elif(re.findall(RE_Numerals,token)):
            token_class[token] = " Numeral"
            print(token, "-------> Numeral")

        elif(re.findall(RE_Special_Characters,token)):
            token_class[token] = " Special Character/Symbol"
            print(token, "-------> Special Character/Symbol")
        elif(re.findall(RE_Identifiers,token)):
            token_class[token] =  " Identifiers"
            print(token, "-------> Identifiers")
        else:
            print("Unknown Value")
    return render_template('index.html', token_class=token_class)
    
if __name__ == "__main__":
    app.run(debug=True)


