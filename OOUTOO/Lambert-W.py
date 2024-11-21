import numpy as np
from scipy.special import lambertw

# Calculate ln(4)
ln_4 = np.log(4)

# Apply the Lambert W function
w_value = lambertw(-ln_4)

# Compute x using the complex value from the Lambert W function
x_solution = np.exp(-w_value)

# Display the results, including both real and imaginary parts
print(x_solution)
