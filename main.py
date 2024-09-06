from aip import AipImageProcess
from PIL import Image
from io import BytesIO
import base64

""" 你的 APPID AK SK """
APP_ID = '114693544'
API_KEY: str = 'kDZoppUtyl1MyzbIy1KeWSPw'
SECRET_KEY: str = 'UDE3YkThMpI59mO5AKfxwmB5JfWOE2oF'

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


client = AipImageProcess(APP_ID, API_KEY, SECRET_KEY)
file_path = r"E:\Users\Administrator\Desktop\公司\恒泰通\素材\16图片\06.png"
image = get_file_content(file_path)

# 调用图像清晰度增强
res_image = client.imageDefinitionEnhance(image)
image_b = base64.b64decode(res_image['image'])

path_list = file_path.split('.')
img_path = "".join(path_list[:-1]) + '-changed.' + path_list[-1]
# img_path = 'changed_images/img_c2.jpg'

with open(img_path, "wb") as img:
    img.write(image_b)
