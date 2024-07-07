import base64

# Replace 'local_image.png' with the path to your local image file
with open("docs_image.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# Save the encoded string to a file
with open("encoded_image.txt", "w") as file:
    file.write(encoded_string)
