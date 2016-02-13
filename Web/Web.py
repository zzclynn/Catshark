from flask import Flask, render_template

app = Flask(__name__)


# TODO  need add a search and button
# index.html page
@app.route('/')
def hello_world():
    return render_template('index.html')



# Post call for search
@app.route('/search', methods="POST")
def search(key):
    app.logger.debug("searching keywords")
    return ""

# show search results
@app.route('/results')
def showresult():
    return ""




if __name__ == '__main__':
    app.run()
