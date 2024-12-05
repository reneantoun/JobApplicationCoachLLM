import gradio as gr

def combine_sentences(sentence1, sentence2):
    return sentence1 + " " + sentence2

# Define the interface
demo = gr.Interface(
    fn=combine_sentences, 
    inputs=["text", "text"],  # Two text input fields
    outputs="text"  # Output field for the combined sentence
)

# Launch the interface
demo.launch(server_name="0.0.0.0", server_port=7861)
