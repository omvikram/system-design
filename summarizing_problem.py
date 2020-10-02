# "In our company we already have developed a great library that can be used to summarize text articles. 
# Just feed it the whole text and it will return a decent summary that is just a few sentences long.

## FEATURES
########################################
# We need to put this in production and make it scalable. We expect that our customers will submit 
# text articles from our mobile app and also from our website.
# The library currently takes between 0.1 and 5 seconds to summarize an article. 
# You need to design a system that uses our existing library and allows users to 
# submit text articles through the mobile app and through the website.
# We anticipate that this service will be used around 1 million times a month. 
# Our desire is to not respond in more than 10 seconds to each request."

## CONSTRAINTS
########################################
# The expected monthly requests are around 1 million
# There should be at most 50 requests per second but the architecture 
# should easily be expandable to handle more than that, if needed
# Responses should not take more than 10 second, with the summarization library 
# possibly taking 5 seconds to do its job
# The summaries will be presented to the users asynchronously, meaning 
# that we will not wait for the summary to be in the HTTP response that comes after the initial HTTP request

## HIGH LEVEL DESIGN
########################################
# Multiple Clients - Web, Apps etc
# Summarizing Service - Exposed API under ELB
# Store the input/output in Database

## HIGH LEVEL DESIGN
########################################
# Multiple Clients - Web, Apps etc
# Wrapper APIs - Exposed API under ELB
# Messaging Queue - RabbitMQ/Kafka
# Summarizing Service Consumers
# Store the input/output in Database


## BOTTLENECKS
########################################
# Asynchronous Processing
# Messaging Queue Scalibility
# Caching for faster response for already processed data
