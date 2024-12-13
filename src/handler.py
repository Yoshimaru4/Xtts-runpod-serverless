""" Example handler file. """

import runpod
from TTS.api import TTS
import torch

# If your handler runs inference on a model, load the model here.
# You will want models to be loaded into memory before starting serverless.

device = "cuda:0" if torch.cuda.is_available() else "cpu"
print("device = ", device)

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

print("Loaded model tts !!")


def handler(job):
    """ Handler function that will be used to process jobs. """
    job_input = job['input']
    text = job_input.get('text')
    speaker = job_input.get('speaker')
    language = job_input.get('language')
    wav = tts.tts(
        text=text,
        speaker=speaker,
        language=language,
    )

    print("ran inference successfully !!!!!!")
    print("type(wav): ", type(wav))

    json_data = {
        "text": text, 
        "wav": [float(x) for x in wav],  # FastAPI does not support numpy types, only support native python types
        "output_sample_rate": tts.config.audio.output_sample_rate,
        "sample_rate": tts.config.audio.sample_rate,
    }

    return json_data


runpod.serverless.start({"handler": handler})
