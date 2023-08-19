from pydub import AudioSegment

def make_chunks(audio, chunk_length_ms):
    """Split the audio into equal sized chunks."""
    
    # Calculate the number of chunks
    n_chunks = len(audio) // chunk_length_ms
    
    # Split the audio
    chunks = [audio[i*chunk_length_ms:(i+1)*chunk_length_ms] 
              for i in range(n_chunks)]
    
    return chunks

audio = AudioSegment.from_wav("1.wav") 

chunk_length_ms = 300000  

chunks = make_chunks(audio, chunk_length_ms) 

for i, chunk in enumerate(chunks):
    chunk_name = f"chunk{i}.wav"
    print ("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")
