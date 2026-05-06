import os
import matplotlib.pyplot as plt
import pandas as pd

# plot bar chart
def plot_bar(df, value_col, xlabel, title, result_dir, notebook_plot=False):    
    # Ensure a directory for plots exists
    os.makedirs(result_dir, exist_ok=True)

    plot_df = df[["state_name", value_col]].dropna().sort_values(by=value_col, ascending=False)

    plt.figure(figsize=(14, 6))
    plt.bar(plot_df["state_name"], plot_df[value_col], edgecolor="black")
    plt.title(title)
    plt.xlabel("State")
    plt.ylabel(xlabel)
    plt.xticks(rotation=90)
    plt.grid(axis="y")
    plt.tight_layout()

    if not notebook_plot:
        filename = f"{value_col}_barchart.png"
        plt.savefig(f"{result_dir}/{filename}")
        print(f"Saved bar chart for {value_col}")
        plt.close()
    else:
        plt.show()

# plot scatter plot 
def plot_scatter(df, x_col, y_col, xlabel, ylabel, title, result_dir,notebook_plot=False):
    os.makedirs(result_dir, exist_ok=True)

    # check columns exist
    if x_col not in df.columns or y_col not in df.columns:
        raise ValueError("Columns not found in DataFrame")

    plot_df = df[[x_col, y_col]].dropna()
    plt.figure(figsize=(8, 6))
    plt.scatter(plot_df[x_col], plot_df[y_col])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()

    if not notebook_plot:
        filename = f"{y_col}_vs_{x_col}_scatter.png"
        plt.savefig(f"{result_dir}/{filename}")
        print(f"Saved scatter plot: {filename}")
        plt.close()
    else:
        plt.show()

# plot heat map
def plot_heatmap(df, result_dir,notebook_plot=False):

    os.makedirs(result_dir, exist_ok=True)

    # keep only numeric columns
    numeric_df = df.select_dtypes(include=["int64", "float64"]).dropna()

    # correlation matrix
    corr = numeric_df.corr()

    plt.figure(figsize=(8, 6))
    plt.imshow(corr, cmap="YlOrRd")

    cols = corr.columns
    label_map = {'mental_health_pct': 'Poor Mental Health (%) – Past 30 Days','rate_per_100k': 'Violent Crime Rate (per 100k)','poverty_rate': 'Poverty Rate','no_insurance_pct': '% No Insurance','unemployment_rate': 'Unemployment Rate'}
    labels = [label_map.get(col, col) for col in cols]
    plt.xticks(range(len(cols)), labels, rotation=45, ha='right')
    plt.yticks(range(len(cols)),labels)

    # add correlation values
    for i in range(len(cols)):
        for j in range(len(cols)):
            plt.text(j, i, f"{corr.iloc[i, j]:.2f}",
                     ha='center', va='center')

    plt.title(f"Correlation Heatmap")
    plt.colorbar()
    plt.tight_layout()

    if not notebook_plot:
        filename = f"heatmap.png"
        plt.savefig(f"{result_dir}/{filename}")
        print(f"Saved heatmap: {filename}")
        plt.close()
    else:
        plt.show()


# clustering analysis
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def run_clustering(df, result_dir="results", notebook_plot=False, n_clusters=3):
    os.makedirs(result_dir, exist_ok=True)
    
    # keep important columns
    plot_df = df[['state_name', 'mental_health_pct', 'rate_per_100k']].dropna().copy()

    # scale 
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(plot_df[['mental_health_pct', 'rate_per_100k']])

    # clustering 
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    plot_df['cluster'] = kmeans.fit_predict(X_scaled)

    # plot clusters 
    plt.figure(figsize=(8, 6))

    for cluster_id in sorted(plot_df['cluster'].unique()):
        subset = plot_df[plot_df['cluster'] == cluster_id]
        plt.scatter(
            subset['mental_health_pct'],
            subset['rate_per_100k'],
            label=f'Cluster {cluster_id}'
        )

    # list of states per cluster
    for cluster_id, group in plot_df.groupby('cluster'):
        print(f"\nCluster {cluster_id}:")
        print(group['state_name'].to_list())

    plt.xlabel('Poor Mental Health (%) – Past 30 Days')
    plt.ylabel('Violent Crime Rate (per 100k)')
    plt.title(f'Mental Health & Crime (Clusters)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()


    if not notebook_plot:
        filename = f"mh_vs_crime_clusters.png"
        plt.savefig(f"{result_dir}/{filename}")
        print(f"Saved clustering plot: {filename}")
        plt.close()
    else:
        plt.show()

def run_clustering_confound(df, result_dir, notebook_plot=False, n_clusters=3):
    os.makedirs(result_dir, exist_ok=True)
    cols = ["state_name","mental_health_pct","rate_per_100k", "poverty_rate", "no_insurance_pct", "unemployment_rate"]
    cluster_df = df[cols].dropna().copy()

    # keep important cols
    feature_cols = ["mental_health_pct","rate_per_100k", "poverty_rate", "no_insurance_pct", "unemployment_rate"]

    # scale
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(cluster_df[feature_cols])

    # clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_df["cluster"] = kmeans.fit_predict(X_scaled)

    # plot mental health vs crime 
    plt.figure(figsize=(8, 6))

    for cluster_id in sorted(cluster_df["cluster"].unique()):
        subset = cluster_df[cluster_df["cluster"] == cluster_id]
        plt.scatter(
            subset["mental_health_pct"],
            subset["rate_per_100k"],
            label=f"Cluster {cluster_id}",
            alpha=0.8
        )

    # list of states per cluster
    for cluster_id, group in cluster_df.groupby('cluster'):
        print(f"\nCluster {cluster_id}:")
        print(group['state_name'].to_list())

    plt.xlabel("Poor Mental Health (%) – Past 30 Days")
    plt.ylabel("Violent Crime Rate (per 100k)")
    plt.title(f"Mental Health & Crime (Clusters Adjusted for Socioeconomic Factors)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if not notebook_plot:
        filename = f"mh_vs_crime_clusters_confound.png"
        plt.savefig(f"{result_dir}/{filename}")
        print(f"Saved clustering plot: {filename}")
        plt.close()
    else:
        plt.show()