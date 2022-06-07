import os
from PIL import Image, ImageDraw, ImageFont
# from .models import FontImage

def making_text_image(ttf_font):
    text = "훈민정음 28자"

    # 폰트를 가운데 위치하도록 할 때
    iw = 400
    ih = 150

    font = ImageFont.truetype(ttf_font, size=48)

    w, h = font.getsize(text)
    image = Image.new("RGB", (iw, ih), (52,58,64))
    draw = ImageDraw.Draw(image)

    mx, my = (iw - w) // 2, (ih - h) // 2
    draw.text((mx, my), text, font=font, fill="white")

    del draw

    # image=image.resize((image.width * 2, image.height * 2))

    # image.show()

    # font_image=FontImage()
    # font_image.image_file=draw
    # font_image.save()

    # image.save(output_path+"")

    return image


def font_to_image():
    output_path = "C:/Study/font_mid_study/fmproject/static/img/"
    font_path = "C:/Users/SM-PC/AppData/Local/Microsoft/Windows/Fonts/"
    ttf_path = ['ACC어린이마음고운체', 'DOSGothic', 'ELAND 초이스 L', 'Gaegu-Bold', 'Ghanachocolate', 'GmarketSansTTFLight', 'Goyang',
                'HSBombaram3.0_Thin', 'IBMPlexSansKR-Medium', 'JejuHallasan', 'KITA', 'MapoAgape', 'MapoMaponaru', 'MaruBuri-Bold',
                'ONE Mobile POP', 'RixYeoljeongdo Regular', 'SANGJU Gyeongcheon Island', 'THEFACESHOP INKLIPQUID', 'TMONBlack', 'hy궁서',
                '강한육군 Medium', '경기천년바탕_Regular', '국립박물관문화재단클래식L', '서울한강 장체L', '솔뫼 김대건 Light', '조선일보명조']

    i = 0
    for a in ttf_path:
        img = making_text_image(font_path + a + ".ttf")
        img.save(output_path + str(i) + ".png")
        i += 1

#font_to_image()


def font_to_image_all():
    output_path = "C:/font_jmage/"
    font_path = "C:/Users/SM-PC/AppData/Local/Microsoft/Windows/Fonts/"
    file_list = os.listdir(font_path)

    for a in file_list:
        font_name, ext = os.path.splitext(a)

        if ext != ".ttf":
            continue

        img = making_text_image(font_path + a)
        img.save(output_path + font_name + ".png")

font_to_image()