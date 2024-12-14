from TTS.api import TTS
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"
print("device = ", device)

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

print("Loaded model tts !!")