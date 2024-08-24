import edge_tts

async def generate_audio(text,outputFilename):
    communicate = edge_tts.Communicate(text,"en-AU-WilliamNeural", pitch="-50Hz", speed="-50%", volume="+20dB")
    await communicate.save(outputFilename)





