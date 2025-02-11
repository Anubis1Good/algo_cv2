import json
from deepface import DeepFace
objs = DeepFace.analyze(img_path = "test\Screenshot_27.png")

print(json.dumps(objs,indent=2))