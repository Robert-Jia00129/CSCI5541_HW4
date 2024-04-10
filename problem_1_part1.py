from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a block of text, and your task is to extract a list of keywords from it."
    },
    {
      "role": "user",
      "content": "The computational trend of NLP research is shifting from feature engineering to representation learning to pretraining-finetuning to very recently prompt engineering with large language models (LLM). Large language models (or other generative models trained on other modalities) allow the extraction of diverse and intrinsic knowledge from human-written texts/images/videos and their pairs. This assignment requires you to explore the limits and capabilities of large language models by designing your own prompts to interact with LLMs, observing their outputs, understanding their shortcomings, or creating your own datasets.\n"
    }
  ],
  temperature=0.5,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response.choices[0].message.content)

# output:
# - NLP research
# - feature engineering
# - representation learning
# - pretraining-finetuning
# - prompt engineering
# - large language models
# - generative models
# - human-written texts
# - images
# - videos
# - knowledge extraction
# - prompts
# - outputs
# - shortcomings
# - datasets
