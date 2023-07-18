# when using the API you must format the prompts like:
#
# const userQuestion = "Why is the sky blue?";
# const prompt = `\n\nHuman: ${userQuestion}\n\nAssistant:`;
# // Send prompt to Claude via API

import os

import dotenv
import httpx
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

# pip install anthropic

dotenv.load_dotenv()

# Configure the default for all requests:
anthropic = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
    # default is 60s
    timeout=20.0,
)

# More granular control:
anthropic_1 = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
anthropic.with_options(
    timeout=5 * 1000,
    api_key=os.environ.get("ANTHROPIC_API_KEY")).completions.create(
    prompt=f"{HUMAN_PROMPT} Where can I get a good coffee in my neighbourhood? {AI_PROMPT}",
    max_tokens_to_sample=300,
    model="claude-2",
)
