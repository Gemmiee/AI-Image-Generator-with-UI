# 🖼️ AI Houses Image Generator (Python + Tkinter)

A simple **desktop AI image generator** built with **Python** and **Tkinter** which focuses on houses.
The app allows users to type a prompt and generate **AI-created images** using the OpenAI API.

The program can automatically generate **creative prompt ideas** and convert them into images that can be previewed and navigated inside the GUI.

---

## 📸 Preview Images


## ✨ Features

* **Prompt Idea Generation** – Uses an AI model to create creative prompt ideas based on user input.
* **Image Generation** – Generates images using an AI image model.
* **Desktop GUI** – Built with Tkinter for a simple graphical interface.
* **Multiple Variants** – Generate **1 or 3 image variations**.
* **Keyboard Navigation**

  * `Left Arrow` → previous image
  * `Right Arrow` → next image
  * `Enter` → generate images

* **Preview Option** – Open generated images using your OS image viewer.
* **Automatic Saving** – Images are stored locally in an `outputs/` folder.

---

## 📸 Example Workflow

1. User types a prompt about a house design (example: `"modern luxury beach house"`).
2. The program asks the AI to generate **creative house design ideas** based on the user's prompt.
3. Each idea then becomes a **prompt for image generation** but in fancier words.
4. Images are generated and saved locally.
5. The GUI displays them and allows navigation between variants.

---

## 🖥 Interface

The interface includes:

* Prompt input box
* Variant selection (1 or 3 images)
* Generate button
* Preview button
* Image viewer inside the window

Keyboard shortcuts make browsing generated images easy.

---

## 📦 Requirements

Install the required Python libraries:

```bash
pip install openai pillow nltk
```

You also need the standard libraries:

```
os
tkinter
base64
```

---

## 🔑 API Key Setup

You need an **OpenAI API key**.

Replace the key in the code:

```python
client = openai.OpenAI(api_key="YOUR_API_KEY")
```

---

## 📁 Project Structure

```
project-folder
│
├── outputs/                # Generated images
├── GigaChad_Thodoris1.png  # UI easter egg image
├── main.py                 # Main application script
└── README.md
```

---

## ▶️ Running the Application

Run the script:

```bash
python main.py
```

The GUI window will open and you can start generating images.

---

## 🎮 Controls

| Key / Button    | Action                |
| --------------- | --------------------- |
| Enter           | Generate images       |
| Left Arrow      | Previous image        |
| Right Arrow     | Next image            |
| Preview Button  | Open image externally |
| Generate Button | Create images         |

---

## ⚙️ How It Works

### 1️⃣ Prompt Idea Generation

The app sends the user input to an AI chat model which generates **creative prompt ideas**.

Example request:

```
Give me 3 house ideas about: futuristic eco home
Return ONLY 3 lines. No numbering, no bullets.
```

---

### 2️⃣ Image Generation

Each generated idea becomes a prompt for the **image model**:

```python
client.images.generate(
    model="gpt-image-1.5",
    prompt=idea,
    size="1024x1024"
)
```

The returned image is **Base64 encoded**, decoded, and saved locally.

---

### 3️⃣ GUI Display

The image is loaded with **Pillow** and displayed in the Tkinter window.

Users can cycle through images using keyboard arrows.

---

## 🧠 Libraries Used

* **Tkinter** – GUI
* **Pillow (PIL)** – image handling
* **OpenAI API** – prompt generation & image generation
* **NLTK** – text processing
* **Base64** – decoding generated images

---

## 🚀 Possible Improvements

Some ideas for future improvements:

* Save images with **timestamped filenames**
* Add **resolution selection**
* Add **image style presets**
* Implement **prompt history**
* Add **progress/loading indicator**
* Allow **custom output directory**
* Package the app as an **executable (.exe)**

---

## ⚠️ Disclaimer

This project is for **educational purposes** and demonstrates how to integrate:

* AI text generation
* AI image generation
* Python desktop GUIs

Usage of the OpenAI API may incur costs depending on your API plan.

---

## 📜 License

MIT License – feel free to modify and use the project.
