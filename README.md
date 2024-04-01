# department_head.messages

Overview:

Program Requirements:
Make a list of 5 ‘Department Head’ usernames, including an admin username. Create a loop through the list of usernames that prints:
○	A special greeting for the admin
○	Generic greeting for the remaining 4 usernames
Defined Scope:
●	Create a specialized greeting for the admin, upon login to the company’s intranet website
●	Create a generic greeting for the remaining 4 department heads, upon login to the company’s intranet website. 
Intended Usage:
To create a printed greeting for each Department Head that will appear after they have logged into the company's intranet website. 

Processing Logic:

Control of Program:
First, the Python program defines a list of 5 ‘department_heads’. Next the program enters a loop in the ‘department_heads’ list. After entering the loop, an ‘if-else’ statement is used to check to see if a ‘department_head’ is equal to ‘Admin’. If there is a ‘department_head’ that is equal to ‘Admin’ it prints a specific message for the Admin. If the ‘department_head’ is NOT equal to ‘Admin’ a generic printed message is printed for the remaining ‘deparment_heads’. 
PROGRAM ENDS.

Data Flow of Program:
●	INPUT: ‘department_heads’ list
●	OUTPUT: Special Greeting for Admin. Generalized greeting for remaining 4 department heads
(PDL) Process Design Language
○	Initialize a List Iteration of Department Heads
○	Print a message for each Department Head, including a specifically unique message for the Admin

Pseudo Code:
○	Define a list of Department Heads containing Department Names
○	For each  Department Head in Department Heads: 
■	If “Department Head” is equal to “Admin”: 
●	Print "Hello Systems Administrator, would you like to see the Status Report since your previous Login?"
■	All Else: 
●	Print a general greeting message for all other Department Heads

Flow Chart:
START
●	Define “Department Heads” list
●	For each “Department Head” in “Department heads”: 
○	If “Department Head” is ‘Admin’: 
■	Print "Hello Systems Administrator, would you like to see the Status Report since your previous Login?"
○	All Else: 
■	Print {Department Name} Department Lead, Let's have a Great day!")
END.

Subroutines/Methods/Functions:
No Subroutines or Functions are used in this Python program. This is a linear program that uses iteration and conditional logic. 

Data (INPUT/OUTPUT):

Element Descriptions:
‘Department_Heads’: A list containing the names of each department head
●	Type: List of Strings 
●	Dimension: 1-dimensional
‘Department_Head’ (inside the loop): Represents each department head during iteration
●	Type: String
●	Dimension: Scalar, individual string element
Relationships between Elements
●	‘Department_Heads’: structure containing multiple string elements, each representing a different department head. 
●	Inside the loop, ‘Department_Heads’: iterates over the ‘Department_Heads’ element, representing one department head at a time. 



Range of Possible Values:
●	Possible values in this Python Program are the strings representing each different department name with values changing on each iteration dependent on each department head in ‘Department_heads’. 
Initial Values of Each Element
●	‘Department_Heads’: ‘Admin’, ‘Marketing’, ‘Accounting’, ‘Human Resources’, ‘Legal’
●	(LOOP) ‘Department_Head’: First takes the value of ‘Admin’ in ‘Department_heads’, then iterates through the remaining ‘Department_Heads’. 

Software Components:
●	No classes or software components. Python program is a script with a loop, conditional statement, with a print function. 

UML Class Diagram:
●	Department_Head
○	Name: String
○	Greeting: String

Properties and Constraints:
●	‘Name’: String, represents the name of each department head. Constraints: Subject to each unique department name. 

Algorithms Defined in Processing Logic:
●	No specific algorithms are used

Testing:

Input Data:
●	‘Department_Heads’: ‘Admin’, ‘Marketing’, ‘Accounting’, ‘Human Resources’, ‘Legal’
Expected Output Data:
●	(‘Admin’): “Hello Systems Administrator, would you like to see the Status Report since your previous Login?”
●	(‘Marketing’, ‘Accounting’, ‘Human Resources’, ‘Legal’): “Welcome! (‘Marketing’, ‘Accounting’, ‘Human Resources’, Legal’) Department Lead, Let’s have a Great day!”
Success Criteria:
●	Prints correct greeting for ‘Admin’ department head
●	Prints generic greeting for all other department heads
●	Loop Iterates through all departments 
