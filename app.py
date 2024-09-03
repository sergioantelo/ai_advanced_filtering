from flask import Flask, render_template, request
import psycopg2
import openai

app = Flask(__name__)

openai.api_key = 'your_openai_api_key'

DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'your_database_name'
DB_USER = 'your_database_user'
DB_PASSWORD = 'your_database_password'

def get_sql_query(query):
    prompt = f"""
    You are a data assistant. Your task is to translate a natural language query into a pure SQL query for a PostgreSQL database. 
    Use the following exact case-sensitive column names: 'Name', 'Salary', 'Position', 'Department'. 
    Do not include any explanation or additional text, just the SQL query itself.
    
    Example queries and their SQL translations:
    1. "Give me the people who have a higher salary than 25000" -> SELECT "Name" FROM employees WHERE "Salary" > 25000;
    2. "Show me all engineers in the IT department" -> SELECT "Name" FROM employees WHERE "Position" = 'Engineer' AND "Department" = 'IT';
    3. "List people who have a salary below 30000 and are not in HR" -> SELECT "Name" FROM employees WHERE "Salary" < 30000 AND "Department" != 'HR';
    
    Now, convert this query into an SQL query:
    '{query}'
    """
    
    completion = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "assistant", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.0
    )
    
    sql_query = completion.choices[0].message.content

    # Strip any additional text that may precede or follow the SQL query
    sql_query_lines = sql_query.split('\n')
    for line in sql_query_lines:
        if line.strip().upper().startswith("SELECT") or line.strip().upper().startswith("DELETE") or line.strip().upper().startswith("INSERT") or line.strip().upper().startswith("UPDATE"):
            return line.strip()
    
    return sql_query

def execute_sql_query(sql_query):
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        
        cursor = connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        return [row[0] for row in result]
    
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return []
    
    finally:
        if connection:
            cursor.close()
            connection.close()

def generate_response(names, query):
    if not names:
        return "Please try again... No matches found."
    
    prompt = f"""
    You are provided with a dataset of employee names that match a specific query.
    
    Query: '{query}'
    
    The following names match this query: {names}.
    
    Using this information, respond with a concise sentence that lists the names matching the query.
    """
    
    completion = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "assistant", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.0
    )
    
    return completion.choices[0].message.content

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        user_query = request.form['query']
        sql_query = get_sql_query(user_query)
        names = execute_sql_query(sql_query)
        response = generate_response(names, user_query)
    
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)