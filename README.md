# SQLite
 __Introduction__ 

 The purpose of this project is, to show how to create a sample database in SQLite in Python. 
 The database contains tables with different information about students in a language school.
 The statistics for various aspects are then displayed in Tableau Public.

 
__Libraries used:__
- sqlite3
- pandas
- random
- secrets
- string
- hashlib
- os

__Steps:__

1. Create the table student_info containing information about student names, the dates of the course, 
English level, teacher, room and whether the student is returning or not by manually inputting sample data

2. Generate random emails based on student names by using random library and save the results in a new table

3. Repeat the process to generate random attendance

4. Generate random passwords and encrypt them

5. Add all the tables to the dataframe

6. Explore the data

7. Visualise statistics of student's information in Tableau

   _Preview:_
![Dashboard 1](https://github.com/cherniad/SQLite/assets/129260187/47778882-efd7-49d7-877c-fa56b12cb451)


   _Link:_ 
https://public.tableau.com/app/profile/daria.cherniaeva/viz/students_17057895693510/Dashboard1

__Results and Learning Outcomes__ 

The code could be used to store information about the students or employees at the company. 
While creating a database, I noticed that if the database were larger and contained people 
with the same names, it would be beneficial to add the primary key. In this case, while generating 
the emails, we could add the condition to append a number after each string, in case of the same name
but different keys. 
