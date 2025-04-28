# Color Palette Extractor - ![Python](https://img.shields.io/badge/Python-3.x-blue)

**Color Palette Extractor** is a Python web application that extracts the dominant colors from uploaded images and displays them in a palette. Powered by Flask, Bootstrap, and Pylette, this application provides a simple interface for uploading images and generating color palettes.

---

## Features

- **Image Upload**: Users can upload images in `.jpg` format using a web interface.
- **Color Extraction**: Extracts the top 12 dominant colors from the uploaded image using the Pylette library.
- **Palette Display**: Displays the extracted color palette on the webpage.
- **Dynamic Processing**: Reprocesses the palette every time a new image is uploaded.

---

## Requirements

### Python Libraries
The following Python libraries are required:
- `Flask`: A lightweight web framework for Python.
- `Flask-Bootstrap`: For integrating Bootstrap with Flask to style the application.
- `Pylette`: A library for extracting color palettes from images.
- `Pillow`: Python Imaging Library for image processing.

### Other Requirements
- Place a folder named `static` in the project directory.
  - This folder should contain an initial placeholder image named `image.jpg`.

- Ensure Python 3.8 or higher is installed.

---

## Installation and Setup
1. Clone this repository or download the code file:
```bash
git clone https://github.com/your-repo/flask-color-palette.git
```
2. Navigate to the project directory:
```bash
cd flask-color-palette
```
3. Install the required Python libraries:
```bash
pip install flask flask-bootstrap pylette pillow
```
4. Create a `static` folder and add an initial image file named `image.jpg`. This file will serve as the default image until a new one is uploaded.
5. Run the application:
```bash
python main.py
```

--- 

## Usage
1. Open the application in your browser. By default, it runs on:
```
http://127.0.0.1:5000/
```
2. The interface consists of:
   - A **file upload button** for selecting an image.
   - A color palette generated from the default or uploaded image.

3. Upload an image (`.jpg` format) by clicking the "Choose File" button and submitting it.
4. The application processes the image and displays:
   - A preview of the uploaded image.
   - A list of the dominant colors extracted from the image.

---

## Application Structure
### Routes
`/`
- Methods: `GET`, `POST`
- Displays the homepage with the default image and palette.
- Processes file uploads and regenerates the palette.

### Logic Overview
Extracting Colors
The Pylette library is used to extract RGB values of the dominant colors:
```Python
palette = extract_colors(image, palette_size=12)

colors = []
for color in palette:
    r, g, b = color.rgb[0], color.rgb[1], color.rgb[2]
    others = (r, g, b)
    colors.append(others)
```

### File Handling
The uploaded image is saved to the `static` directory:
```Python
file.save('./static/image.jpg')
```

### Rendering
The extracted palette and the uploaded image are passed to the index.html template:
```Python
return render_template('index.html', palette=colors, image=image)
```

---

## Example Outputs
### Initial View
The webpage displays the placeholder image (`image.jpg`) along with its color palette.
### Uploaded Image
- **User Input**: Upload a new `.jpg` image.
- **Generated Palette**: The extracted color palette is displayed in a visually appealing format, showing the RGB values of dominant colors.

---

## Notes
- **Supported Formats**: Only `.jpg` images are supported for upload and processing. Extend functionality by adding support for `.png` or `.bmp`.
- **Palette Size**: The number of extracted colors is set to 12. Modify `palette_size` to adjust this value.
- **File Overwrite**: The uploaded image overwrites the existing `image.jpg` in the static folder.



