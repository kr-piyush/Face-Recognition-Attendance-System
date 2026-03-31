# 🎓 Face Recognition Attendance System

A real-time attendance marking system using face recognition. It detects faces via webcam, matches them against known images, and automatically logs attendance with timestamps into a CSV file.

---

## 📁 Project Structure

```
CV/
├── app.py                  # Main Python script
├── Attendance.csv          # Auto-generated attendance log
└── README.md
```

---

## ⚙️ Prerequisites

Make sure you have the following installed on your system:

- **Python 3.7 – 3.10** (recommended)
- **pip** (Python package manager)
- **CMake** (required to build `dlib`)
- **A working webcam**

### Install CMake

- **Windows:** Download from [cmake.org](https://cmake.org/download/) and add to PATH
- **Linux:** `sudo apt install cmake`
- **macOS:** `brew install cmake`

---

## 🚀 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AnshumanJ28/CV.git
cd CV
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install opencv-python
pip install numpy
pip install face_recognition
```

> **Note:** `face_recognition` depends on `dlib`. If installation fails, install `dlib` manually first:
> ```bash
> pip install dlib
> pip install face_recognition
> ```
> On Windows, you may need to install Visual Studio Build Tools or use a pre-built `dlib` wheel from [here](https://github.com/jloh02/dlib/releases).

---

## 🖼️ Adding Known Faces

1. Create a folder named `Image` inside the project directory (if it doesn't exist):
   ```bash
   mkdir Image
   ```

2. Add photos of the people you want to recognize into the `Image/` folder.

3. **Naming Convention:** Name each image file after the person.
   - Use underscores for spaces: `John_Doe.jpg` → displays as `JOHN DOE`
   - Supported formats: `.jpg`, `.jpeg`, `.png`


> ⚠️ Make sure each image contains **exactly one clearly visible face** for best accuracy.

---

## ▶️ Running the Project

```bash
python app.py
```

If you have multiple Python versions installed:

```bash
python3 app.py
```

If your virtual environment isn't activated yet, activate it first, then run:

- **Windows:**
  ```bash
  venv\Scripts\activate
  python app.py
  ```
- **Linux / macOS:**
  ```bash
  source venv/bin/activate
  python app.py
  ```

On startup, the script will:
1. Load all images from the `Image/` folder
2. Encode the known faces
3. Print `"Encoding Complete"` in the terminal
4. Open your webcam feed

### Controls

| Key | Action        |
|-----|---------------|
| `Q` | Quit / Exit   |

---

## 📋 How It Works

1. **Image Loading** — Reads all images from the `Image/` folder and extracts face encodings.
2. **Webcam Feed** — Captures live video from the default webcam.
3. **Face Detection** — Detects faces in each frame (downscaled 4x for speed).
4. **Face Matching** — Compares detected faces against known encodings using a distance threshold of `0.5`.
5. **Attendance Marking** — If a match is found and the person hasn't been logged yet, their name and current time are saved to `Attendance.csv`.
6. **Visual Feedback:**
   - 🟢 **Green box** — Recognized person (name shown)
   - 🔴 **Red box** — Unknown face

---

## 📄 Attendance Log

Attendance is saved automatically to `Attendance.csv` in the project root:

- A new entry is added **only once per session** per person.
- The file is created automatically if it doesn't exist.

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---|---|
| `dlib` fails to install | Install CMake and Visual Studio Build Tools (Windows), then retry |
| Webcam not opening | Check that no other app is using the camera; try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` |
| `No module named face_recognition` | Run `pip install face_recognition` inside your virtual environment |
| Face not being recognized | Ensure the image in `Image/` folder is clear, well-lit, and contains only one face |
| Encoding takes too long | Reduce the number of images or use lower-resolution photos |

---

## 📦 Dependencies Summary

| Package | Purpose |
|---|---|
| `opencv-python` | Webcam capture & image rendering |
| `numpy` | Array operations for face distance |
| `face_recognition` | Face detection & encoding |
| `dlib` | Backend for `face_recognition` |

---

## 📌 Notes

- The system uses a **face distance threshold of `0.5`** — lower means stricter matching. You can adjust this in the code:
  ```python
  if matches[matchIndex] and faceDis[matchIndex] < 0.5:  # Change 0.5 as needed
  ```
- Works best in **good lighting conditions**.
- Tested on **Python 3.9**.

---

## 👨‍💻 Author

**Anshuman Jain**  
GitHub: [@kr-piyush](https://github.com/kr-piyush)
