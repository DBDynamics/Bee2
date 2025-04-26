from PIL import Image

def invert_image_colors(input_path, output_path):
    """
    反转图片颜色
    :param input_path: 输入图片路径
    :param output_path: 输出图片路径
    """
    try:
        # 打开图片文件
        with Image.open(input_path) as img:
            # 如果是RGBA模式，转换为RGB模式处理
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            
            # 反转颜色
            inverted_img = Image.eval(img, lambda x: 255 - x)
            
            # 保存处理后的图片
            inverted_img.save(output_path)
            print(f"图片颜色反转完成，已保存到: {output_path}")
    except Exception as e:
        print(f"处理图片时出错: {e}")

if __name__ == "__main__":
    input_image = input("请输入要处理的图片路径: ")
    output_image = input("请输入保存路径: ")
    invert_image_colors(input_image, output_image)