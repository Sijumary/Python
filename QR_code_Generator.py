import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import os

#defining fuction that takes in a text parameter and generates QR code

def generate_qr(text):
    qr = qrcode.QRCode(   # an instance of the QRCode class from the qrcode library is created.
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # sets the error correction level to high (H), allowing for about 30% of the QR code to be restored if damaged.
        box_size=10,
        border=4,
        )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white') # creates an image representation of the generated QR code.
    filename = 'qr_code.png'  # A filename (qr_code.png) is defined for saving the generated image.
    img.save(filename)
    return filename

# define function which allows the user to save the generated QR code

def save_qr(filename):
    filepath = filedialog.asksaveasfilename(defaultextention='.png', filetypes=[('PNG Images', '*.png')])

    if filepath:
        os.rename(filename,filepath)
        messagebox.showinfo('QR code Saved!')

# define a function which creates main window, labels, entry field, canvas and buttons needed for QR code

def create_window():
    window = tk.Tk()
    window.title('QR Code Generator')

    label = tk.Label(window, text='Enter the text/URL:')
    label.pack()

    ent = tk.Entry(window)
    ent.pack()

    canvas = tk.Canvas(window, width=200, height=200)
    canvas.pack()

def generate_and_display():
    text = ent.get()
    filename = generate_qr(text)
    photo = ImageTk.PhotoImage(Image.open(filename))
    canvas.create_image(100, 100, image=photo)
    button2 = tk.Button(window, text='Save QR Code', command=lambda: save_qr(filename))
    button2.pack()
    window.mainloop()

    button = tk.Button(window, text='Generate QR Code', command=generate_and_display)
    button.pack()

    window.mainloop()

if __name__ == '__main__':
    create_window()
    generate_qr('Hello World!')
