from ibm_watson_machine_learning.foundation_models import Model

model_id = "meta-llama/llama-2-13b-chat"
my_credentials = {"url": "https://us-south.ml.cloud.ibm.com"}
gen_parms = {"max_new_tokens": 256, "temperature": 0.1}
project_id = "skills-network"

model = Model(model_id, my_credentials, gen_parms, project_id)

prompt_txt = "How to be a good Data Scientist?"
generated_response = model.generate(prompt_txt)
generated_text = generated_response["results"][0]["generated_text"]

print(generated_text)

