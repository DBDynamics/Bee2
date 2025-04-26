from PIL import Image
import os

def resize_image(input_path, output_path, scale_factor):
    """
    缩放图片并保存
    :param input_path: 输入图片路径
    :param output_path: 输出图片路径
    :param scale_factor: 缩放比例(0-1)
    """
    try:
        with Image.open(input_path) as img:
            width, height = img.size
            new_size = (int(width * scale_factor), int(height * scale_factor))
            resized_img = img.resize(new_size, Image.LANCZOS)
            resized_img.save(output_path)
            print(f"图片已成功缩放并保存到 {output_path}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    input_img = input("请输入要缩放的图片路径: ")
    output_img = input("请输入缩放后保存的路径: ")
    scale = float(input("请输入缩放比例(0-1): "))
    
    resize_image(input_img, output_img, scale)