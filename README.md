
# Text-to-Speech API

This is a **FastAPI-based Text-to-Speech API** using Coqui TTS models to convert input text into speech (WAV files).

## 🚀 Features
- Converts text to speech
- Saves output audio in `outputs/` folder
- Simple REST API using FastAPI

## 🔧 Requirements
- Python 3.8+

### Install dependencies
```
pip install -r requirements.txt
```

## ▶️ Usage

1. **Run the server**
   ```
   uvicorn main:app --reload
   ```

2. **Make a POST Request**
   - **Endpoint:** `/text-to-speech`
   - **Method:** POST
   - **Body:**
     ```json
     { "text": "Hello world" }
     ```

3. **Response**
   ```json
   {
     "input_text": "Hello world",
     "audio_file": "outputs/audio_xxxxx.wav",
     "message": "✅ Text converted to speech successfully"
   }
   ```

---

### ✨ Built with
- FastAPI
- Coqui TTS
- PyTorch

---

## 📂 Project Structure

```
final_tts/
  ├── main.py
  └── requirements.txt
```

---
