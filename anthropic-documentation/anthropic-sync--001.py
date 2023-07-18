# when using the API you must format the prompts like:
#
# const userQuestion = "Why is the sky blue?";
# const prompt = `\n\nHuman: ${userQuestion}\n\nAssistant:`;
# // Send prompt to Claude via API
import asyncio

# pip install anthropic
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT, AsyncAnthropic
import dotenv
import os

dotenv.load_dotenv()

anthropic = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# POST: /v1/complete
completion = anthropic.completions.create(
    # mandatory parameters :-
    # ["max_tokens_to_sample", "model", "prompt"], ["max_tokens_to_sample", "model", "prompt", "stream"]
    model="claude-2", # claude-1
    max_tokens_to_sample=300, # The maximum number of tokens to generate before stopping.
    temperature=0.7,
    # top_k=,
    # top_p=
    # extra-headers =   # Ex. Headers | None. default_headers={"anthropic-version": "My-Custom-Value"},
    # extra_query =     # Add additional query parameters to the request. Ex. Query | None
    # extra_body =      # Add additional JSON properties to the request. Ex. Body | None
    # timeout =         # Override the client-level default timeout for this request, in seconds
    prompt=f"{HUMAN_PROMPT} how does a court case get to the Supreme Court? {AI_PROMPT}",
)
print(completion.completion)

