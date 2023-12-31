import asyncio
import os

import dotenv
# pip install anthropic
from anthropic import HUMAN_PROMPT, AI_PROMPT, AsyncAnthropic

dotenv.load_dotenv()

anthropic = AsyncAnthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


async def main():
    completion = await anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=300,
        prompt=f"{HUMAN_PROMPT} how does a court case get to the Supreme Court? {AI_PROMPT}",
    )
    print(completion.completion)


asyncio.run(main())