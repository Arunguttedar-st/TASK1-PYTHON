import os
import qrcode


def generate_qr_code(text_data, file_name="output_qr"):
    # Ensure the output filename ends with .png extension
    if not file_name.endswith(".png"):
        file_name += ".png"

    # Configure the QR Code parameters
    qr = qrcode.QRCode(
        version=1,  # Controls matrix size (1 is 21x21 grid)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% recovery capacity
        box_size=10,  # Dimensions of each module box in pixels
        border=4,  # Border margin width in boxes
    )

    # Attach payload data and auto-fit grid matrix
    qr.add_data(text_data)
    qr.make(fit=True)

    # Render image with custom pattern and background colors
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Save output image to disk
    qr_img.save(file_name)

    # Output status and absolute saved file destination
    full_path = os.path.abspath(file_name)
    print(f"Success! QR code saved at: {full_path}")


# Execution entry point
if __name__ == "__main__":
    user_input = input("Enter text or URL to encode: ")
    if user_input.strip():
        generate_qr_code(user_input, "my_generated_qr.png")
    else:
        print("Error: Input data cannot be empty.")