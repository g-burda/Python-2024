#Excercise 10_2
import pandas as pd
import numpy as np

days_in_May = pd.Series(pd.date_range("2024-05-01", periods=31, freq="D"))
random_temperatures = np.random.randint(0, 40, size=len(days_in_May))
temperatures_in_May = pd.Series(random_temperatures, index=days_in_May)

print(temperatures_in_May)



#Excercise 10.3
import pandas as pd

data_periodic_table = {
    'Name': ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium'],
    'Symbol': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca'],
    'Weight': [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 14.007, 15.999, 18.998, 20.180, 22.99, 24.305, 26.982, 28.086, 30.974, 32.065, 35.453, 39.948, 39.098, 40.078]
}

periodic_table = pd.DataFrame(data_periodic_table, index=range(1, 21))

print(periodic_table)