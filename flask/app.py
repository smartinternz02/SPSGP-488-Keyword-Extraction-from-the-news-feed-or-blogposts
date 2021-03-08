from flask import Flask, request, render_template
import re
import requests

app = Flask(__name__)

def check(typ,output):
    url = "https://seo-keyword-extraction-from-url.p.rapidapi.com/"

    payload = "{\"input_data\": [\""+output+"\"], \"input_type\": \""+typ+"\", \"N\": 20}"
    #print(payload)
    headers = {
    'x-rapidapi-host': "seo-keyword-extraction-from-url.p.rapidapi.com",
    'x-rapidapi-key': "fc7d2661e5msh3883b30e2558118p19f844jsna07968dd9ba0",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url,  data=payload,  headers=headers)
    print(response.text)
    #return response.text
    return response.json()['result']
    

#home page
@app.route('/')
def home():
    return render_template('home.html')

#home page
@app.route('/extractor')
def extractor():
    return render_template('extractor.html')

#extractor page
@app.route('/keywords',  methods=['POST'])
def keywords():
    typ=request.form['type']
    output = request.form['output']
    if typ=="text":
        output=re.sub("[^a-zA-Z.,]"," ",output)
    print(output)
    keyword = check(typ,output)
    #return keyword
    return render_template('keywords.html',keyword=keyword)

    
if __name__ == "__main__":
    app.run(debug=False)