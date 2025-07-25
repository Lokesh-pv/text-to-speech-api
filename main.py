from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from TTS.api import TTS
import os
import uuid
import uvicorn


# Initialize FastAPI
app = FastAPI()

# Load TTS model once at startup
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

# Create output directory
os.makedirs("outputs", exist_ok=True)

# Define request body model
class TextInput(BaseModel):
    text: str

# POST endpoint for TTS
@app.post("/text-to-speech")
async def convert_text_to_speech(payload: TextInput):
    text = payload.text.strip()
    if not text:
        return JSONResponse(status_code=400, content={"error": "Text input is empty."})

    filename = f"outputs/audio_{uuid.uuid4().hex}.wav"
    tts.tts_to_file(text=text, file_path=filename)

    return {
        "input_text": text,
        "audio_file": filename,
        "message": "✅ Text converted to speech successfully"
    }




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)