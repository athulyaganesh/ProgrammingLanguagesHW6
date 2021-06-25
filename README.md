# ProgrammingLanguagesHW6

This is Group 8's solution for the Producer Consumer Multithreading problem for CS 3003. We attempted our solution in Python. 

We have used four classes- 
a. Item
b. ItemQueue
c. Producer 
d. Consumer 
e. We also used a main function. 

Description of each Class is as follows: 
1. Item- A simple class, created to be able to store each item in the queue. Each Item object will consist of an Id and a producer name, and has methods to return both of them. 
2. ItemQueue- This class consists of a list. We are able to "put" elements of type Item, into the list, or take them out as needed. 
3. Producer- This class Produces new items in an infinite while loop, and adds them to an ItemQueue type.
4. Consumer- This class removed items from the ItemQueue type and displays the ID and Name on screen. 
5. Main- We used the main to create 2 producers and 3 consumers(as the question specifies), and have them produce and consume items in a concurrent manner, using multiple threads. 
