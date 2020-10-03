## How Do Search Engines Work?

## FEATURES
########################################
# Every search engine has three main functions: 
# Crawling (to discover content), 
# Indexing (to track and store content), and 
# Retrieval (to fetch relevant content when users query the search engine).

## CONSTRAINTS
########################################
# Find out the world wide web pages to crawl
# How to index the keywords and the web page urls
# The retrieval of the data should be fast
# The search result should point to web and mob web urls
# Infrastructure to support the same
# Highly scalabale database to keep the mapping

## HIGH LEVEL DESIGN
########################################
# Crawling - Need to build a crawler or a bot or spider which crawls the web pages
# Finds out the links in the page and keeps it for mapping
# Respect nofollow and robots.txt while crawl every page in sitemap
# Indexing - Each link which is crawled should be mapped with the keywords
# This should be kept in a distributed database system
# We might need to cache few frequent keyword results using the edges
# Retrieval - fething the results based on keywords so Retrieval Algo has to be defined
# This should be implemented as business logic in the API which then retrieves the web pages.

## LOW LEVEL DESIGN
########################################
# Crawler > scheduled tasks build in any language which supports multi threading
# Crawler > scheduled tasks to mark valid/invalid web pages and update the keywords mapping
# Indexing > Google uses BigTable with multiple DB partitions and Tablet Servers to lookup
# Indexing > For indexing we need to set up partitions and a lookup DB for the partitios itself
# Retrieval > Rest APIs with frequet cache lookup 
# Retrieval > CDN network should be used here

## BOTTLENECKS
########################################
# Semantics of the crawled pages
# faster search across all regions