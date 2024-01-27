import streamlit as st
from PIL import Image,ImageFilter
with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")
    if camera_image:
        img = Image.open(camera_image)
        gray_scale = img.convert('L')
        im_blurred = img.filter(filter=ImageFilter.BLUR)
        st.image(im_blurred)
