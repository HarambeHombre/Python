# Password Manager - ![Python](https://img.shields.io/badge/Python-3.10-green)

**Password Manager** is a Python-based application built using the `tkinter` library. It allows users to securely generate, store, and manage passwords. The app provides a user-friendly interface for storing credentials associated with different websites and includes features such as password generation, search functionality, and persistent data storage using a JSON file.

---

## Features

- **Password Generation**: Creates strong and randomized passwords with a mix of letters, numbers, and symbols.
- **Data Persistence**: Stores website credentials (email/username and passwords) in a JSON file.
- **Search Functionality**: Quickly retrieve stored credentials by website name.
- **User-Friendly Interface**: Intuitive GUI built using `tkinter`.
- **Clipboard Integration**: Automatically copies the generated password to the clipboard.

---

## Requirements

The application requires the following:
- Python 3.8 or higher.
- A `logo.png` file to serve as the logo (placed in the same directory as the script).

Python libraries used:
- `tkinter`: Built-in library for GUI development.
- `random`: Used for password generation.
- `messagebox`: Provides pop-up alerts and warnings.
- `json`: Handles persistent data storage and retrieval.

---

## Installation and Setup

1. Clone this repository or copy the script file.
2. Ensure Python is installed on your system. Download it from [python.org](https://www.python.org/downloads/).
3. Place a `logo.png` file in the same directory as the Python script. This file will serve as the app's logo.

---

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using the following command:
   ```bash
   python main.py
   ```

---

## Usage
1. Generate a Password
   - Click the "**Generate Password**" button to create a random password.
   - The password is displayed in the password field and copied to the clipboard.

2. Save Password
- Enter the **Website**, **Email/Username**, and **Password**.
- Click "**Add**" to save the credentials.
- Credentials are stored in `data.json` for future use.

3. Search for a Password
- Enter the **Website** name in the website field.
- Click the "**Search**" button.
- If the website exists, the app displays the email and password in a pop-up. Otherwise, it shows an error message.

---

## UI Overview
1. Logo: Displays a logo at the top of the window (requires `logo.png` file).
2. Input Fields:
   - **Website**: Text input for the website name.
   - **Email/Username**: Text input for email or username (auto-filled with a static default email if provided).
   - **Password**: Text input for the password.

3. Buttons:
   - **Search**: Searches for credentials based on the website name.
   - **Generate Password**: Creates a new secure password.
   - **Add**: Saves the credentials to `data.json`.

---

## File Structure
```
project-directory/
│
├── main.py      # The main Python script
├── data.json           # Password storage file (created automatically)
├── logo.png            # Logo image file
```

---

## Code Breakdown
### Password Generator
Generates secure passwords using a mix of letters, numbers, and symbols:
```Python
def generate_password():
    ...
    new_password = "".join(password_list)
    password_input.insert(0, new_password)
    password_input.clipboard_append(string=new_password)
```

### Save Passwords
Saves credentials to a JSON file and updates existing data:
```Python
def save_password():
    new_data = {
        n_website: {
            "email": n_email,
            "password": n_password,
        }
    }
    ...
    with open("./data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)
```

### Search Functionality
Retrieves credentials for a specific website:
```Python
def search():
    with open("./data.json", "r") as data_file:
        data = json.load(data_file)
    if website in data:
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
```

---

## Notes
- **Data File**: Credentials are stored in `data.json`. If the file does not exist, it is created automatically.
- **Default Email**: To set a default email, replace `STATIC_EMAIL` in the script with your email address.
- **Error Handling**: The app displays helpful warnings if fields are empty or data is missing.

---

## Example Output
### Initial View:
The app opens with fields for website, email, and password, along with buttons for searching, generating, and saving passwords.
### Generated Password:
```
Generated Password: @8G!A3cd!8
```
Populated in the password field and copied to the clipboard.

### Saved Credentials:
Stored in `data.json` in the following format:
```Json
{
    "example.com": {
        "email": "user@example.com",
        "password": "strongpassword123!"
    }
}
```

### Search Result:
Displays:
```
Website: example.com
Email: user@example.com
Password: strongpassword
```

