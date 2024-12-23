from fastapi import FastAPI, File, UploadFile
from starlette.responses import StreamingResponse
from ultralytics import YOLO
from PIL import ImageDraw, Image
from io import BytesIO

MODEL_FOLDER = "models/"
model_name = "yolo11n.pt"

app = FastAPI()

@app.get("/")
def default_page():
    return {"message": "test:test"}

@app.post("/detect")
async def detect_and_return_image(image_file: UploadFile = File(...)):
    """
    Handler of /detect POST endpoint. Receives uploaded file and passes it through YOLOv11 object detection model.
    """
    buf = await image_file.read()
    output = detect_objects_on_image(Image.open(BytesIO(buf)))
    print(output)
    return {
        "output": output
    }


def detect_objects_on_image(image):
    """
    Receives an image, passes it through YOLOv11 model and returns an array of detected objects and their bounding boxes
    """
    model = YOLO(MODEL_FOLDER + model_name)
    results = model.predict(image, device='cpu', conf=0.5, save=True, save_txt=True)
    names = model.names
    output = create_upload_file(results[0], names)
    return output


def create_upload_file(results, names):
    boxes = results.boxes.xyxy.tolist()
    classes = results.boxes.cls.tolist()
    confidences = results.boxes.conf.tolist()

    output = []
    for box, cls, conf in zip(boxes, classes, confidences):
        x1, y1, x2, y2 = box
        detected_class = int(cls)
        name = names[detected_class]
        output.append({
            'label': name,
            'confidence': conf,
            'bounding_box': {
                'x1': int(x1),
                'y1': int(y1),
                'x2': int(x2),
                'y2': int(y2)
            }
        })
    return output