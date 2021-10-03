EMail Homework
===

Assignment
-
(Option 2) Write a program that maintains a list of “trusted” domains and takes as input an arbitrarily-sized list of other domains and a number. The function will check each input domain and if the Levenshtein distance is below the input number, list the domain as risky along with the domain that it is similar to and the distance.

Install
-
Activate environment
`source env/bin/activate`

Install package
`pip install -r requirements.txt`


Run
-
`python main.py`

Enter comma separated list of domains to check.
Enter number for the distance to check