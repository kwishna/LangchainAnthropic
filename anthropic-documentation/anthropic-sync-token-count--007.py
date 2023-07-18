#!/usr/bin/env poetry run python

from anthropic import Anthropic


def sync_tokens() -> None:
    client = Anthropic()

    text = "hello world!"

    tokens = client.count_tokens(text)
    print(f"'{text}' is {tokens} tokens")


sync_tokens()
