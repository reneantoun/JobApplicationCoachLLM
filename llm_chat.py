from ibm_watson_machine_learning.foundation_models import Model
import gradio as gr

my_credentials = {"url": "https://us-south.ml.cloud.ibm.com"}
model_id = "meta-llama/llama-2-13b-chat"
project_id = "skills-network"

gen_parms = {"max_new_tokens": 512, "temperature": 0.1}

model = Model(model_id, my_credentials, gen_parms, project_id)

def generate_response(prompt_txt):
    generated_response = model.generate(prompt_txt)
    generated_text = generated_response["results"][0]["generated_text"]
    return generated_text

chat_application = gr.Interface(
    fn=generate_response,
    allow_flagging="never",
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Output"),
    title="Watsonx.ai Chatbot",
    description="Ask any question and the chatbot will try to answer."
)

chat_application.launch()
