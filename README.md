# Social Engagement Overview
Make a Python app that acts as a comment management system like you would see on social media. The goal of the app is to act as an administrator suite, allowing the user to edit and delete comments.

# Specification 


Comment class: 
  Comments should have the following instance variables: text, likes, dislikes and is_flagged. 
  There should also be a function called print_info that prints out each of the comment's variables.

Question class should be a subclass of comment with 2 additional instance variables: 
  answer - this should be the answer to the question
  topic - this should be what the question is about. (i.e., Coding, Health, Gaming, etc.)
  Override the print_info function to also include the topic and answer to the question in addition to the variables from the Comment parent.


Directly in main, make a list of comments as well as several functions for crunching data about those comments.
