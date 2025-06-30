import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt



color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
              'white': [[180, 18, 255], [0, 0, 231]],
              'red_1': [[180, 255, 255], [159, 50, 70]],
              'red_2': [[9, 255, 255], [0, 50, 70]],
              'green': [[89, 255, 255], [36, 50, 70]],
              'blue': [[128, 255, 255], [90, 50, 70]],
              'yellow': [[35, 255, 255], [25, 50, 70]],
              'purple': [[158, 255, 255], [129, 50, 70]],
              'orange': [[24, 255, 255], [10, 50, 70]],
              'gray': [[180, 18, 230], [0, 0, 40]]}

if 'colors' not in st.session_state:
    st.session_state.colors = {}
    
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = []

def get_colors(img_hsv):
    st.session_state.colors = {}
    for h in range(img_hsv.shape[0]):
        for w in range(img_hsv.shape[1]):
            hsv_pixel = img_hsv[h,w, :]
            hue = hsv_pixel[0]
            saturation = hsv_pixel[1]
            value = hsv_pixel[2]
            for color in color_dict_HSV.keys():
                if ((color_dict_HSV[color][0][0]>= hue >=color_dict_HSV[color][1][0]) \
                    and (color_dict_HSV[color][0][1]>= saturation >=color_dict_HSV[color][1][1]) \
                    and (color_dict_HSV[color][0][2]>= value >=color_dict_HSV[color][1][2])):
                    if color.split('_')[0] not in st.session_state.colors:
                        st.session_state.colors[color.split('_')[0]] = 0
                    st.session_state.colors[color.split('_')[0]]+=1
    st.session_state.colors = dict(sorted(st.session_state.colors.items(), reverse=True))
    
def segment_by__color(image, color):
    image_copy = image.copy()
    img_hsv = cv2.cvtColor(image_copy, cv2.COLOR_BGR2HSV)
    for h in range(img_hsv.shape[0]):
        for w in range(img_hsv.shape[1]):
            hsv_pixel = img_hsv[h,w, :]
            hue = hsv_pixel[0]
            saturation = hsv_pixel[1]
            value = hsv_pixel[2]
            if not((color_dict_HSV[color][0][0]>= hue >=color_dict_HSV[color][1][0]) \
                and (color_dict_HSV[color][0][1]>= saturation >=color_dict_HSV[color][1][1]) \
                and (color_dict_HSV[color][0][2]>= value >=color_dict_HSV[color][1][2])):
                image_copy[h,w, :] = [0,0,0]
    bw = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    mask = cv2.threshold(bw, 1, 255, cv2.THRESH_BINARY)[1]
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,  np.ones((5,5),np.uint8))
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    external_contours = np.zeros(mask.shape)
    for i in range(len(contours)):
        if hierarchy[0][i][-1] == -1:
            cv2.drawContours(external_contours, contours, i, 255, -1)
    mask = external_contours.astype('uint8')
    fin = cv2.bitwise_and(image, image, mask=mask)
    return fin

st.title("Color Segmentation App")

uploaded_files = st.file_uploader(
    "Choose a picture to segment", accept_multiple_files=True
)
image = None
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    image = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    if uploaded_file.name not in st.session_state.uploaded_files:
        print('loaded')
        st.session_state.uploaded_files.append(uploaded_file.name)
        get_colors(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
if image is not None:
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption='Uploaded Image',  width=300)
    st.selectbox("Select a color to segment", options=list(st.session_state.colors.keys()), key="color_selection")
    if st.session_state.color_selection:
        segmented_image = segment_by__color(image, st.session_state.color_selection)
        st.image(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB), caption=f'Segmented Image by {st.session_state.color_selection}', width=300)
    



                            