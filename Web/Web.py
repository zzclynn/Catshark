from flask import Flask, render_template, request

app = Flask(__name__)


# TODO  need add a search and button
# index.html page
@app.route('/')
def index():
    queryString = request.args.to_dict()
    query = queryString.get('query') # get query parameter
    if (query != None):   # check query para is None
        result = searchIndex(query)

        return render_template('result.html')  # search the keyword in index
    else:
        return render_template('index.html')


# show search results
@app.route('/results')
def showresult():
    return ""



# build index use pyLucene

def createIndex():pass

def searchIndex(query):pass


if __name__ == '__main__':
    app.run()
