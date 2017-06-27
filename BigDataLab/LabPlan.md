# Functional Distributed Big Data Processing

## Syllabus Mapping

AQA:

	* 4.11 Big Data
		- volume – too big to fit into a single server
		- Know that when data sizes are so big as not to fit on to a single server:
			+ the processing must be distributed across more than one machine
			+ functional programming is a solution, because it makes it easier to write correct and efficient distributed code.
	* 4.12.2.1 Functional language programs
		- Show experience of constructing simple programs in a functional programming language.
		- Have experience of using the following in a functional programming language:
			+ map
			+ filter
			+ reduce

# Learning Outcomes

Having completed this practical, students will be able to: 

	* demonstrate understanding some of the challenges associated with big data and distributed data processing
	* demonstrate practical use of `map`, `reduce`, `filter` and `sort` in a functional programming language
	* show experience writing functions for distributed processing



## Dev Notes

	* Need to have a set of distributed data on a set of servers
	* Want to be able to run data-local processing on that
		- set of heroku apps with different data using node?


## Warm-up Exercise

	* Form teams
	* Each team is issued with a stack of cards with text on them
	* The team must come up with a way of counting the number of occurrences of each word, and then sorting those by decreasing occurrence count within a time-limit of say 10 mins
	* Discussion: 
		- how did each team choose to do the task? 
		- was the work split up equally?
		- how did the team specifically deal with the problem of combining counts from each document?

## Programming Exercise 1: counting words in a string

	* Write a Javascript function to count the occurrences of each word in a document stored in a string, and store the result in a dictionary

## Programming Exercise 2a: counting words in a many strings

	* Use a loop to apply that function to an array of strings and store the results in an array

## Programming Exercise 2b: counting words in a many strings using map
	
	* Use the map function to do the same

## Programming Exercise 3: merging counts

	* Write a Javascript function to merge and sort the counts from multiple strings

## Programming Exercise 4: aggregating counts

	* Write a Javascript function reduce the set of merged counts to their totals, and then print them sorted by decreasing counts

## Pause for reflection; what happens if we have "Big Data"? 
	
	* Consider the computational and data transfer costs of "pull" versus "push" computation

## Programming Exercise 5: Exploring pull-computation

	* Considering distributed data, use the pull-method to compute the counts & the cost

## Programming Exercise 6: Exploring push computation

	* Considering distributed data, use the push-method to compute the counts & the cost

## Wrap-up

	* Cover key take-away messages




