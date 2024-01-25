from PIL import Image, ImageDraw


def generate_catdog_image():
    # Создаем изображение
    width, height = 300, 200
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Загружаем шрифт (если нужен)
    # font = ImageFont.load_default()

    # Рисуем кота
    draw.text((50, 50), "🐱", fill="black")  # используем эмоджи для кота

    # Рисуем собаку
    draw.text((150, 50), "🐶", fill="black")  # используем эмоджи для собаки

    # Сохраняем изображение
    image.save("catdog_image.png")


# Генерируем изображение
if __name__ == '__main__':
    generate_catdog_image()
