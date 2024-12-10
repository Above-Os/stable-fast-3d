import os
from huggingface_hub import login
from sf3d import SF3D  # Assuming this is your import

# Load the model
model = SF3D.from_pretrained(
    "stabilityai/stable-fast-3d",
    config_name="config.yaml",
    weight_name="model.safetensors",
)