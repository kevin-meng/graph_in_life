import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

# copy image: https://www.resizepixel.com/ 
def load_image(image_file):
    img = Image.open(image_file)
    return img

def img_circle(img_src,outline=2,outline_color=(205,201,201),img_width=None,local=True):
    # 增加添加边框功能
    # if not local:
    #     url = request.urlopen(url)
    # img_src = Image.open(url).convert("RGBA")
    if img_width is None:
        img_width = img_src.width
    x = min(img_src.height,img_src.width)
    r = int(x/2)
    # turn src image to square with x width
    # img_src = Image.open(fpath).convert("RGBA")    
    img_src = img_src.resize((x,x), Image.ANTIALIAS)
    
    # create a new pinture which is used for return value
    img_return = Image.new('RGBA', (x,x),(255,255,255,0))
    
    # create a white picture,alpha tunnuel is 100% transparent
    img_white = Image.new('RGBA',(x,x),(255,255,255,0))   
    
    img_outline = Image.new('RGBA',(x,x),outline_color)  
    # create the objects link to the pixel matrix of img
    p_src = img_src.load()  
    p_return = img_return.load()
    p_white = img_white.load()
    p_outline = img_outline.load()
    
    # set the pixels of the return picture
    for i in range(x):
        for j in range(x):
            lx = abs(i-r) 
            ly = abs(j-r)
            l  = (pow(lx,2) + pow(ly,2))** 0.5 
            
            if l < (r-outline):
                p_return[i,j] = p_src[i,j]
            elif l > r:
                p_return[i,j] = p_white[i,j]
            else :
                p_return[i,j] = p_outline[i,j]
    return img_return



uploaded_file = st.file_uploader("Choose a file")
# print(uploaded_file)

# 压缩
precent = st.slider('Select a range of values', 0.0, 1.0,0.75)

# 截取圆头像
crop_circle = st.checkbox('crop')


if uploaded_file is not None:
    st.image(load_image(uploaded_file), width=400)

    if crop_circle：
        img_circle()



# def 



