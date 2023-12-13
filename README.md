## CLI - Construction Sites Salary Management System

This is a Command Line Interface (CLI) application implemented using Python. The application is made for managing salary records for casual laborers in the construction industry. It is a user-friendly interface for construction site administrators to input, update, and view salary records seamlessly. The application adheres to best practices bacause it utilizes a database modified by SQLAlchemy ORM and a well-maintained virtual environment using Pipenv.

## Features

1. Salary Record Management: a user-friendly interface for construction site administrators to input, update, and view salary records seamlessly.The system will also facilitate efficient sorting and retrieval of payment information, empowering construction companies to manage payroll effortlessly.
2. Casual Laborer Information Management: management of essential details about casual laborers, such as contact information, job roles, and work history.
3. Payment Tracking: provide real-time insights into financial transactions, allowing construction companies to monitor payment status and history.
4. Security and Confidentiality: to safeguard the confidentiality and integrity of both salary records and laborer information.
5. Ease of Integration:for seamless integration with existing construction site management tools or databases, ensuring minimal disruption to established workflows.

## Benefits

+ Beyond salary records, the system contributes to a holistic approach to workforce management by consolidating laborer information, streamlining administrative tasks.
+ The automated functionalities will save time and resources, allowing construction companies to focus on core activities rather than manual bookkeeping.
+ The CLI-based system enhances transparency in salary-related processes, fostering trust between construction companies and casual laborers.

## Installation

1. Fork and clone the repository

   *** git clone <link> ***

2. Activate Pipenv virtual environment

   ** pipenv shell **

3. Install dependencies using pipenv

   ** pipenv install **

## Usage

- Help menu

    python3 app.py --help

- Add a New worker

   python3 app.py add-worker

- Add Salary 

    python3 app.py update

- list workers

    python3 app.py list-workers

- delete worker

    python3 app.py <worker.id>


## Contributions

Feedback on what can be improved is much welcome

## Acknowledgements

+ Click and Python
+ Sqlalchemy



