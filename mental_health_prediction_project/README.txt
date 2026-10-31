MINDCARE - MENTAL HEALTH PREDICTION ML DEMO
===========================================

WHAT IS INCLUDED
- app.py: Flask backend, synthetic dataset generation, Random Forest training,
  evaluation metrics and prediction API.
- templates/index.html: Web page.
- static/style.css: Styling and responsive layout.
- static/script.js: Slider updates and API request handling.
- requirements.txt: Python packages.

REQUIREMENTS
- Python 3.10 or newer (Python 3.14 may have package compatibility differences)
- Visual Studio Code
- Internet connection for first-time package installation and Google Fonts/Chart.js CDN
  (the app itself does not require an external prediction API).

RUN IN VS CODE (WINDOWS)
1. Extract the ZIP file.
2. Open VS Code.
3. Select File > Open Folder and choose the extracted "mental_health_prediction" folder.
4. Open Terminal > New Terminal.
5. Create a virtual environment:
      py -m venv .venv
6. Activate it:
      .venv\Scripts\activate
7. Install dependencies:
      python -m pip install --upgrade pip
      python -m pip install -r requirements.txt
8. Start the app:
      python app.py
9. Open this address in Chrome:
      http://127.0.0.1:5000
10. To stop the server, click the terminal and press Ctrl+C.

IF 'py' IS NOT RECOGNIZED
Try:
      python -m venv .venv

IF INSTALLATION FAILS
Use Python 3.11 or 3.12, then repeat the virtual-environment and installation steps.
Do not install packages into a different Python environment from the one running app.py.

HOW IT WORKS
- Creates 2,000 artificial examples with five numeric features, each from 0 to 10.
- Uses a synthetic rule with random noise to create two classes.
- Splits the data into 80% training and 20% testing.
- Trains a RandomForestClassifier with 180 trees.
- Calculates Accuracy, Precision, Recall and F1-score on the test set.
- Uses the trained model to classify the five slider values entered on the page.

IMPORTANT LIMITATION
This is a classroom demonstration using artificial data, not a validated mental-health
screening instrument. "Higher-risk pattern" is only a synthetic model class. It does
not diagnose, predict, or assess a real person's mental health. Do not use it for
clinical or personal health decisions.
