import whisper
import os 
from datetime import timedelta
import json
# Load model directly
##from transformers import AutoTokenizer, AutoModelForMaskedLM
#from transformers import pipeline

#tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-multilingual-cased")
#model = AutoModelForMaskedLM.from_pretrained("google-bert/bert-base-multilingual-cased")

files = list(filter(lambda s : s != "" and (s[-4:] == ".wav" or s[-4:] == ".mp3"), os.popen("ls audio-input").read().split("\n")))
print(files)
model = whisper.load_model("medium")
for file in files:
    print("\n\n Currently processing : ", file, " \n")
    result = model.transcribe("audio-input/" + file)["segments"]
    print(result)
    with open("audio-output/" + file[:-3] + "txt", "w") as f:
        for sentence in result:
            f.write(str(timedelta(seconds = sentence["start"])) + " : " + sentence["text"] + "\n")
    with open("audio-output/" + file[:-3] + "json", "w", encoding='utf-8') as f:
        output = [{"time" : sentence["start"], "text" : sentence["text"]} for sentence in result]
        json.dump(output, f, indent= 4, ensure_ascii=False)
    
# Use a pipeline as a high-level helper


#pipe = pipeline("fill-mask", model="google-bert/bert-base-multilingual-cased")