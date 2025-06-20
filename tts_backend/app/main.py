from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import FileResponse
from app.inference import synthesize, speaker_manager

app = FastAPI()

@app.get("/synthesize")
def tts(
    text: str = Query(..., description="Textul care va fi sintetizat."),
    speaker_id: int = Query(None, description="ID numeric pentru speaker."),
    speaker_name: str = Query(None, description="Numele speakerului (ex: VCTK_SPK08_female_cv_ro)")
):
    if speaker_name is not None:
        if speaker_name not in speaker_manager.name_to_id:
            raise HTTPException(status_code=404, detail="Speaker name not found.")
        speaker_id = speaker_manager.name_to_id[speaker_name]
    elif speaker_id is None:
        raise HTTPException(status_code=400, detail="Provide either speaker_id or speaker_name.")
    
    audio_file = synthesize(text, speaker_id)
    return FileResponse(audio_file, media_type="audio/wav", filename="output.wav")


@app.get("/speakers")
def list_speakers():
    return speaker_manager.name_to_id
