import json
from openai import OpenAI
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

client = OpenAI()

# Load document chunks
with open(
    "enterprise-knowledge-copilot/outputs/document_chunks.json",
    encoding="utf-8"
) as f:
    chunks = json.load(f)

texts = [chunk["text"] for chunk in chunks]

# Create embeddings
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedding_model.encode(texts)

# User question
question = input("\nAsk the Knowledge Copilot: ")

query_embedding = embedding_model.encode([question])
scores = cosine_similarity(query_embedding, embeddings)[0]

# Retrieve top 3 chunks
best_indices = scores.argsort()[-3:][::-1]

context = "\n\n".join(
    texts[index] for index in best_indices
)

prompt = f"""
Answer the question using only the provided company knowledge.

If the answer is not contained in the context, say:
"I could not find that information in the company knowledge base."

CONTEXT:
{context}

QUESTION:
{question}
"""

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

print("\nCOPILOT ANSWER")
print("-" * 50)
print(response.output_text)

print("\nRETRIEVED SOURCES")
print("-" * 50)

for index in best_indices:
    print(
        f"Chunk {chunks[index]['chunk_id']} "
        f"| Similarity: {scores[index]:.3f}"
    )