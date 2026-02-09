import gradio as gr
def predict(text): return "Positive!" if "good" in text else "Negative!"
gr.Interface(fn=predict, inputs="text", outputs="text").launch()
