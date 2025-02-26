import cv2

def ascii_to_text(ascii_values):
    'Convert ascii to text'
    return ''.join(chr(val) for val in ascii_values)

def decrypt_message(image_path):
    'Decrypt the message'
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found. Check the file path.")
        return

    try:
        with open("password.txt", "r") as f:
            stored_password = f.read().strip()
    except FileNotFoundError:
        print("Error: Password file not found.")
        return

    user_pass = input("Enter passcode for decryption: ")
    if user_pass != stored_password:
        print("YOU ARE NOT AUTHORIZED!")
        return

    n, m = 0, 0
    ascii_values = []

    message_length = img[n, m, 0]
    m += 1
    if m >= img.shape[1]:
        m = 0
        n += 1

    for _ in range(message_length):
        ascii_values.append(img[n, m, 0])
        m += 1
        if m >= img.shape[1]:
            m = 0
            n += 1

    decrypted_message = ascii_to_text(ascii_values)
    print("Decrypted Message:", decrypted_message)

    with open('Secret Information.txt', 'w') as f:
        f.write(decrypted_message)

image_path = "encryptedImage.png"
decrypt_message(image_path)
