from fastai.vision.all import *
import gradio as gr

# import os
# os.system("pip uninstall -y gradio")
# os.system("pip install gradio==3.16.0")

art_style_labels = (
    'Abstract Expressionism',
    'Baroque',
    'Contemporary',
    'Cubism',
    'Impressionism',
    'Minimalism',
    'Pop Art',
    'Realism',
    'Renaissance',
    'Surrealism')

model = load_learner('models/art_style_model_v6.pkl')


def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(art_style_labels, map(float, probs)))


image = gr.Image()
label = gr.Label()
examples = [
    'test_images/unknown_01.jpg',
    'test_images/unknown_02.jpg',
    'test_images/unknown_03.jpg',
    'test_images/unknown_04.jpg'
]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False, share=True)
