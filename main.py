from flask import Flask, redirect
import json

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/v1/main/en/glow")

@app.route('/v1/<menu>/<lang>/<icon>')
def generate(menu,lang,icon):
    #File setup
    vcard = open(menu + '/' + lang + '.txt', 'r')
    vcard = vcard.read()
    vcard = vcard.splitlines()
    icons = json.loads(open(menu + '/' + icon + '-icons.json', 'r').read())
    result = ''
    count = 0
    for item in vcard:
        if 'PHOTO;ENCODING=b:' in item:
            count += 1
            result += item + icons[str(count)] + '\n'
        else:
            result += item + '\n'
    code = ''
    print(result)
    result = result.splitlines()
    for item in result:
        code += '<p>' + item + '</p>'  
    return code

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
