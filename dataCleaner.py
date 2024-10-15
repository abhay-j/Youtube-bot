import json
import re


#get the dummy data into json and create a dictionary 
with open("transcripts.json", "r") as file:
    data = json.load(file)


total_videos = len(data)


#utility function to remove non speech parts lile [music]
def remove_non_speech_parts(text_to_clean):
    clean_text = re.sub(r'\[[^\]]+\]', '', text_to_clean)
    return clean_text





cleaned_data = {} #here we are going to store cleaned (data that is non-null/none)
for index, (video_id, transcript) in enumerate(data.items(), start=1):
    if transcript: #if transcript exists then add video id and transcript to the cleaned_data dictionary
        
        transcript_text = []
        #iterate over each transcript list 
        for transcript_item in transcript:
            #remove the time stamps and add the the "text"
            transcript_text.append(transcript_item['text'])
        
        
        
        #turn the list of strings (transctipts) into one single string (transcript)
        text_to_clean = ' '.join(transcript_text)
        cleaned_data[video_id] =  remove_non_speech_parts(text_to_clean)
        
        print(f"processed {index}/{total_videos} videos")




with open("cleaned_data.json","w") as file:
    json.dump(cleaned_data, file, indent=2)