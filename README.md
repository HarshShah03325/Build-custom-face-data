# Build-custom-face-data
## Steps to follow:

### 1. Clone the repository to your local machine:
``` 
git clone https://github.com/HarshShah03325/Build-custom-face-data.git 

```

### 2. Create and activate python virtual environment:
- Please refer to these [instructions](https://docs.python.org/3/tutorial/venv.html)

### 3. Install the required dependencies:
```
pip install -r requirements.txt
```
### 4. Create a folder named 'dataset' and inside the /dataset folder create a folder of 'your-name' ( For instance: Harsh )

### 5. Get ready to click some pictures:
```
python create_dataset.py --cascade haarcascade_frontalface_default.xml --output dataset/your-name
```
#### Press 'k' on your keyboard to capture a image and press 'q' after you have finished taking upto 30 images
