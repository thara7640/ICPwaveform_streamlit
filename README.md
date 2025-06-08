✅ Step-by-Step Instructions
1. ✅ Install Python (if not installed)
Recommended: Python 3.9 – 3.11 (Python 3.12 may cause compatibility issues with PyTorch)

Download from: https://www.python.org/downloads/

2. ✅ Create and Activate a Virtual Environment (Optional but Recommended)

# Navigate to your project folder
cd path\to\your\project-folder

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
3. ✅ Install Required Packages
Install Streamlit, PyTorch, and YOLOv5 dependencies:

pip install streamlit torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install opencv-python pillow numpy
If you cloned YOLOv5 from GitHub, also run:

pip install -r yolov5/requirements.txt
4. ✅ Ensure Your Files Are in Place
Your folder should contain:

📁 project-folder/
├── app.py        ← your Streamlit script
├── best.pt       ← your trained YOLOv5 model
5. ✅ (Optional Fix) If You Encounter PosixPath Errors
Add this to the top of app.py:

python
import pathlib
from pathlib import WindowsPath
pathlib.PosixPath = WindowsPath
6. ▶️ Run Your Streamlit App
In the terminal, run:

streamlit run app.py
7. 🌐 Open the App in Browser
After running, Streamlit will open a browser tab automatically.

If not, visit http://localhost:8501 manually.
