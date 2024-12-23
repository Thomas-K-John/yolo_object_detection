# yolo_object_detection

## Create a virtual environment:
	python -m venv <env_name>
	Eg: python -m venv yolo_object_detection

## To upgrade pip (Optional)
 	pip install --upgrade pip

## Activate the environment (Windows machine):
	.\<env_name>\Scripts\activate
	Eg: .\yolo_object_detection\Scripts\activate

## Install fastapi packages
	pip install fastapi uvicorn
## Install yolo package
	pip install ultralytics
 	pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

## To create and run a docker container:
	docker-compose up --build

## Swagger UI for uploading the image and to collect the output response in JSON format:
	http://127.0.0.1:8000/docs


