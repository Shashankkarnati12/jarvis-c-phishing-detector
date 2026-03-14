import kagglehub

# Download the dataset from Kaggle
path = kagglehub.dataset_download("samahsadiq/benign-and-malicious-urls")

print("✅ Dataset downloaded successfully!")
print("📂 Path to dataset files:", path)
