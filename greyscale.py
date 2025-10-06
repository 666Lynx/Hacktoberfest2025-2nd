from PIL import Image
image_path = "input.jpg"
image = Image.open(image_path)
gray_image = image.convert("L")
gray_image.save("grayscale_output.jpg")
print("✅ Image successfully converted to grayscale and saved as grayscale_output.jpg")
