import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

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

custom_colors = {
    1: "#d73027",  # Red
    2: "#fc8d59",  # Orange
    3: "#fee08b",  # Yellow
    4: "#91cf60",  # Green  
    5: "#1b7837"  # Dark Green
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
def plot_stacked_bars(data1, data2, labels, title, ax, color_map):
    df = pd.DataFrame({"Original": data1, "Enhanced": data2}).fillna(0)
    df = df.T  # Transpose to have "Original" and "Enhanced" on y-axis

    # Ensure ratings are in the correct order
    df = df[labels]

    colors = [color_map[label] for label in color_map.keys()]
    # Plot stacked bars
    df.plot(kind="barh", stacked=True, color=colors, ax=ax, width=0.6)
    ax.set_title(title)
    ax.set_xlabel("Count")
    ax.set_ylabel("Text Type")
    ax.legend(title="Ratings", loc="upper right")

# Create the first figure (Readability & Understandability)
fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

plot_stacked_bars(readable_original, readable_enhanced, labels=range(1, 6), 
                  title="Readability Ratings", ax=axes[0], color_map=custom_colors)
plot_stacked_bars(understandable_original, understandable_enhanced, labels=range(1, 6), 
                  title="Understandability Ratings", ax=axes[1], color_map=custom_colors)

plt.tight_layout()
plt.savefig(graph_path + "readability_understandability.png", dpi=300)
# plt.show()

# Second figure for Missing Information
fig, ax = plt.subplots(figsize=(16, 9))  
plot_stacked_bars(missing_info_original, missing_info_enhanced, labels=["No", "Maybe", "Yes"], 
                  title="Missing Information Ratings", ax=ax, color_map=pastel_missing_info_colors)
plt.savefig(graph_path + "missing_information.png", dpi=300)
# plt.show()
