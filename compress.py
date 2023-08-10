from tkinter import *
import tkinter as tk
import zlib, base64


def selected():
    label.config(text="selected: "+option.get())


root = Tk()
root.title("Compression/Decompression")
root.geometry("500x500")

frame = Frame(root, highlightthickness=1, highlightbackground="black",padx=20, pady=20)
frame.pack()


def compressWindow():

    compWindow = Toplevel(frame)
    compWindow.title("compression")
    compWindow.geometry("200x200")
    Label(compWindow, text="Compression").pack()

    label1 = Label(compWindow, text="File to be compressed: ")
    label1.pack()
    input_file = Entry(compWindow)
    input_file.pack()

    label2 = Label(compWindow, text="Name your new compressed file: ")
    label2.pack()
    output_file = Entry(compWindow)
    output_file.pack()

    button = Button(compWindow, text="Compress", command=lambda: compress(input_file.get(), output_file.get()))
    button.pack()

    def compress(inputfile, outputfile):
        data = open(inputfile, 'r').read()
        byte_data = bytes(data, 'utf-8')
        compressed_data = base64.b64encode(zlib.compress(byte_data, 9))
        decoded_data = compressed_data.decode('utf-8')
        compressed_file = open(outputfile, 'w')
        compressed_file.write(decoded_data)


def decompressWindow():
    decompWindow = Toplevel(frame)
    decompWindow.title("compression")
    decompWindow.geometry("200x200")
    Label(decompWindow, text="Decompression").pack()

    label1 = Label(decompWindow, text="File to be decompressed: ")
    label1.pack()
    input_file = Entry(decompWindow)
    input_file.pack()

    label2 = Label(decompWindow, text="Name your new decompressed file: ")
    label2.pack()
    output_file = Entry(decompWindow)
    output_file.pack()

    button = Button(decompWindow, text="Decompress", command=lambda: decompress(input_file.get(), output_file.get()))
    button.pack()

    def decompress(inputfile, outputfile):
        data = open(inputfile, 'r').read()
        encoded_data = data.encode('utf-8')
        decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
        decoded_data = decompressed_data.decode('utf-8')
        file = open(outputfile, 'w')
        file.write(decoded_data)
        file.close()


label = Label(frame, text="Action to be performed: ")
label.pack()
option = StringVar(value="compression")
radio1 = Radiobutton(frame, text="Compression", variable=option, value="Compression", command=selected)
radio2 = Radiobutton(frame, text="Decompression", variable=option, value="Decompression", command=selected)
radio1.pack()
radio2.pack()
btn = Button(frame, text="Proceed to compress", command=compressWindow)
btn.pack(pady=10)

btn = Button(frame, text="Proceed to decompress", command=decompressWindow)
btn.pack(pady=10)


root.mainloop()
