import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("dataset_part_1.csv")

# Display dataset information
print(df.info())

# Missing values analysis
missing_percentage = (
    df.isnull().sum() / len(df) * 100
).sort_values(ascending=False)

print("\nMissing Values (%)")
print(missing_percentage)

# Launch site statistics
launch_site_counts = (
    df["LaunchSite"]
    .value_counts()
)

print("\nLaunch Site Distribution")
print(launch_site_counts)

# Orbit distribution
orbit_counts = (
    df["Orbit"]
    .value_counts()
)

print("\nOrbit Distribution")
print(orbit_counts)

# Landing outcome analysis
landing_counts = (
    df["Class"]
    .value_counts()
)

print("\nLanding Outcome Distribution")
print(landing_counts)

# Basic payload statistics
print("\nPayload Statistics")
print(df["PayloadMass"].describe())
