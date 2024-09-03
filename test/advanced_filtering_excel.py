import openai
import pandas as pd

openai.api_key = 'your_openai_api_key'

excel_file_path = "dummy_data.xlsx"
df = pd.read_excel(excel_file_path)

def get_filter_expression(query):
    prompt = f"""
    You are an expert data assistant. Your task is to translate a natural language query into a Pandas DataFrame filtering expression.
    Example queries and their expressions:
    1. "Give me the people who have a higher salary than 25000" -> df[df['Salary'] > 25000]
    2. "Show me all engineers in the IT department" -> df[(df['Position'] == 'Engineer') & (df['Department'] == 'IT')]
    3. "List people who have a salary below 30000 and are not in HR" -> df[(df['Salary'] < 30000) & (df['Department'] != 'HR')]
    
    Now, convert this query into a DataFrame filtering expression:
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
    
    return completion.choices[0].message.content

def filter_data(df, filter_expression):
    try:
        filtered_df = eval(filter_expression)
        return filtered_df
    except Exception as e:
        print(f"Error executing filter expression: {e}")
        return pd.DataFrame()

def generate_response(filtered_df, query):
    if filtered_df.empty:
        return "Please try again... No matches found."
    
    data_string = ", ".join(filtered_df['Name'].tolist())
    prompt = f"""
    You are provided with a dataset of employee names that match a specific query.
    
    Query: '{query}'
    
    The following names match this query: {data_string}.
    
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

while True:
    user_query = input("Enter your query (or type 'exit' to quit): ")
    if user_query.lower() == 'exit':
        break
    
    filter_expression = get_filter_expression(user_query)
    print(f"Generated filter expression: {filter_expression}")

    filtered_df = filter_data(df, filter_expression)
    
    response = generate_response(filtered_df, user_query)
    print("\nResponse:\n", response)

