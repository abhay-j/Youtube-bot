from sentence_transformers import SentenceTransformer
import json
import time

with open("cleaned_data.json","r") as file:
    data = json.load(file)
    
model = SentenceTransformer('all-MiniLM-L6-v2') #embedding model from huggingface. It's lightweight and generates 384-dimensional embeddings, suitable for tasks like clustering or semantic search

documents= [] # to store data with its embeddings 


start_time = time.time()
print(start_time)

for video_id, content in data.items():
    combined_text = data[video_id]["text"]
    embedding = model.encode(combined_text)
    print(f"Embeddings shape: {embedding.shape}")
    
    documents.append({
        "id":video_id,
        "embedding":embedding.tolist(),
        "title":content["title"],
        "url":content["url"],
        "published_at":content["published_at"]
    })

end_time = time.time()
print(end_time)


print(f"Time taken: {end_time - start_time:.2f} seconds")

with open("embeddings.json", "w") as file:
    json.dump(documents, file)