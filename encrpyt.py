import cv2
import os
import streamlit as st

def text_to_ascii(text):
    'convert the text message to ascii'
    return [ord(char) for char in text]

def encrypt_message(image_path, secret_message, password):
    'encrypt message into image'
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image file not found. Check the file path.")
        return
    
    ascii_values = text_to_ascii(secret_message)
    message_length = len(ascii_values)
    ascii_values = [message_length] + ascii_values

    n, m = 0, 0

    for val in ascii_values:
        img[n, m, 0] = val
        m += 1
        if m >= img.shape[1]:
            m = 0
            n += 1
            if n >= img.shape[0]:
                print("Message too long for the image!")
                return

    output_img = "encryptedImage.png"
    cv2.imwrite(output_img, img)
    print("Message encrypted and saved as", output_img)

    with open("password.txt", "w") as f:
        f.write(password)

    os.system(f"start {output_img}")


# Input Cover Image
print("Note: Please Enter cover image name extension carefully")
image_path = input("Enter image path: ") 

# Secret Message
message = input("Enter secret message: ")

# Enter password
password = input("Enter a passcode: ")

encrypt_message(image_path, message, password)
