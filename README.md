# Chomsky-Conversion

## Quick DJango/Python Virtual Environment Notes

DJango Version: 5.0
Python Virtual Environment Version: 3.10.11

To start the django server:
    1. Activate the Python Virtual Environment (.venv) by running .venv\Scripts\activate
    2. Navigate to the DJango framework with 'cd chomsky_web'
    3. Then run 'python manage.py runserver'

## Table of Contents

- [Chomsky-Conversion](#chomsky-conversion)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [Built With](#built-with)
  - [Features](#features)
  - [Acknowledgements](#acknowledgements)

## Overview

The Chomsky-Conversion project aims to implement a conversion process that transforms a Context Free Grammar (CFG) into Chomsky Normal Form (CNF). CFGs are powerful language representations, but CNF simplifies the structure, making it easier for certain algorithms and parsers to operate.

### Built With

This project is developed using Python, a versatile programming language known for its extensive library support and documentation. Python is an excellent choice for handling structured data from JSON input files.

## Features

The Chomsky-Conversion program simplifies Context Free Grammars (CFGs) by converting them into Chomsky Normal Form (CNF). It accepts CFGs in JSON format as input and generates CNFs in JSON format as output. This conversion streamlines CFGs for use in various algorithms and parsers, achieved through functions that eliminate useless productions, handle ε (empty string) rules, remove unit productions, and manage diverse right-hand side combinations. Developed in Python, the program accommodates CFGs of varying complexity.

## Acknowledgements

Include credits to external resources, tutorials, or libraries that have been influential in understanding and implementing the Context Free Grammar to Chomsky Normal Form conversion. If you have specific resources or references you'd like to acknowledge, make sure to include them in this section as your project progresses.
