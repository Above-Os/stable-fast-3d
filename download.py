
import os
from sf3d.system import SF3D


print(os.environ.get('HUGGINGFACE_TOKEN')) 
# Load the model
model = SF3D.from_pretrained(
    "stabilityai/stable-fast-3d",
    config_name="config.yaml",
    weight_name="model.safetensors",
)