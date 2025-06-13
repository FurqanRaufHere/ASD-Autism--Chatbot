
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
import joblib

# Load the dataset
df = pd.read_csv('data.csv')  # Ensure correct path to the dataset

# Load embeddings into dict: gene -> vector
def load_embeddings(file_path):
    embeddings = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            gene = parts[0]
            vector = np.array(parts[1:], dtype=float)
            embeddings[gene] = vector
    return embeddings

embeddings_path = 'gene2vec_dim_200_iter_9.txt'  # Ensure correct path to the embeddings file
gene_embeddings = load_embeddings(embeddings_path)
print(f"Loaded embeddings for {len(gene_embeddings)} genes")

# Function to get row embedding by averaging gene embeddings
def get_row_embedding(gene_str):
    genes = gene_str.split('|')
    vectors = [gene_embeddings.get(g, np.zeros(embedding_dim)) for g in genes]
    if vectors:
        return np.mean(vectors, axis=0)  # average embedding vector
    else:
        return np.zeros(embedding_dim)

# Set embedding dimension based on the embeddings
embedding_dim = len(next(iter(gene_embeddings.values())))  # Check the embedding size
emb_matrix = np.array([get_row_embedding(gene_str) for gene_str in df['Gene(s)']])

# Create a DataFrame with embedding columns
emb_df = pd.DataFrame(emb_matrix, columns=[f'emb_{i}' for i in range(embedding_dim)])

# Combine with original dataframe
df = pd.concat([df.reset_index(drop=True), emb_df.reset_index(drop=True)], axis=1)

# Encode target labels
le = LabelEncoder()
df['target'] = le.fit_transform(df['Germline classification'])

# Define feature matrix (X) and target labels (y)
feature_cols = [col for col in df.columns if col.startswith('emb_')]
X = df[feature_cols].values
y = df['target'].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Train the RandomForest model
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)

# Make predictions
y_pred = rf.predict(X_test)

# Evaluate the model
print("🔍 Accuracy:", accuracy_score(y_test, y_pred))
print("📊 Classification Report:\n", classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(rf, 'asds_model.pkl')  # Save the model for later use in FastAPI
