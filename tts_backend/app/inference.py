import torch
import numpy as np
import soundfile as sf
import os

from app.model_loader import load_everything

CONFIG_PATH = "models/config.json"
MODEL_PATH = "models/best_model.pth"
SPEAKERS_PATH = "models/speakers_clean.json"
OUTPUT_PATH = "audio_output/output.wav"

model, config, ap, tokenizer, speaker_manager = load_everything(CONFIG_PATH, MODEL_PATH, SPEAKERS_PATH)

__all__ = ["synthesize", "speaker_manager"]


def get_speaker_id_by_name(speaker_name: str) -> int:
    return speaker_manager.name_to_id[speaker_name]


def synthesize(text: str, speaker_id: int = 0):
    inputs = tokenizer.text_to_ids(text)
    inputs = torch.LongTensor(inputs)[None, :]

    speaker_tensor = torch.LongTensor([speaker_id])
    x_lengths = torch.LongTensor([inputs.shape[1]])

    if torch.cuda.is_available():
        inputs = inputs.cuda()
        speaker_tensor = speaker_tensor.cuda()
        x_lengths = x_lengths.cuda()

    with torch.no_grad():
        outputs = model.inference(
            inputs,
            aux_input={
                "x_lengths": x_lengths,
                "speaker_ids": speaker_tensor
            }
        )

    wav = outputs["model_outputs"][0].squeeze().cpu().numpy()
    print(">>> waveform shape:", wav.shape)
    print(">>> waveform dtype:", wav.dtype)
    sf.write(OUTPUT_PATH, wav, config.audio.sample_rate)
    return OUTPUT_PATH
