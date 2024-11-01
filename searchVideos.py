from sentence_transformers import SentenceTransformer
from pinecone import Pinecone


pc = Pinecone(api_key="YOUR_API_KEY")

index_name = "youtube-transcripts-embeddings"

index = pc.Index(index_name)


def get_embedding(query):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode(query)
    return embedding.tolist()
    

def search_videos(query, top_k = 5):
    
    print(index.describe_index_stats())
    try:
        query_embedding = get_embedding(query)
        
        #similarity search 
        result = index.query(
            vector = query_embedding,
            top_k = top_k,
            include_metadata = True,
            namespace='youtube-transcripts-embeddings'
        )
        
        
        similar_videos = [] # to store the matches in the result
        for match in result['matches']:
            similar_videos.append({
                'id':match['id'],
                'score': match['score'],
                'url': match['metadata']['url'],
                'published_at': match['metadata']['published_at'],
                'title': match['metadata']['title']
            })
        
        return similar_videos
            
        
        print(result['matches'])
    except Exception as e:
         print(f"An error occurred during the search: {e}")
         
        
matches = search_videos("videos about visual detection", 5)

for video in matches:
    print(f"Title: {video['title']}\nURL: {video['url']}\nScore: {video['score']}\n")