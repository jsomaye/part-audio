from pydub import AudioSegment

def make_chunks(audio, chunk_length_ms):
    """Split the audio into equal sized chunks."""
    
    # Calculate the number of chunks
    n_chunks = len(audio) // chunk_length_ms
    
    # Split the audio
    chunks = [audio[i*chunk_length_ms:(i+1)*chunk_length_ms] 
              for i in range(n_chunks)]
    
    return chunks

# خواندن فایل صوتی
audio = AudioSegment.from_wav("1.wav") 

# مشخص کردن طول هر قسمت بر حسب میلی ثانیه 
# مثلا 5 دقیقه -> 300 ثانیه -> 300000 میلی ثانیه
chunk_length_ms = 300000  


# تقسیم فایل صوتی به قسمت های مساوی
chunks = make_chunks(audio, chunk_length_ms) 

# ذخیره قسمت ها در فایل
for i, chunk in enumerate(chunks):
    chunk_name = f"chunk{i}.wav"
    print ("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")
