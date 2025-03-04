import pandas as pd

# Load the data from the CSV file
data_df = pd.read_csv('prediction_results.csv')

# Initialize a list to store the results
results = []

# Function to calculate the percentage increase
def calculate_percentage_increase(param):
    measured_pre = data_df[(data_df['Parameter'] == param) & (data_df['Type'] == 'Measured') & (data_df['Time'] == 'Pre')]['Value']
    measured_post = data_df[(data_df['Parameter'] == param) & (data_df['Type'] == 'Measured') & (data_df['Time'] == 'Post')]['Value']
    simulated_pre = data_df[(data_df['Parameter'] == param) & (data_df['Type'] == 'Simulated') & (data_df['Time'] == 'Pre')]['Value']
    simulated_post = data_df[(data_df['Parameter'] == param) & (data_df['Type'] == 'Simulated') & (data_df['Time'] == 'Post')]['Value']
    
    if len(measured_pre) == 1 and len(measured_post) == 1 and len(simulated_pre) == 1 and len(simulated_post) == 1:
        measured_increase = ((measured_post.values[0] - measured_pre.values[0]) / measured_pre.values[0]) * 100
        simulated_increase = ((simulated_post.values[0] - simulated_pre.values[0]) / simulated_pre.values[0]) * 100
        results.append([param, 'Percentage Increase', measured_increase, simulated_increase])
    
# Perform percentage increase calculation for each parameter
parameters = data_df['Parameter'].unique()
for param in parameters:
    calculate_percentage_increase(param)

# Convert results to DataFrame
results_df = pd.DataFrame(results, columns=['Parameter', 'Metric', 'Measured Percentage Increase', 'Simulated Percentage Increase'])

# Save results to CSV
results_df.to_csv('percentage_increase_results.csv', index=False)

print("Percentage increase results have been saved to 'percentage_increase_results.csv'.")
