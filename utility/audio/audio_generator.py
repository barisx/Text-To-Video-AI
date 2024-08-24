import edge_tts

async def generate_audio(text,outputFilename):
    communicate = edge_tts.Communicate(text,"en-AU-WilliamNeural", pitch="-50Hz", volume="+20%")
    await communicate.save(outputFilename)





