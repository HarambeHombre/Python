from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from Pylette import extract_colors

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/', methods=["GET", "POST"])
def main():
    image = './static/image.jpg'
    palette = extract_colors(image, palette_size=12)

    colors = []
    for color in palette:
        r, g, b = color.rgb[0], color.rgb[1], color.rgb[2]
        others = (r, g, b)
        colors.append(others)

    if request.method == "POST":
        file = request.files['the_file']
        if file:
            file.save('./static/image.jpg')
        return redirect(url_for('main'))

    return render_template('index.html', palette=colors, image=image)

if __name__ == '__main__':
    app.run(debug=True)