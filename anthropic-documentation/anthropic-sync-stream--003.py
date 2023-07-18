# pip install anthropic
import os

import dotenv
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

dotenv.load_dotenv()

anthropic = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

stream = anthropic.completions.create(
    prompt=f"{HUMAN_PROMPT} Your prompt here {AI_PROMPT}",
    max_tokens_to_sample=300,
    model="claude-2",
    stream=True,
)
for completion in stream:
    print(completion.completion)
