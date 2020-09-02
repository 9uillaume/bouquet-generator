# bouquet-generator
Bloomon technical challenge

Small app made in few hours to generate bouquets from data input giving bouquet designs and flowers to make them.

### To run it

###### Docker

You can use the available Docker image to get the desired Python version and it will run by default with `sample.txt` given data input for the challenge, can be modifiied in Dockerfile.

Steps:

- `docker build .` builds image from Dockerfile for the app
- `docker run <built image>` runs Docker image freshly built

###### Locally

If you have Python 3.7 on your machine, but everything 3.5+ should be good, you can simply pipe data input into running the Python script as:
`cat sample.txt | python app.py`

Otherwise to use it as a CLI you can simply run the script and give data inputs manually:
`python app.py`



### Improvements

This test was made under a rush of making it work, breaking down into methods and proper naming of variables to not be messy and keep it clear. Steps in mind now that it's done to improve:

- Now we save data inputs parsed such as bouquet designs and flowers in the app memory on the fly in global variable to go faster, might be better to persist it somewhere for clarity, more flexible use, and enjoy a storage methods to filter, extract data you want. Key Value would work like a charm like Redis or some NoSql Mongo/Dynamo
- The flowers incoming are kind of a cornerstone it will define which bouquet will be made in priority, first bouquet design in => more chance to be made cause we compensate missing extra flowers with flowers from other potential bouquets, today I take a flower of each to reach total and make it fair for next bouquets
- Outside of the core :point_up: of the logic, for better clarity with more time I could see some Object Oriented Programing with some nice classes in different files, getting some air in this main file, better readability and maintain
- Unit tests? never hurts, considered TDD for this one but with limited time preferred to run straight into it by designing in paper how it will look