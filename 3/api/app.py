from flask import Flask, request, render_template, jsonify
from redis_cache_ import ini, find_match, add_to_dic

ini("female-name.txt")

app = Flask(__name__, template_folder="Templates") 
#Templates can be add directly button to form add word and query
#this is furure scope

@app.route("/")
def index():
    return "Welcome to Test api <br><br> To add word to dictonary:- modifie URL example with your choice <br> /add_word/word=example <br><br> for dict as below <br> /autocomplete/query=fo "

@app.route("/add_word/<string:word>")
def add_word(word):
    word = word.split("=") 
    
    if word[0] != 'word' or (len(word) > 2 ) or not (word[-1]).isalpha():
        return "use correct URL <br> It must be word=example format" 
    word = word[-1]
    word.lower()
    add_to_dic(word)
    return "added " + word

@app.route("/autocomplete/<string:query>")
def autocomplete(query):
    query = query.split("=")
    if query[0] != 'query' or (len(query) > 2 ) or not (query[-1]).isalpha():
        return "use correct URL <br> It must be query=fo format"
    query = query[-1]
    query.lower()

    res = find_match(query)
    return jsonify(res)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)  #host changes localhost to '0.0.0.0'