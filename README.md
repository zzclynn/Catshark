# Catshark

Description
-----------

Inspired by [Project Airbnb - Machine Learning of prediction](https://slack-files.com/T0GUEMKEZ-F0J4G9QTT-274d3bc97e), Catshark aims to develop a platform to predict the relevance of search results from Home Depot.


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

### Java, Javascript, R
### [Spark Web Framework](http://sparkjava.com/)
Spark is a simple and lightweight Java web framework build for rapid development. In this project, we will use Spark web framework to build our Restful backend service. For [tutorials](https://sparktutorials.github.io/) and [sample code](https://github.com/perwendel/spark/blob/master/README.md#examples), for [begineers](https://sparktutorials.github.io/2015/08/04/spark-video-tutorials.html)
### [Handlebars](https://github.com/jknack/handlebars.java)
Handlebars is a powerful javascript template engine help you build front end web view without pain. In this project, we will use Handlebars.java which is a Java port of handlebars. The Spark template handlebars sample code you can found [here](https://github.com/perwendel/spark-template-engines/tree/master/spark-template-handlebars) 

### [Lucene](https://lucene.apache.org/)
Lucene is an open-source Java full-text search library which makes it easy to add search functionality to an application or website. In this project, we will use Lucene to build our search index based on Home Depot datasets. Some [tutorials](http://www.lucenetutorial.com/) for beginners can be found [here](http://www.lucenetutorial.com/). 


Development Guildlines
----------------------

- __Modularity.__ Following the principle _"loose coupling and high cohesion"_, each module should be standalone.

- __Minimalism.__ Each module should be kept short, simple, and concise. Every piece of code should be transparent upon first reading. 
- __Easy extensibility.__ New modules (as new classes and functions) are should be simply add, and existing modules should be extended easily.

Owner
-----

@team: Catshark