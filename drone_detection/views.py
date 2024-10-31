import os
import torch
from django.http import JsonResponse
from django.shortcuts import render
from PIL import Image

# Load the YOLOv8 model once when the server starts
model = torch.load('/app/yolov8n.pt')  # Load the model directly from the .pt file
model.eval()  # Set the model to evaluation mode

def detect_objects(request):
    # Set the path to the image located in the parent directory
    img_path = "/app/input.jpg"   # Adjusted to go one directory up

    # Check if the image exists
    if not os.path.exists(img_path):
        return JsonResponse({'error': 'Image not found at the specified path.'}, status=404)

    # Run the model on the input image
    img = Image.open(img_path)
    results = model(img)  # Assuming your model can take a PIL image directly

    # Convert results to a JSON response
    return JsonResponse(results.pandas().xyxy[0].to_dict(orient="records"), safe=False)
