import pickle

# Load model
with open("models/kmeans_model.pkl", "rb") as f:
    kmeans = pickle.load(f)

# Load scaler
with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

print("KMeans features:", getattr(kmeans, "n_features_in_", "Unknown"))
print("Scaler features:", getattr(scaler, "n_features_in_", "Unknown"))
print("Cluster Centers:")
print(kmeans.cluster_centers_)