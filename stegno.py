import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from stegano import lsb


# function to encode text in the image
def encode():
    # get the image path and text from the text box
    img_path = filedialog.askopenfilename(title="Select Image", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")))
    text = text_box.get("1.0", tk.END)

    # open the image and encode the text in it
    img = Image.open(img_path)
    encoded_img = lsb.hide(img, text)

    # save the encoded image
    encoded_img.save("encoded.png")

    # show success message to the user
    messagebox.showinfo("Success", "Text encoded successfully!")
    text_box.delete("1.0", tk.END)

    # display the input and encoded images
    input_img = ImageTk.PhotoImage(img)
    encoded_img = ImageTk.PhotoImage(encoded_img)
    input_label.config(image=input_img)
    input_label.image = input_img
    encoded_label.config(image=encoded_img)
    encoded_label.image = encoded_img
  


# function to decode text from the image
# function to decode text from the image
def decode():
    # get the image path from the user
    img_path = filedialog.askopenfilename(title="Select Image", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")))

    # decode the text from the image
    decoded_text = lsb.reveal(Image.open(img_path))

    # show the decoded text in a message box
    messagebox.showinfo("Decoded Text", decoded_text)

    # clear the text box
    text_box.delete("1.0", tk.END)



# create a GUI window
root = tk.Tk()
root.title("Text in Image")

# create a text box for entering the text
text_box = tk.Text(root, height=10, width=50)
text_box.pack(padx=10, pady=10)

# create a button to encode text
encode_button = tk.Button(root, text="Encode Text", command=encode)
encode_button.pack(padx=10, pady=10)

# create a button to decode text
decode_button = tk.Button(root, text="Decode Text", command=decode)
decode_button.pack(padx=10, pady=10)

# create labels to display the input and encoded images
input_label = tk.Label(root, text="Input Image")
input_label.pack(padx=10, pady=10)
encoded_label = tk.Label(root, text="Encoded Image")
encoded_label.pack(padx=10, pady=10)

# run the GUI window
root.mainloop()