import matplotlib.pyplot as plt
import pandas as pd

"""
def view_statistics():
    # Read the statistics from the file
    with open("statistics.csv", "r") as file:
        data = file.readlines()
    
    # Calculate the average improvement in readability
    total_improvement = 0
    for line in data:
        original, enhanced = line.split(",")
        improvement = float(original) - float(enhanced)
        total_improvement += improvement
    average_improvement = total_improvement / len(data)
    
    return average_improvement
"""
# file = "C:\\Users\\guipa\\OneDrive\\Documentos\\GitHub\\TEL_Enhanced_Readability\\excel_stats\\statistics_new_metrics_based.xlsx"
file = "C:\\Users\\guipa\\OneDrive\\Documentos\\GitHub\\TEL_Enhanced_Readability\\statistics_general_sentiment_cleaned.xlsx"

def view_statistics():
    # Read the statistics from the excel file
    df = pd.read_excel(file)
    # Calculate the average improvement in readability
    df["Improvement"] = df["Readability Original"] - df["Readability Simplified"] / df["Readability Original"]
    print(df["Improvement"])
    average_improvement = df["Improvement"].mean()
    print(average_improvement)
    return average_improvement

# first prompt (general sentiment): average improvement = 13.200027988278896
# first prompt (general sentiment cleaned): average improvement = 13.15973127537509
# second prompt (metric based): average improvement = 13.43
# third prompt (metric based): average improvement = 13.39
# fourth prompt (metric based): average improvement = 13.43
# fourth prompt (metric based cleaned): average improvement = 13.394554137534223

def graph_readability():
    # Read the statistics from the excel file
    df = pd.read_excel(file)
    # Calculate the percentage improvement in readability
    df["Percentage Improvement"] = ((df["Readability Original"] - df["Readability Simplified"]) / df["Readability Original"]) * 100

    # Plot the percentage improvement in readability
    plt.scatter(df["Readability Original"], df["Percentage Improvement"])
    plt.xlabel("Flesch-Kincaid Grade Level")
    plt.ylabel("Percentage Improvement")
    plt.title("Percentage Improvement in Readability")
    plt.ylim(bottom=0)
    plt.show()

def graph_readability_categories():
    # Read the statistics from the excel file
    df = pd.read_excel(file)
    # Calculate the percentage improvement in readability
    df["Percentage Improvement"] = ((df["Readability Original"] - df["Readability Simplified"]) / df["Readability Original"]) * 100

    # Define thresholds for performance clusters
    high_threshold = 20  # Example threshold for high performers
    low_threshold = 5   # Example threshold for low performers

    # Assign performance categories based on thresholds
    df["Performance"] = pd.cut(df["Percentage Improvement"],
                               bins=[-float('inf'), low_threshold, high_threshold, float('inf')],
                               labels=["Low", "Average", "High"])

    # Plot the percentage improvement in readability with different colors for each performance category
    colors = {"High": "green", "Average": "orange", "Low": "red"}
    plt.scatter(df["Readability Original"], df["Percentage Improvement"], 
                c=df["Performance"].map(colors), label=df["Performance"])

    plt.xlabel("Flesch-Kincaid Grade Level")
    plt.ylabel("Percentage Improvement")
    plt.title("Percentage Improvement in Readability")
    plt.ylim(bottom=0)

    # Add a legend to the plot
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label)
               for label, color in colors.items()]
    plt.legend(handles=handles, title="Performance")

    plt.show()


view_statistics()
graph_readability_categories()