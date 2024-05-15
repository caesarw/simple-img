from PIL import Image, ImageEnhance
import io


def adjust_brightness(image_data, brightness_factor):
    image = Image.open(io.BytesIO(image_data))
    # Enhance the image by increasing the brightness by 30%
    enhancer = ImageEnhance.Brightness(image)
    enhanced_image = enhancer.enhance(brightness_factor)
    return enhanced_image
