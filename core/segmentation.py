from PIL import Image, ImageDraw, ImageFont
import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn
from torchvision import transforms as T
import io

# COCO label names
COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag',
    'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite',
    'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana',
    'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table',
    'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock',
    'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

# Load model once
model = maskrcnn_resnet50_fpn(pretrained=True)
model.eval()

# Image transforms
transform = T.Compose([
    T.ToTensor()
])

def generate_segmentation(image_source):
    if isinstance(image_source, str):
        image = Image.open(image_source).convert("RGB")
    else:
        image = Image.open(image_source).convert("RGB")

    image_tensor = transform(image)
    with torch.no_grad():
        predictions = model([image_tensor])[0]

    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    threshold = 0.5
    for box, label_idx, score in zip(predictions['boxes'], predictions['labels'], predictions['scores']):
        if score >= threshold:
            box = box.tolist()
            label = COCO_INSTANCE_CATEGORY_NAMES[label_idx] if label_idx < len(COCO_INSTANCE_CATEGORY_NAMES) else f"Class {label_idx}"
            # Draw green rectangle with thicker line (width=4)
            draw.rectangle(box, outline="green", width=14)
            # Draw label
            draw.text((box[0] + 5, box[1] - 10), label, fill="green", font=font)

    return image
