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
    video_ids = []
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
            video_ids.append(item['id']['videoId'])
        
        next_page_token = response.get('nextPageToken')
        
        if not next_page_token:
            break
        
    return video_ids
        

print(get_videos_from_channel(CHANNEL_ID))