import os
import tkinter as tk
from tkinter import messagebox, PhotoImage
import base64
import openai
from PIL import Image, ImageTk
import nltk
from nltk import word_tokenize


client = openai.OpenAI(api_key = 'YOUR_API_KEY_HERE')  # <-- replace "YOUR_API_KEY_HERE" with your openAI API key
# -----------------------------------------------------------------------------------------
OUTPUT_DIR= "outputs"

class TkinterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Generator")
        self.root.geometry("500x600")
        self.root.configure(bg="#ADD2FF")
        self.v = tk.IntVar()
        self.v.set(1)
        self.index = 0
        root.bind("<Return>", self.process)       # <-- kalei thn def process
        root.bind("<Left>", self.prevImg)         # <-- kalei thn prevImg gia image navigation
        root.bind("<Right>", self.nextImg)        # <-- kalei thn nextImg gia image navigation

        # Title
        tk.Label(
            root, text="AI Image Generator", font=("Courier New", 16, "bold"), fg="#1A3B63", bg="#ADD2FF"
        ).pack(pady=5)

        tk.Label(
            root, text="99.9% free. Kinda...", font=("Courier New", 8, "italic"), fg="#1A3B63", bg="#ADD2FF"
        ).pack(pady=2)

        # Easter egg
        pil_img = Image.open("GigaChad_Thodoris1.png").convert("RGBA")
        pil_img = pil_img.resize((100,100))
        self.chad_img = ImageTk.PhotoImage(pil_img)
        image_label = tk.Label(root, image=self.chad_img)
        image_label.pack(pady=5)

        # Rounded radio buttons
        tk.Radiobutton(
            root, text="One Variant", font=("Courier New", 12), fg="#1A3B63", bg="#ADD2FF", variable=self.v, value=1
        ).pack(pady=5)

        tk.Radiobutton(
            root, text="Three Variants", font=("Courier New", 12), fg="#1A3B63", bg="#ADD2FF", variable=self.v, value=2
        ).pack(pady=5)

        tk.Label(
            root, text="Write prompt on the textbox below", font=("Courier New", 8, "italic"), fg="#1A3B63", bg="#ADD2FF"
        ).pack(pady=2)

        self.image_label2 = tk.Label(root, text="image will appear here", image="")
        self.image_label2.pack(pady=5)

        # Fields
        input_frame = tk.Frame(root, bg="#FFFFFF")    # gia to text box
        input_frame.pack(pady=10)
        button_frame = tk.Frame(root, bg="#ADD2FF")  # gia ta "preview" kai "generate" buttons
        button_frame.pack(pady=10)

        self.input_field = tk.Entry(
            input_frame, width=40, font=("Courier New", 11), bg="#FFFFFF", fg="#1A3B63", insertbackground="grey"
        )
        self.input_field.pack(padx=5)

        # Preview button
        tk.Button(
            button_frame, text="Preview", font=("Courier New", 12), bg="#2C62A5", fg="#FFFFFF", activebackground="#45A049"
        , command= self.preview_first).pack(side=tk.LEFT, padx=5)

        # Generate Button
        tk.Button(
            button_frame, text="Generate", font=("Courier New", 12), bg="#2C62A5", fg="#FFFFFF",
            activebackground="#45A049", command= self.process  # <-- auto tha steilei thn apanthsh sthn process def
        ).pack(side=tk.RIGHT, padx=5)



    def process(self, event=None):  # event=None shmainei oti h process kaleitai kai me keybind apo to keyboard (to enter)
        global image_paths

        user = self.input_field.get()   # pairnei to input apo to text box
        print(user)

        if self.v.get() == 1:   # posa variants exoume?
            n = 1               # 1 variant
            print(n)
        else:
            n = 3               # 3 variants
            print(n)

        ideas = self.generate_ideas(user, n)
        image_paths = self.generate_images_from_ideas(ideas)

        self.index = 0           # h eikona pou tha mas deixnei to tkinter parathiro
        self.showImage(self.index)



    def showImage(self, index):
        global imagePreview
        img = Image.open(image_paths[self.index])
        img = img.resize((200,200))
        imagePreview = ImageTk.PhotoImage(img)
        self.image_label2.config(image=imagePreview)

    def nextImg(self, event=None):
        global index

        """ POLY SOS AUTO EDW """
        # edw, se periptwsh pou to index ginei 3, epeidh to index ksekinaei apo 0 kai tha bgei ektos oriwn,
        # tou leme na kanei mod me to mhkos ths image_paths (pou einai lista), wste se periptwsh pou to
        # index ginei 3, mesw ths mod na ginei ksana 0 gia na mas paei sthn arxikh eikona
        self.index = (self.index +1) % len(image_paths)
        self.showImage(self.index)

    def prevImg(self, event=None):
        global index
        if not image_paths:
            return
        self.index = (self.index -1) % len(image_paths)
        self.showImage(self.index)


    def preview_first(self):
        global index
        # anoigei thn eikona me thn efarmogh gia eikones ston yplogisth anti so ui
        if image_paths == True:
            os.startfile(image_paths[self.index])
        # edw me to image_paths[index] me bash to index (dhladh ti eikona blepoume) mas thn kanei preview


    def generate_ideas(self, user_text, n):
        prompt = f"Give me {n} house ideas about: {user_text} \n" \
                 f"Return ONLY {n} lines. No numbering, no bullets."

        # role = user shmainei oti stelnoume to mhnyma san users kai oxi san admins
        # content = prompt shmainei oti to content tou mhnymatos tha einai to prompt pou exoume grapsei apo panw
        # temperature einai to poso tha kathisei na to skeftei. Sthn periptwsh mas den theloume kai kati extreme, opote mpainei metrio 0.9
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.9
        )

        ideas=[]                                                       # list ideas opou tha ginetai append me ta ananewmena prompt ideas
        for line in resp.choices[0].message.content.splitlines():      # for loop: pairnei apo thn list choices ta ananewmena prompts kai ta kanei split lines an einai 3 variants
            print(line)
            line = line.strip()                                        # ksebrakoma (kanei to text raw)
            if line != "":
                ideas.append(line)
        return ideas[:n]


    def generate_images_from_ideas(self, ideas):
        paths = []

        for i in range(len(ideas)):
            img = client.images.generate(
                model = "gpt-image-1.5",
                prompt = ideas[i],
                size = "1024x1024",
                n = 1,
                output_format = "jpeg"
            )

            filepath = os.path.join(OUTPUT_DIR, f"request_{i+1}.jpg")

            b64= img.data[0].b64_json
            print(b64)
            with open(filepath, "wb") as f:
                f.write(base64.b64decode(b64))

            paths.append(filepath)

        return paths


# -----------------------------------------------------------------------------------------
def main():
    root = tk.Tk()
    window = TkinterWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
