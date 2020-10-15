## How Do Design a Distributed Cache?
# A distributed cache is a cache which has its data spread across several nodes in a 
# (a) cluster, (b) across several clusters or (c) across several data centres located around the world.

## FEATURES
########################################
# Database Caching 
# User Session Storage, 
# In Memory Data Lookup,
# Potential to scale on demand & being highly available

## CONSTRAINTS
########################################
# Huge Sum of Key Value Storage
# Cache Invalidation
# Cache Eviction Policy
# Cache Concurrency
# Data Struture to allow fast retrieval of the data

## HIGH LEVEL DESIGN
########################################
# Read from main database and write in cache - 2 Operations
# Select one of the Eviction Policy - LRU, LFU, FIFO, LIFO, MFU
# Main Database + lookup, insert, delete and update functionality
# Distributed Caching Infra with Key Value Segregation

## LOW LEVEL DESIGN
########################################
# Eviction policy - LRU ca be build using doubly linked list or hash table
# Cache Concurrency should be balanced by shards + commit locks
# Cache functionalities - lookup, insert, delete and update 
# Distributed Cache - where volatile memory being used from different machines
 

## BOTTLENECKS
########################################
# Cache Miss
# Cost of the Infrastructure
# High Read/Write Operations