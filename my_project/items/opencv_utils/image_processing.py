# opencv_utils/image_processing.py
import cv2

def convert_to_grayscale(input_image_path: str, output_image_path: str) -> None:
    """Converts an image to grayscale and saves it."""
    image = cv2.imread(input_image_path)

    if image is None:
        raise FileNotFoundError(f"Image file not found at path: {input_image_path}")

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Save the grayscale image
    cv2.imwrite(output_image_path, grayscale_image)
