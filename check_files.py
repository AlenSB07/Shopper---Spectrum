import pickle

# Check similarity file
with open("models/product_similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

print("===== PRODUCT SIMILARITY =====")
print(type(similarity))

if hasattr(similarity, "shape"):
    print("Shape:", similarity.shape)

if hasattr(similarity, "head"):
    print(similarity.head())

print("\n")

# Check customer product file
with open("models/customer_product.pkl", "rb") as f:
    customer_product = pickle.load(f)

print("===== CUSTOMER PRODUCT =====")
print(type(customer_product))

if hasattr(customer_product, "shape"):
    print("Shape:", customer_product.shape)

if hasattr(customer_product, "head"):
    print(customer_product.head())