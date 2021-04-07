# Web scrapping technical test

the objective is web scrapping the following e-commerces: 
- Mercado Livre
- Magazine Luiza
- Casas Bahia

For that, there's 40k urls on offers.csv

I decided to use [Scrapy](https://scrapy.org/) framework because of the performance with numerous urls.

To execute, it's necessary to clone the project and:

 `` cd birdietest ``

 `` scrapy crawl storespider -a filename=offers.csv -O output.json``

or:

 `` scrapy crawl storespider -a filename=minioffers.csv -O minioutput.json ``
 
 
(I made one .csv smaller, just for tests)

After running the Scrapy spider, you can consult the database. It was used MongoDB to the database. 

To initiate the mongo shell on default port (27017), you can run:

`` mongo ``

Then to switch to implemented database, you need to run:

`` use birdietest ``


It's now possible to do CRUD operations. The mongo shell CRUD operations can be consulted by [here](https://docs.mongodb.com/manual/crud/).
