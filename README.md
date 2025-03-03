# nc_test: TerraClimate NC File Testing and Visualization

This script demonstrates how to load and visualize precipitation data from a TerraClimate NetCDF file using `netCDF4` and `matplotlib`.

## Requirements
- `netCDF4`
- `matplotlib`
- `numpy`

Install dependencies:
```bash
pip install netCDF4 matplotlib numpy
```

## Overview
- Opens the TerraClimate `.nc` file containing precipitation data for 2021.
- Extracts latitude, longitude, and precipitation (`ppt`) variables.
- Displays the precipitation data for the first time step (January) using a heatmap.

## How to Use
1. Update the file path to your `.nc` file.
2. Run the script to view the dataset and plot the January precipitation data.

## Output
A plot of precipitation data for January is displayed, and dataset details are printed in the console.
