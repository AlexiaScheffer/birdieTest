# Web scrapping technical test

the objective is web scrapping the following e-commerces: 
- Mercado Livre
- Magazine Luiza
- Casas Bahia

For that, there's 40k urls on offers.csv

I decided to use Scrapy framework because of the performance with numerous urls.

To execute, it's necessary to clone the project and:

 `` cd birdietest ``

 `` scrapy crawl storespider -a filename=offers.csv -O output.json``

or:

 `` scrapy crawl storespider -a filename=minioffers.csv -O minioutput.json ``
 
 
(I made one .csv smaller, just to test)
