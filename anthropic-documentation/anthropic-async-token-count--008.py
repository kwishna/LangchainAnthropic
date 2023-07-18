#!/usr/bin/env poetry run python

import asyncio

from anthropic import AsyncAnthropic


async def async_tokens() -> None:
    anthropic = AsyncAnthropic()

    text = "fist message"
    tokens = await anthropic.count_tokens(text)
    print(f"'{text}' is {tokens} tokens")

    text = "second message"
    tokens = await anthropic.count_tokens(text)
    print(f"'{text}' is {tokens} tokens")


asyncio.run(async_tokens())
