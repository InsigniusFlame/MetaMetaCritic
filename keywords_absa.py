from scraper import review_text_list
from huggingface_hub import InferenceClient
import random

client = InferenceClient(api_key="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")
	
def construct_prompt(review_text):
    review = ""
    for r in review_text:
        review += str(review_text.index(r) + 1) + ") " + r + ". "
    prompt = f"""
    From the reviews below, summarize the Pros and Cons (in english) of the video game:
    Reviews: "{review}".
    """
    return prompt

prompt = construct_prompt(random.choices(review_text_list,k=15))
messages = [
	{ "role": "user", "content": f"{prompt}" }
]


stream = client.chat.completions.create(
    model="meta-llama/Llama-3.2-3B-Instruct", 
	messages=messages, 
	max_tokens=550,
	stream=True
)
output = ""
for chunk in stream:
    output += chunk.choices[0].delta.content
print(output)