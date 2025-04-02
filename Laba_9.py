from PIL import Image, ImageEnhance, ImageFilter, ImageFont, ImageDraw
import os

# 9.1
def image_info(image_path):
    try:
        img = Image.open(image_path)
        print(f"Размер изображения: {img.width}x{img.height}")
        print(f"Формат изображения: {img.format}")
        print(f"Цветовая модель: {img.mode}")
    except FileNotFoundError:
        print(f"Файл {image_path} не найден.")

# 9.2
def resize_and_flip(image_path):
    try:
        img = Image.open(image_path)
        resized_img = img.resize((img.width // 3, img.height // 3))
        resized_img.save("resized_" + os.path.basename(image_path))
        flipped_img_h = img.transpose(Image.FLIP_LEFT_RIGHT)
        flipped_img_h.save("flipped_h_" + os.path.basename(image_path))
        flipped_img_v = img.transpose(Image.FLIP_TOP_BOTTOM)
        flipped_img_v.save("flipped_v_" + os.path.basename(image_path))
    except FileNotFoundError:
        print(f"Файл {image_path} не найден.")


# 9.3
def apply_filter(input_folder, output_folder, filter_type):
    if not os.path.exists("output_images"):
        os.makedirs("output_images")
    for i in range(1, 6):
        try:
            image_path = os.path.join(input_folder, f"{i}.jpg")
            img = Image.open(image_path)
            if filter_type == "sharpen":
                filtered_img = img.filter(ImageFilter.SHARPEN)
            elif filter_type == "edge_enhance":
                filtered_img = img.filter(ImageFilter.EDGE_ENHANCE)
            elif filter_type == "emboss":
                filtered_img = img.filter(ImageFilter.EMBOSS)
            elif filter_type == "contour":
                filtered_img = img.filter(ImageFilter.CONTOUR)
            elif filter_type == "detail":
                 filtered_img = img.filter(ImageFilter.DETAIL)
            else:
                print(f"Фильтр {filter_type} не поддерживается.")
                return
            filtered_img.save(os.path.join(output_folder, f"filtered_{i}.jpg"))
        except FileNotFoundError:
            print(f"Файл {image_path} не найден.")

# 9.4
def watermark_text(input_image_path, output_image_path, text, pos):
    if not os.path.exists("watermarked_images"):
        os.makedirs("watermarked_images")
    photo = Image.open(input_image_path)
    drawing = ImageDraw.Draw(photo)
    black = (3, 8, 12)
    font = ImageFont.truetype("Times New Roman.ttf", 36)
    drawing.text(pos, text, fill=black, font=font)
    photo.save(os.path.join("watermarked_images", output_image_path))

image_info("image.jpg")
resize_and_flip("image.jpg")
apply_filter("input_images", "output_images", "contour")
watermark_text("image.png", "Image_watermarkered.png",text='Никулин Вадим', pos=(510, 260))

for i in range(1,6):
    watermark_text(f"{i}.jpg", f"Image_watermarkered_{i}.jpg", text='Никулин Вадим', pos=(510, 260))
