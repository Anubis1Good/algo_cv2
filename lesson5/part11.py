import json
from deepface import DeepFace
objs = DeepFace.analyze(img_path = "RG3.jpg")

print(json.dumps(objs,indent=2))