# AI Dummy Data Query WebApp

This project is a simple Flask web application that allows users to input natural language queries to retrieve data from a PostgreSQL database. The application uses OpenAI's GPT API to translate natural language queries into SQL queries, executes these queries on a PostgreSQL database, and displays the results in a simple interface.

## Prerequisites

- Python 3.7 or higher
- PostgreSQL database installed and running
- `psycopg2` library for PostgreSQL integration
- OpenAI API key
- Flask and its dependencies

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sergioantelo/ai_advanced_filtering.git
   cd data-query-webapp

2. **Activate the preloaded virtual environment**:
   ```bash
   source venv/Scripts/activate

3. **Import the SQL dump into your PostgreSQL database**:

   ```bash
    psql -U your_username -d your_database -f db_backup/employee_data.sql

4. **Configure OpenAI API key**:

   ```bash
    # Navigate to app.py and change it there
    openai.api_key = 'your_openai_api_key'

5. **Update database credentials**:

   ```bash
   # Navigate to app.py and update them there
    DB_NAME = 'your_database_name'
    DB_USER = 'your_database_user'
    DB_PASSWORD = 'your_database_password'

6. **Run the applicationUpdate database credentials**:

   ```bash
   python app.py

7. **ALTERNATIVE: You can test the same in the test folder**:

   ```bash
   python test/advanced_filtering_excel.py

## Usage

1. **Input queries**
    - Type natual language queries into the search bar.
    - Click the search button or press "Enter" to submit.

2. **View results**
    - The app will display the results retrieved from the database based on your query.

## Example Queries

- "List all employees earning more than 30000"
- "Show all engineers in the IT department"
- "Who are the employees in the Exploration department with a salary less than 25000?"
- "Give me all employees earning less than 20000 or working as an Engineer or working in IT"
- "Show all employees"
- "List all people working in sales and earning less than 20000"
