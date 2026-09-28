from pathlib import Path
import json


# -----------------------------
# Configuration
# -----------------------------

INPUT_FILE = Path(
    "enterprise-knowledge-copilot/data/company_knowledge.txt"
)

OUTPUT_FILE = Path(
    "enterprise-knowledge-copilot/outputs/document_chunks.json"
)

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


# -----------------------------
# Load document
# -----------------------------

text = INPUT_FILE.read_text(encoding="utf-8")

print("ENTERPRISE KNOWLEDGE COPILOT — DOCUMENT CHUNKING")
print("=" * 55)

print(f"\nDocument characters: {len(text):,}")


# -----------------------------
# Chunk document
# -----------------------------

chunks = []

start = 0
chunk_id = 1

while start < len(text):

    end = start + CHUNK_SIZE

    chunk_text = text[start:end].strip()

    if chunk_text:

        chunks.append({
            "chunk_id": chunk_id,
            "text": chunk_text
        })

        chunk_id += 1

    start += CHUNK_SIZE - CHUNK_OVERLAP


# -----------------------------
# Save chunks
# -----------------------------

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

with OUTPUT_FILE.open(
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        chunks,
        file,
        indent=2
    )


# -----------------------------
# Results
# -----------------------------

print(f"Chunks created: {len(chunks)}")
print(f"Chunk size: {CHUNK_SIZE}")
print(f"Chunk overlap: {CHUNK_OVERLAP}")

print("\nSample chunk:")
print("-" * 55)
print(chunks[0]["text"])

print(
    f"\nChunks saved to: {OUTPUT_FILE}"
)

print("\nDocument chunking complete!")