import pandas as pd

# Create a larger dummy dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack", "Kara", "Leo", "Mona", "Nick", "Olivia", "Paul", "Quincy", "Rita", "Steve", "Tina"],
    "Salary": [25000, 18000, 22000, 17000, 21000, 20000, 30000, 19000, 16000, 23000, 15000, 31000, 27000, 18000, 24000, 26000, 28000, 29000, 21000, 20000],
    "Position": ["Engineer", "Designer", "Engineer", "Manager", "Analyst", "Engineer", "Developer", "Developer", "Prospector", "Engineer", "Analyst", "Manager", "Designer", "Prospector", "Engineer", "Manager", "Analyst", "Developer", "Prospector", "Engineer"],
    "Department": ["Development", "Marketing", "Development", "Sales", "Finance", "Development", "IT", "IT", "Exploration", "Development", "Finance", "Management", "Marketing", "Exploration", "Development", "Sales", "Finance", "IT", "Exploration", "Development"]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel("dummy_data.xlsx", index=False)
