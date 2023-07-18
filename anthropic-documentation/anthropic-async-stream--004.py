import os

import dotenv
from anthropic import HUMAN_PROMPT, AI_PROMPT, AsyncAnthropic
dotenv.load_dotenv()

anthropic = AsyncAnthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

stream = await anthropic.completions.create(
    prompt=f"{HUMAN_PROMPT} Your prompt here {AI_PROMPT}",
    max_tokens_to_sample=300,
    model="claude-2",
    stream=True,
)
async for completion in stream:
    print(completion.completion)
