import os
from glob import glob
from pathlib import Path

import torch

from talkative_llm.llm import (AlpacaLoraCaller, CohereCaller,
                               HuggingFaceCaller, MPTCaller, OpenAICaller)

CONFIG_DIR = Path(__file__).parent / 'configs'
CACHE_DIR = Path(__file__).parent.parent / '.cache'

PROMPTS = ['The former Tour de France winner Lance Armstrong has admitted to what wrongdoing?',
           'Last summer we went to the beach on lake Michigan. It was a windy day and the waves were huge. There was a warning posted on the beach, warning the swimmers of something. What was the warning?',
           'In 1995 a member of the synthpop band Depeche Mode called it quits. Some fans still feel despondent about him leaving the band. Why is that (hint: what were his greatest contributions to the success of the band)? ',
           'A bicycle has 2 wheels and goes 10 mile per hour. A tricycle has 3 wheels and goes how fast? ',
           'Complete this line: I see a little silhouetto of a man ']

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["HF_DATASETS_CACHE"]=str(CACHE_DIR)
print("Using cache:" + str(CACHE_DIR))

def print_results(prompts, answers):
    for p, a in zip(prompts, answers):
        a = a['generation']
        if p in a:
            a = a.replace(p, '')
        a = a.strip()
        print("PROMPT: " + p)
        print("ANSWER: " + a)
        print()

def openai_caller_completion():
    config_path = str(CONFIG_DIR / 'openai' / 'openai_completion_example.yaml')
    caller = OpenAICaller(config=config_path)
    results = caller.generate(PROMPTS)
    print_results(PROMPTS, results)
    del caller


def huggingface_caller(config_path: str):
    #print(f'Testing {os.path.basename(config_path)}')
    caller = HuggingFaceCaller(config=config_path)
    results = caller.generate(PROMPTS)
    print_results(PROMPTS, results)
    del caller
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

print("GPT-3.5-turbo")
openai_caller_completion()
print("GEMMA-7b-it")
huggingface_caller(CONFIG_DIR / 'huggingface/gemma_llm_example.yaml')
print("Mistral-7B-v0.1")
huggingface_caller(CONFIG_DIR / 'huggingface/mistral_llm_example.yaml')
