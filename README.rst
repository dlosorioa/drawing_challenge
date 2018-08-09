=================
drawing_challenge
=================


Huge - Coding Challenge


Description
===========

Not just another command line drawing tool.

Build as a extensible python package to which more tools can be added


Note
====

This project has been set up using PyScaffold 3.0.3. For details and usage
information on PyScaffold see http://pyscaffold.org/.



Instructions
====

This code challenge was developed in Python. Using PyScaffold to setup a quick easy to use dev environment including unit testing and python packaging.

1 - Make sure to have Python installed

	- https://www.python.org/downloads/
	- https://docs.python-guide.org/starting/installation/

2 - Install requirements: 

	>> pip install -r requirements.txt

3 - To complete the setup of the app, run this command:

	>> python setup.py develop

4 - By the instructions, the drawing tool reads commands from a text file, and deliver the output in another text file.
	By default, input and output files are in files folder:

	- Input file: files/input/default.txt

	- Output file: files/output/default.txt

5 - In order to run this project use the following command:

	>> python src/drawing_challenge/skeleton.py [-h] [--version] [-in [input]] [-out [output]] [-v] [-vv]

6 - This project has unit test coverage close to the 80%, mainly focused on the expected results per the input commands. 
	Run the test using:

	>> python setup.py test

