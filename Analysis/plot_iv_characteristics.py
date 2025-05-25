
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel('Data/IV_Data_Charted.xlsx', sheet_name='Data')


# Plot Transfer Characteristics
plt.figure(figsize=(8, 6))
plt.plot(df['Gate V (V)'], df['Drain I (μA)'], marker='o', linestyle='-', linewidth=1, color='orange')

# Titles and labels
plt.title('GFET Transfer Characteristics')
plt.xlabel('Gate Voltage (V)')
plt.ylabel('Drain Current (μA)')
plt.grid(True)
plt.tight_layout()

# Save the plot

plt.show()
