# Cafe Directory Application - ![Python](https://img.shields.io/badge/Python-3.10-green)
The `Cafe Directory Application` is a Flask-based web app that allows users to manage a list of cafes. Users can add new cafes, view a directory of cafes, and delete entries. This app uses SQLAlchemy for database management and Flask-WTF for form handling, with a Bootstrap-powered user interface for an enhanced user experience.

---

## Features
- **Add Cafes**: Users can add new cafes by filling out a form with relevant details such as name, location, amenities, and coffee price.
- **View Cafe Directory**: Displays all cafes in a clean, Bootstrap-styled table.
- **Delete Cafes**: Users can remove cafes from the directory.
- **Database Integration**: Uses SQLite to store data persistently.
- **Form Validation**: Ensures input fields are filled out appropriately using Flask-WTF.

---

## Requirements
### Python Libraries
The following Python libraries are required:
- `Flask`: A lightweight web framework.
- `Flask-Bootstrap`: Provides easy integration of Bootstrap styles.
- `Flask-SQLAlchemy`: For database management.
- `Flask-WTF`: For creating and validating forms.
- `WTForms`: Provides fields for user forms.

---

## Installation
1. Clone the repository:
```bash   
git clone https://github.com/your-repo/cafe-directory.git
```
2. Navigate to the project directory:
```bash
cd cafe-directory
```
3. Install the required dependencies:
```bash
pip install flask flask-bootstrap flask-sqlalchemy flask-wtf
```
4. Set up the database:
```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

---

## Usage
1. Run the application:
```bash
python main.py
```
2. Open the application in your browser:
   - Default URL: `http://127.0.0.1:5000/`

---

## Application Structure
### Routes
`/`
- Method: `GET`
- Displays the list of cafes in the database using the `index.html` template.

`/add`
- Method: `GET`, `POST`
- Displays a form for adding new cafes to the database.
- Redirects to the main page upon successful submission.

`/delete/<int:id>`
- Method: `GET`
- Deletes the cafe entry with the given ID.

### Database Model
The `Cafe` model defines the structure for each cafe entry:
```Python
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)
```

### Forms
The `CafeForm` class is used to create and validate input fields for adding cafes:
```Python
class CafeForm(FlaskForm):
    name = StringField('Cafe Name')
    map_url = StringField('Map URL')
    img_url = StringField('Image URL')
    location = StringField('Location')
    seats = StringField('Seats')
    coffee_price = StringField('Coffee Price')
    has_sockets = BooleanField('Extra sockets')
    has_toilet = BooleanField('Toilets')
    has_wifi = BooleanField('WiFi')
    can_take_calls = BooleanField('Take Calls')
    submit = SubmitField('Add')
```

---

## Example Outputs
### Main Page
The main page displays a list of cafes:
```
Cafe Name | Location | Coffee Price | Amenities
-----------------------------------------------
Cafe Latte | Downtown | $2.50       | WiFi, Sockets
Starbrew   | Uptown   | $3.00       | WiFi, Calls
```

### Add Page
The add page allows users to input details about a new cafe.
### Delete Function
Upon clicking the delete link, the cafe is removed from the database.

---

## Notes
- **Database Persistence**: Data is stored in a SQLite file named `cafes.db`.
- **Customization**: You can modify the Bootstrap styling in the templates to suit your needs.
- **Error Handling**: Ensure proper user input validation for consistent data entry.



