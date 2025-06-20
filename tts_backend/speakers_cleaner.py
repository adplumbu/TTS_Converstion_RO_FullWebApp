import torch
import json

# Încarcă fișierul .pth
pth_path = "models/speakers.pth"
all_speakers = torch.load(pth_path, map_location="cpu")

# Definește lista celor ignorați
ignored = {
    "VCTK_SPK01_male_cv_ro",
    "VCTK_SPK06_male_cv_ro",
    "VCTK_SPK16_female_cv_ro"
}

# Filtrează doar pe cei buni
filtered = {name: idx for idx, name in all_speakers.items() if name not in ignored}

# Reindexează speakerii de la 0
new_speakers = {name: i for i, name in enumerate(filtered.values())}

# Salvează ca JSON
with open("models/speakers_clean.json", "w", encoding="utf-8") as f:
    json.dump(new_speakers, f, indent=4, ensure_ascii=False)

print("Am salvat models/speakers_clean.json cu speakerii validati.")
