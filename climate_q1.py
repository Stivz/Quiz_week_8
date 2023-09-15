import sqlite3
import matplotlib.pyplot as plt

# Initialize empty lists
years = []
co2 = []
temp = []

# Connect to the SQLite database (replace 'your_database.db' with the actual database file path)
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

# Execute an SQL query to fetch data from the database
cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData")

# Fetch all the rows returned by the query
data = cursor.fetchall()

# Populate the lists
for row in data:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

# Close the database connection
conn.close()

# Create subplots and plot the data
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

plt.show()
plt.savefig("co2_temp_1.png")