import os

import dotenv
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT, APIConnectionError, RateLimitError, APIStatusError

dotenv.load_dotenv()

anthropic = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

try:
    anthropic.completions.create(
        prompt=f"{HUMAN_PROMPT} Your prompt here {AI_PROMPT}",
        max_tokens_to_sample=300,
        model="claude-2",
    )
except APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.

except RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")

except APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
