import torch

# Calea către fișierul .pth
pth_path = "models/speakers.pth"  # modifică dacă e în altă parte

# Încarcă fișierul .pth
speakers_dict = torch.load(pth_path, map_location="cpu")

# Afișează conținutul
print("Continutul speakers.pth:")
for name, idx in speakers_dict.items():
    print(f"{idx}: {name}")