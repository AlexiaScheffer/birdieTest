# Web scrapping technical test

the objective is web scrapping the following e-commerces: 
- Mercado Livre
- Magazine Luiza
- Casas Bahia

For that, there's 40k urls on offers.csv

I decided to use [Scrapy](https://scrapy.org/) framework because of the performance with numerous urls.

For the code to work it is necessary:
- to clone the project
- `` pip install -r requirements.txt ``
- install mongo and pymongo

And then, execute the spider:
- going to the spider folder:
 `` cd birdietest ``

- and executing the command with all the urls:
 `` scrapy crawl storespider -a filename=offers.csv -O output.json &> logs.log``

- or with a sample of urls for testing purposes:
 `` scrapy crawl storespider -a filename=minioffers.csv -O minioutput.json &> logs.log ``
 
It is created a file named logs.log which we can look the scrapy outputs

After running the Scrapy spider, you are allowed to consult the database. It was used MongoDB to the database. 

To initiate the mongo shell on default port (27017), you can run:

`` mongo ``

Then to switch to implemented database, you need to run:

`` use birdietest ``

It's now possible to do CRUD operations. 
The mongo shell CRUD operations can be consulted by [here](https://docs.mongodb.com/manual/crud/).
