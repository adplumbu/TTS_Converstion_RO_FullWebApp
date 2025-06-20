from TTS.tts.models.vits import Vits
from TTS.tts.utils.text.tokenizer import TTSTokenizer
from TTS.tts.utils.speakers import SpeakerManager
from TTS.utils.audio import AudioProcessor
from TTS.config import load_config

import torch
import json

def load_everything(config_path, model_path, speakers_path):
    config = load_config(config_path)  # doar citim config.json

    # Inițializează componentele audio și text
    ap = AudioProcessor.init_from_config(config)
    tokenizer, config = TTSTokenizer.init_from_config(config)

    # SpeakerManager separat, încărcăm manual JSON-ul
    speaker_manager = SpeakerManager()
    with open(speakers_path, "r", encoding="utf-8") as f:
        speaker_manager.name_to_id = json.load(f)

    # Debug: afișează speakerii încărcați
    print("Lista de speakeri disponibili:")
    for name, id in speaker_manager.name_to_id.items():
        print(f"{id}: {name}")

    # Încarcă modelul VITS antrenat
    model = Vits.init_from_config(config)
    model.load_checkpoint(config, model_path)
    model.cuda() if torch.cuda.is_available() else model.cpu()
    model.eval()

    return model, config, ap, tokenizer, speaker_manager
