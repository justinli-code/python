# install qrcode module by 'pip install qrcode'
# install imageio module by 'pip install imageio'
# install pillow module by 'pip install pillow'
# install matplotlib by 'pip install matplotlib'

"""
import qrcode
qr = qrcode.QRCode(
    version=1,#调整版式1-40(30-40无法扫描)
    border=8,#边框大小
)
qr.add_data("")#输入你想扫描的内容
img = qr.make_image(fill_color="black",back_color="white")
img.save("text.jpg")
"""

#!/user/bin/Python3

import qrcode
from PIL import Image
import matplotlib.pyplot as plt

def getQRcode(strs, name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=40,
        border=2,
    )
    # 添加数据
    qr.add_data(strs)
    # 填充数据
    qr.make(fit=True)
    # 生成图片
    img = qr.make_image(fill_color="black", back_color="red")
    img = img.convert("CMYK")  # RGBA
    # 添加logo
    # icon = Image.open("F:\\李泽洋小学\\python\\mmm.png")
    icon = Image.open("y.png")
    # 获取图片的宽高
    img_w, img_h = img.size
    factor = 6
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # 重新设置logo的尺寸
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    img.paste(icon, (w, h), icon)
    # 显示图片
    plt.imshow(img)
    plt.show()
    img.save(name)
    return img


if __name__ == '__main__':
    getQRcode("以后少玩一会，别真正玩时没时间啦！", '01.png')
    print('execute.....')
