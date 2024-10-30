import json
from deepface import DeepFace

result = DeepFace.verify(
  img1_path = "faces\RG1.jpg",
  img2_path = "faces\RG2.jpg",
)
print(json.dumps(result,indent=2))
