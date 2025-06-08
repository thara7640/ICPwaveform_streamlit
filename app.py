import streamlit as st
import torch
import pathlib
import pickle
import io
from pathlib import WindowsPath
from PIL import Image
import numpy as np
import cv2

def main():
    image_ban = Image.open('images/image2.png')
    st.image(image_ban, use_container_width=False)

if __name__ == '__main__':
        main()

# Temporary fix for PosixPath loading error on Windows
pathlib.PosixPath = WindowsPath

def letterbox(img, new_shape=(640, 640), color=(114, 114, 114)):
    import math
    shape = img.shape[:2]  # current shape [height, width]
    r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
    new_unpad = (int(round(shape[1] * r)), int(round(shape[0] * r)))
    dw = new_shape[1] - new_unpad[0]
    dh = new_shape[0] - new_unpad[1]
    dw /= 2  # divide padding into 2 sides
    dh /= 2

    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    img = cv2.resize(img, new_unpad, interpolation=cv2.INTER_LINEAR)
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

    return img


@st.cache_resource
def load_model():
    return torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

model = load_model()

st.title("YOLOv5 Detection for ICP Waveforms")
st.markdown("Upload an image to detect poor brain compliance using YOLOv5.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    results = model(image)
    results.render()

    output_image = Image.fromarray(results.ims[0])
    st.image(output_image, caption="Detection Result", use_column_width=True)
