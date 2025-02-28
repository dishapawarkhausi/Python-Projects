# Unit Converter

A simple web-based **Unit Converter** built using **Python (Flask)** for the backend and **HTML, CSS, JavaScript** for the frontend. This project allows users to convert between different measurement units.

## Features
- Convert between different units (length, weight, temperature, etc.)
- User-friendly interface with dropdown selections
- JavaScript for interactive UI updates
- Flask backend for handling conversions

## Project Structure
```
Unit_Converter/
│── app.py                  # Flask backend
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
│── /templates
│   ├── index.html          # Frontend HTML
│── /static
│   ├── style.css           # CSS for styling
│   ├── script.js           # JavaScript for interactivity
```

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/dishapawarkhausi/python-projects.git
cd python-projects/Unit_Converter
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App
```bash
python app.py
```

The application will start and be accessible at:
```
http://127.0.0.1:5000/
```

## Usage
1. Enter the value you want to convert.
2. Select the conversion type.
3. Click the "Convert" button to see the result.

## Technologies Used
- **Python** (Flask) - Backend
- **HTML, CSS** - Frontend
- **JavaScript** - Interactive elements

## Contributing
Feel free to fork this repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License.

---

