# channel id : UCphwJynbSnC0XPY7Vh6qFbQ
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import json
API_KEY = "AIzaSyBSa4LpEW1P5rQ9uWrPuJEDxf_NBByzn1I"
CHANNEL_ID = "UCphwJynbSnC0XPY7Vh6qFbQ"

#Initialize your api 
youtube = build('youtube', 'v3', developerKey=API_KEY)


#fetch all videos from the youtube channel 
def get_videos_from_channel(channel_id):
    # video_ids = []
    video_detials = {}
    next_page_token = None
    
    while True:
        # create request to get video_ids 
        request = youtube.search().list(
            part = 'snippet',
            channelId = channel_id,
            maxResults = 50, # limits the results to 50, can be increased
            type = 'video', 
            pageToken = next_page_token
            
        )
        
        response = request.execute()
        
       
        
            
            
        for item in response['items']:
            # individual_video_details = {}
            # individual_video_details['id'] = item['id']['videoId']
            # individual_video_details['published_at'] = item['snippet']['publishedAt']
            # individual_video_details['title'] = item['snippet']['title']
            
            #video_ids.append(item['id']['videoId'])
            #video_detials.append(individual_video_details)
            
            video_detials[item['id']['videoId']]={
                'published_at':item['snippet']['publishedAt'],
                'title':item['snippet']['title'],
                'text':''
            }
            
            
        
        next_page_token = response.get('nextPageToken')
        
        if not next_page_token:
            break
        
    return video_detials
        



#function to fetch the transcripts of a video 
# def get_transcript(video_id):
#     try:
#         transcript = YouTubeTranscriptApi.get_transcript(video_id)
#         return transcript
#     except Exception as e:
#         print(f"transcript not available for the video {video_id}: {e}")
#         return None





#function to get transcripts for all videos on a channel
# def get_all_transcripts(channel_id):
#     video_ids = get_videos_from_channel(channel_id)
#     transcripts = {}
    
#     for video_id in video_ids:
#         print(f"getting transcript for video id: ${video_id}")
#         transcript = get_transcript(video_id)
        
#         if transcript:
#             transcripts[video_id] = transcript
    
#     #save transcripts to a json file 
#     with open('transcripts.json', 'w') as f:
#         json.dump(transcripts, f, indent=4)
    
#     print(f"Transcripts saved to 'transcripts.json'")
    

# Run the script
# get_all_transcripts(CHANNEL_ID)     
        
    