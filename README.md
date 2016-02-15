# Catshark

Description
-----------

Inspired by [Project Airbnb - Machine Learning of prediction](https://slack-files.com/T0GUEMKEZ-F0J4G9QTT-274d3bc97e), Catshark aims to help Homedepot to refine their search alogrithm using using a relevance rater. This tool, which based on machine learning technique, can predict a relevance score for a given pair of query term and search result in a simple click.


Plan
----

Based on our experiences on web development and descriptions metioned above, we take _Feb, 2016_ as the __1st stage__ with the __primary__ goal of __prototyping__ our own chat application following the [Development Guildlines](https://github.com/BitTigerNY/AraChat/edit/master/README.md#Development Guildlines) metioned below. Here're some tentative schedules.

* __[2016/02/01 - 2016/02/07]__ Project Selection, Plan Discussion, and Proposal Draft Writing
* __[2016/02/08 - 2016/02/24]__ System Design, Resource Discovery, Project Implementation, Document Writing 
* __[2016/02/25 - 2016/02/29]__ User Manual Writing and Video Presentation Making

_Details of each schedule and task will be added later._

Resource
--------

1. [BitTiger Project: Airbnb - Machine Learning of prediction](https://slack-files.com/T0GUEMKEZ-F0J4G9QTT-274d3bc97e)

Language & Framework
--------------------

### Python, Javascript, Flask
### [Flask Web Framework](http://flask.pocoo.org/)
Flask is a simple and lightweight Python web framework build for rapid development. In this project, we will use Flask web framework to build our Restful backend service. For [tutorials](http://flask.pocoo.org/docs/0.10/tutorial/) and [sample code](https://github.com/mitsuhiko/flask/tree/master/examples/flaskr/)

### [PyLucene](https://lucene.apache.org/)
Lucene is an open-source full-text search library which makes it easy to add search functionality to an application or website. In this project, we will use Lucene to build our search index based on Home Depot datasets. Some [tutorials](http://www.lucenetutorial.com/) for beginners can be found [here](http://www.lucenetutorial.com/). 

### [Python](https://www.python.org/)
We choose python as primary language for machine learning section. Python is a concise scripting language rich with various thrid-party libraries, including scientific computing stack: Numpy, Pandas, etc, and machine learning packages: scikit-learn, nltk.We plan to use Random forest, Xgboost, Bagging Regressor to train our model, and produce final results with ensembling. 

Development Guildlines
----------------------

- __Modularity.__ Following the principle _"loose coupling and high cohesion"_, each module should be standalone.

- __Minimalism.__ Each module should be kept short, simple, and concise. Every piece of code should be transparent upon first reading. 
- __Easy extensibility.__ New modules (as new classes and functions) are should be simply add, and existing modules should be extended easily.

Owner
-----

@team: Catshark
