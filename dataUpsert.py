from pinecone import Pinecone, ServerlessSpec
import json
pc = Pinecone(api_key="YOUR_API_KEY")


index_name = "youtube-transcripts-embeddings"

pc.create_index(
    name = index_name,
    dimension = 384,
    metric="cosine",
    spec = ServerlessSpec(cloud="aws", region="us-east-1")   
)

index = pc.Index(index_name)

with open("embeddings.json", "r") as file:
    embeddings = json.load(file)
    

upsert_data = []

for item in embeddings:
    upsert_data.append(
        (
            item['id'], #unique id
            item['embedding'] , # vector
            {
                'url': item['url'],
                'published_at': item['published_at'],
                'title': item['title']
            }
            
        )
    )

index.upsert(vectors=upsert_data, namespace="youtube-transcripts-embeddings")

print(f"Successfully upserted {len(upsert_data)} vectors to Pinecone.")
print(index.describe_index_stats())