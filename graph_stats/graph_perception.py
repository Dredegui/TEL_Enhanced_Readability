import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# File paths
results_path = "C:\\Users\\guipa\\OneDrive\\Documentos\\GitHub\\TEL_Enhanced_Readability\\human_study\\"
graph_path = "C:\\Users\\guipa\\OneDrive\\Documentos\\GitHub\\TEL_Enhanced_Readability\\graph_stats\\"
original_file = results_path + "original_text_results.xlsx"
enhanced_file = results_path + "enhanced_text_results.xlsx"

# Define custom colors for categories
second_custom_colors = {
    1: "#d73027",  # Red
    2: "#fc8d59",  # Orange
    3: "#fee08b",  # Yellow
    4: "#d9ef8b",  # Light Green
    5: "#91cf60"  # Green
}

# 5 colors: Yellow through Red with Orange as the middle color
custom_colors = {
    1: "#FFFF00", # Yellow
    2: "#FFC300", # Golden Yellow
    3: "#FF5733", # Orange
    4: "#C70039", # Red-Orange
    5: "#900C3F"  # Red
}


missing_info_colors = {
    "No": "#d73027",     # Red
    "Maybe": "#fee08b",  # Yellow
    "Yes": "#1b7837"     # Green
}

pastel_missing_info_colors = {
    # Orange, Yellow, Green
    "No": "#fc8d59",     # Orange
    "Maybe": "#fee08b",  # Yellow
    "Yes": "#91cf60"  # Green  
}


# Load the data
original_df = pd.read_excel(original_file, sheet_name="Sheet1")
enhanced_df = pd.read_excel(enhanced_file, sheet_name="Sheet1")

# Select relevant columns
readable_col = "How was the readability of the text?"
understandable_col = "How understandable was the content of text?"
missing_info_col = "Did you feel the some content was missing?"

# Function to process rating data
def process_ratings(df, category):
    return df[category].value_counts().sort_index()

# Process data for readability and understandability
readable_original = process_ratings(original_df, readable_col)
readable_enhanced = process_ratings(enhanced_df, readable_col)
understandable_original = process_ratings(original_df, understandable_col)
understandable_enhanced = process_ratings(enhanced_df, understandable_col)

# Process data for missing information
missing_info_original = process_ratings(original_df, missing_info_col)
missing_info_enhanced = process_ratings(enhanced_df, missing_info_col)

# Function to plot stacked bars with "Original" and "Enhanced" on the y-axis
def plot_stacked_bars(df, labels, title, ax, color_map):
    # Ensure ratings are in the correct order
    df = df[labels]

    sample_sizes = [f"{label}\n(n = {int(abs(df.loc[label]).sum())})" for label in df.index]
    df.index = sample_sizes
    print(df.head())
    colors = [color_map[label] for label in color_map.keys()]
    # Plot stacked bars
    df.plot(kind="barh", stacked=True, color=colors, ax=ax, width=0.6)
    ax.axvline(0, color="black", linewidth=1) # Add central reference line at zero
    ax.set_title(title)
    ax.set_xlabel("Count")
    ax.set_ylabel("Text Type")
    ax.legend(title="Ratings", loc="upper right")

def plot_manual_stacked_barh(df, labels, title, ax, color_map):
    df = df[labels]  # Ensure correct order of ratings
    sample_sizes = [f"{label}\n(n = {int(abs(df.loc[label]).sum())})" for label in df.index]
    df.index = sample_sizes
    
    y_positions = np.arange(len(df))  # Positioning for bars
    # Add values from 1 and 2 ratings
    left_positions = (df[1].values + df[2].values) *-1  # Initialize left start positions
    print(df.head())
    for label in labels:
        values = df[label].values
        color = color_map[label]
        print(f"Plotting {label}: y_positions={y_positions}, values={values}, left_positions={left_positions}, color={color}")
        ax.barh(y_positions, values, left=left_positions, color=color, label=label, height=0.6)
        left_positions += values  # Update left positions for stacking

    
    ax.axvline(0, color='black', linewidth=1)  # Central reference line
    ax.set_yticks(y_positions)
    ax.set_yticklabels(df.index)
    ax.set_title(title)
    ax.set_xlabel("Count")
    ax.set_ylabel("Text Type")
    ax.legend(title="Ratings", loc="upper right")
    print(ax)

# Create the first figure (Readability & Understandability)
fig, ax = plt.subplots(figsize=(16, 9))
df = pd.DataFrame({"Original Readability": readable_original,
                   "Enhanced Readability": readable_enhanced,
                   "Original Understandability": understandable_original,
                   "Enhanced Understandability": understandable_enhanced
                   }).fillna(0)
df = df.T  # Transpose to have "Original" and "Enhanced" on y-axis

#df[[1, 2]] *= -1 # Invert the negative ratings for better visualization

#plot_stacked_bars(df, labels=[1, 2, 3, 4, 5], title="Ratings", ax=ax, color_map=custom_colors)
plot_manual_stacked_barh(df, labels=[1, 2, 3, 4, 5], title="Ratings", ax=ax, color_map=custom_colors)
plt.tight_layout()
plt.savefig(graph_path + "readability_understandability.png", dpi=300)
# plt.show()

# Second figure for Missing Information
df = pd.DataFrame({"Original": missing_info_original, "Enhanced": missing_info_enhanced}).fillna(0)
df = df.T  # Transpose to have "Original" and "Enhanced" on y-axis
df["No"] *= -1 # Invert the "No" ratings for better visualization
fig, ax = plt.subplots(figsize=(16, 9))  
plot_stacked_bars(df, labels=["No", "Maybe", "Yes"], 
                  title="Missing Information Ratings", ax=ax, color_map=pastel_missing_info_colors)
plt.savefig(graph_path + "missing_information.png", dpi=300)
# plt.show()
