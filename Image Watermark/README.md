# Image Viewer with Watermark Application - ![Python](https://img.shields.io/badge/Python-3.10-green)
**Image Viewer with Watermark Application** is a simple Python GUI program built using `tkinter`. It allows users to upload an image and automatically applies a watermark overlay on it, displaying the result.

---

## Features
- **Image Upload**: Lets users upload `.jpg`, `.png`, or `.bmp` images using a file dialog.
- **Watermark Application**: Adds a predefined watermark overlay (`overlay.png`) to the uploaded image.
- **Dynamic Resizing**: Both the uploaded image and the watermark are resized to fit dimensions of `800x600`.
- **User-Friendly GUI**: Intuitive interface powered by `tkinter`.


## Requirements
### Python Libraries
The following Python libraries are required:
- `tkinter`: For creating the graphical user interface (GUI).
- `Pillow`: Python Imaging Library fork used for image processing.
Install the required libraries using:
```bash
pip install pillow
```

---

## Installation and Setup
1. Clone this repository or download the script file.
2. Place a watermark image named `overlay.png` in the same directory as the Python script. This image will be used as the watermark overlay.
3. Ensure Python is installed on your system. You can download it from python.org.

## Usage
1. Run the program:
```bash
python main.py
```
2. The GUI window opens with the following layout:
   - A label prompting the user to upload an image.
   - A button labeled "Choose Image".

3. Click the "**Choose Image**" button to open a file dialog and select an image file (`.jpg`, `.png`, or `.bmp`).
4. The program processes the uploaded image:
   - Resizes the image to `800x600`.
   - Resizes the watermark (`overlay.png`) to match the same dimensions.
   - Applies the watermark to the uploaded image.
5. The final image with the watermark is displayed using the system's default image viewer.

---

## Application Structure
### GUI Layout
The GUI consists of:
- **Label**: Informs the user about the functionality.
- **Button**: Allows the user to select an image.

## File Selection
A `tkinter` file dialog is used to select images:
```Python
file_open = tk.filedialog.askopenfile(initialdir='.', filetypes=[types])
```

## Image Processing
The `Pillow` library is used to handle image resizing, overlay application, and rendering:
```Python
image = Image.open(file_open.name).convert('RGBA')
resized = image.resize((800, 600))
image_overlay = Image.open('overlay.png').convert('RGBA')
resized_overlay = image_overlay.resize((800, 600))
resized.paste(resized_overlay, mask=resized_overlay)
```

---

## Example Workflow
1. Initial Window:
```
[Label: "Click the button below to open an image with a watermark applied."]
[Button: Choose Image]
```
2. File Dialog:
   - Navigate to your image directory and select an image.
3. Final Output:
   - The uploaded image is displayed with the watermark applied.

---

## Notes
- **Overlay File**: Ensure the `overlay.png` file is placed in the same directory as the script.
- **Image Resizing**: Images and overlays are resized to `800x600`. Modify the dimensions in the script as needed:
```Python
resized = image.resize((width, height))
resized_overlay = image_overlay.resize((width, height))
```



