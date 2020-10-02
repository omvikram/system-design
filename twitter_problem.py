## “Design a simplified version of Twitter where people can post tweets, 
# follow other people and favorite tweets.”

## FEATURES
########################################
## posting new tweets
## following a user
## favoriting a tweet
## displaying data about users and tweets

## CONSTRAINTS
########################################
## 10 million users
## 10 million tweets per day
## 20 million tweet favorites per day
## 100 million HTTP requests to the site
## 2 billion “follow” relations
## Some users and tweets could generate an extraordinary amount of traffic

## HIGH LEVEL DESIGN
########################################
## Load Balacer
## Nginx
## Memcached
## MySQL (Master - Slave)

## HIGH LEVEL DESIGN
########################################
## DB SCHEMA - users, tweets, connections, favorites
## REST APIs - GET, PUT, POST

## BOTTLENECKS
########################################
## High volume data - DB Shardig, DB Partition
## Increased Traffic - ELB, CDN
