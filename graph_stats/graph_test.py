import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
results_path = "C:\\Users\\guipa\\OneDrive\\Documentos\\GitHub\\TEL_Enhanced_Readability\\human_study\\"
graph_path = "C:\\Users\\guipa\\OneDrive\\Documentos\\GitHub\\TEL_Enhanced_Readability\\graph_stats\\"
file_path = results_path + "knowledgeTest.csv"
df = pd.read_csv(file_path)
smoothing = 0.3
smoothing_string = str(smoothing).replace(".", "_")
# Display basic information and the first few rows
df.info(), df.head()
# Convert "Gain" to numeric, coercing errors to NaN if necessary
df["Gain"] = pd.to_numeric(df["Gain"], errors="coerce")

# Check if conversion was successful
df.info(), df.head()
# Set up the plotting style
sns.set(style="whitegrid")

# Create the first figure: 4 violin plots (Pre & Post for each group)
plt.figure(figsize=(10, 6))
df_melted = df.melt(id_vars=["Condition"], value_vars=["Pre", "Post"], var_name="Test", value_name="Score")
df_melted["Group"] = df_melted["Condition"].map({0: "Group 0", 1: "Group 1"})
sns.violinplot(x="Group", y="Score", hue="Test", data=df_melted, split=True, inner="quartile", palette="muted", bw_adjust=smoothing)

plt.title("Pre and Post Test Scores by Group")
plt.xlabel("Group")
plt.ylabel("Score")
plt.legend(title="Test")
plt.ylim(0, 100)
plt.savefig(graph_path + "pre_post_text_" + smoothing_string +".png", dpi=300)
#plt.show()

# Create the second figure: 2 violin plots (RawDif_PostPre for each group)
plt.figure(figsize=(8, 5))
sns.violinplot(x="Condition", y="RawDif_PostPre", data=df, palette="coolwarm", bw_adjust=smoothing)
plt.xticks(ticks=[0, 1], labels=["Group 0", "Group 1"])
plt.title("Raw Difference (Post - Pre) by Group")
plt.xlabel("Group")
plt.ylabel("Raw Difference in Scores")
plt.ylim(-100, 100)
plt.savefig(graph_path + "raw_difference_" + smoothing_string + ".png", dpi=300)
#plt.show()

# Create the third figure: 2 violin plots (Gain for each group)
plt.figure(figsize=(8, 5))
sns.violinplot(x="Condition", y="Gain", data=df, palette="coolwarm", bw_adjust=smoothing)
plt.xticks(ticks=[0, 1], labels=["Group 0", "Group 1"])
plt.title("Gain Scores by Group")
plt.xlabel("Group")
plt.ylabel("Gain Score")
plt.ylim(-100, 100)
plt.savefig(graph_path + "gain_" + smoothing_string +".png", dpi=300)
#plt.show()
