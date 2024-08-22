import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import re

# Function to parse cyclictest results
def parse_cyclictest_output(filename):
    data = {'user': [], 'kernel': [], 'irq': []}
    with open(filename, 'r') as file:
        for line in file:
            if re.match(r"^\s*\d+", line):
                parts = line.split()
                timestamp = int(parts[0])
                user_latency = int(parts[1])
                kernel_latency = int(parts[2])
                irq_latency = int(parts[3])
                data['user'].append((timestamp, user_latency))
                data['kernel'].append((timestamp, kernel_latency))
                data['irq'].append((timestamp, irq_latency))
    return data

# Convert the data to a DataFrame for easier plotting
def data_to_dataframe(data):
    df_user = pd.DataFrame(data['user'], columns=['Time', 'Latency']).set_index('Time')
    df_kernel = pd.DataFrame(data['kernel'], columns=['Time', 'Latency']).set_index('Time')
    df_irq = pd.DataFrame(data['irq'], columns=['Time', 'Latency']).set_index('Time')
    return df_user, df_kernel, df_irq

# Plot the data
def plot_latency(dataframes):
    plt.figure(figsize=(12, 6))
    
    # Plot user latency in red
    plt.plot(dataframes['user'].index, dataframes['user']['Latency'], color='red', label='User Latency')
    
    # Plot kernel latency in green
    plt.plot(dataframes['kernel'].index, dataframes['kernel']['Latency'], color='green', label='Kernel Latency')
    
    # Plot irq latency in blue
    plt.plot(dataframes['irq'].index, dataframes['irq']['Latency'], color='blue', label='IRQ Latency')
    
    plt.title('Cyclictest for Latency with Stress on PREEMPT_RT')
    plt.xlabel('Time (ms)')
    plt.ylabel('Occurences')
    plt.legend()
    plt.grid(True)
    plt.show()

# Read and parse the cyclictest results
data = parse_cyclictest_output('<Enter file name and path>') #enter file name and path to the file

# Convert the data to DataFrames
df_user, df_kernel, df_irq = data_to_dataframe(data)

# Plot the data
plot_latency({'user': df_user, 'kernel': df_kernel, 'irq': df_irq})