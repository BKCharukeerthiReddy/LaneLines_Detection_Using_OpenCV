from flask import Flask, render_template
# Check if you have this import anywhere in your code
from watchdog.events import EVENT_TYPE_OPENED

import os

app = Flask(__name__)

# Function to get image filenames
def get_image_filenames():
    original_images = os.listdir(os.path.join('static', 'images', 'original'))
    processed_images = os.listdir(os.path.join('static', 'images', 'processed'))
    return original_images, processed_images

@app.route('/')
def index():
    original_images, processed_images = get_image_filenames()
    image_pairs = zip(original_images, processed_images)
    return render_template('index.html', image_pairs=image_pairs)

if __name__ == '__main__':
    app.run(debug=True)
