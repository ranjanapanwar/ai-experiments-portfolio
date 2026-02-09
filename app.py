import gradio as gr
from transformers import pipeline

# Load pre-trained sentiment model (downloads automatically)
classifier = pipeline("sentiment-analysis")


def predict_sentiment(text):
    result = classifier(text)[0]
    label = result['label']
    score = f"{result['score']:.2%}"
    return f"Sentiment: **{label}** (confidence: {score})"


# Create interface
with gr.Blocks(title="Sentiment Analyzer") as demo:
    gr.Markdown("# 🚀 AI Sentiment Analyzer")
    gr.Markdown("Enter text to analyze sentiment (positive/negative)")

    with gr.Row():
        text_input = gr.Textbox(
            label="Your Text",
            placeholder="I love this app!",
            lines=2
        )
        sentiment_output = gr.Markdown()

    analyze_btn = gr.Button("Analyze", variant="primary")

    analyze_btn.click(
        fn=predict_sentiment,
        inputs=text_input,
        outputs=sentiment_output
    )

    gr.Examples(
        examples=[
            "This movie was amazing!",
            "I hate this product",
            "It's okay, nothing special"
        ],
        inputs=text_input
    )

if __name__ == "__main__":
    demo.launch()
