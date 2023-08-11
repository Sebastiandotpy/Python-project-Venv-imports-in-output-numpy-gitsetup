*Exercise Project: Virtual Environment, Absolute Imports, Input/Output, NumPy, and Git Setup*
*Objective:* This exercise project combines the use of a virtual environment, absolute imports for organized code structure, input/output operations, NumPy calculations, and setting up a Git repository with proper ignore rules.
*Instructions:*
*Part 1: Virtual Environment Setup*
1. Create a new directory for your project: MyProject.
2. Inside MyProject, create a virtual environment named venv using the following command:
   python -m venv venv
   
3. Create a .gitignore file in the MyProject directory and add the following lines to ignore the venv directory:
   venv/
   
4. Activate the virtual environment:
   - On Windows: venv\Scripts\activate
   - On macOS and Linux: source venv/bin/activate
*Part 2: Absolute Imports, Package Structure, and Input/Output*
1. Inside the MyProject directory, create a package named my_package with the following structure:
   MyProject/
   ├── venv/
   ├── my_package/
   │   ├── __init__.py
   │   ├── module_a.py
   │   └── subpackage/
   │       ├── __init__.py
   │       └── module_b.py
   ├── main.py
   └── io_operations.py
   
2. In module_a.py, define a function named greet_module_a() that returns the string "Greetings from Module A!".
3. In module_b.py inside the subpackage, define a function named greet_module_b() that returns the string "Greetings from Module B!".
4. In the main __init__.py of my_package, import greet_module_a() and greet_module_b().
5. In main.py, import and call the functions from the my_package.
6. In io_operations.py, use functions from my_package to:
   - Import the functions from my_package.
   - Write the output of greet_module_a() and greet_module_b() to a file named output.txt.
   - Read the contents of the output.txt file and print them.
*Part 3: Install NumPy and Perform Calculations*
1. Activate your virtual environment as mentioned earlier.
2. Install NumPy using pip:
   pip install numpy
   
3. Update the subpackage module module_b.py in the my_package as follows:
python
   # my_package/subpackage/module_b.py
   import numpy as np

   def greet_module_b():
       return "Greetings from Module B!"

   def perform_calculations():
       numbers = np.array([1, 2, 3, 4, 5])
       sum_numbers = np.sum(_____)
       average = np.___(_____) # research the numpy method of the average
       return sum_numbers, average
   
4. In io_operations.py, add an import for the perform_calculations() function as mentioned earlier.
5. Run the io_operations.py script to see the results.
*Part 4: Git Setup and Requirements*
1. Initialize a Git repository in the MyProject directory:
   git init
   
2. Create a requirements.txt file by using the following command:
   pip freeze > requirements.txt
   
*Part 5: Stage, Commit, and Push to Git*
1. Stage all the files in your project for commit:
   git add .
   
2. Commit the staged changes with a meaningful message:
git commit -m "Initial setup"
