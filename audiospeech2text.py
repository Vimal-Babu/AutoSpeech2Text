import os 
import whisper
import json 

input_folder = "media_files"
output_folder = "transcriptions"

#create output folder if not exists

os.makedirs(output_folder, exist_ok=True)

# load the smallest whisper model

model = whisper.load_model("tiny")


def transcribe_file(file_path):
    # print("transscribe function works------------------>>>")
    # print(file_path)
    """Transcribe audio or video file using whisper"""
    result =model.transcribe(file_path)
    #print(result,"resultttttttttttt")
    return result["text"]

def process_directory(directory):
    # print("process dirctory function works ------>>>")
    """recursively find media file and transcribe them"""
    media_extensions = {".mp3",".wav",".mp4",".mkv"}
    
    for root, _,files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in media_extensions):
                file_path = os.path.join(root,file)
                transcription = transcribe_file(file_path)
                
                #save as json
                output_path = os.path.join(output_folder,f"{file}.json")
                with open(output_path, "w",encoding ="utf-8") as f:
                    json.dump({"file":file,"transcription":transcription},f,indent=4)
                print(f"Processed: {file}")
                
process_directory(input_folder)