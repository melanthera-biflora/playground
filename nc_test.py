import netCDF4
import matplotlib.pyplot as plt
import numpy as np

# Open the NC file
dataset = netCDF4.Dataset('C:/Users/C837516128/TerraClimate_ppt_2021.nc', 'r')  # 'r' mode for read-only

# Print information about the file
print(dataset)
# Access the latitude, longitude, and precipitation variables
lat = dataset.variables['lat'][:]
lon = dataset.variables['lon'][:]
ppt = dataset.variables['ppt'][:]
# Check the shape of ppt to confirm it matches the dimensions (12, 4320, 8640)
print(ppt.shape)
# Get precipitation data for the first time step
ppt_time_step_1 = ppt[0, :, :]  # First time step (e.g., January)
print(ppt_time_step_1)


# Plot the first time step of precipitation data
plt.figure(figsize=(10, 6))
plt.imshow(ppt_time_step_1, cmap='viridis', aspect='auto')
plt.colorbar(label='Precipitation (mm)')
plt.title('Precipitation for First Time Step (January)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


# Close the dataset after use
dataset.close()