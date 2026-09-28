import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

with open(
    "enterprise-knowledge-copilot/outputs/document_chunks.json",
    encoding="utf-8"
) as f:
    chunks = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [chunk["text"] for chunk in chunks]
embeddings = model.encode(texts)

query = input("\nAsk a question: ")
query_embedding = model.encode([query])

scores = cosine_similarity(query_embedding, embeddings)[0]
best_indices = scores.argsort()[-3:][::-1]

print("\nTOP RELEVANT CONTEXT\n")

for index in best_indices:
    print(f"Score: {scores[index]:.3f}")
    print(texts[index])
    print("-" * 50)