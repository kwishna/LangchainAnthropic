# curl --request POST \
#      --url https://api.anthropic.com/v1/complete \
#      --header "anthropic-version: 2023-06-01" \
#      --header "content-type: application/json" \
#      --header "x-api-key: $ANTHROPIC_API_KEY" \
#      --data '
# {
#   "model": "claude-1",
#   "prompt": "\n\nHuman: Hello, world!\n\nAssistant:",
#   "max_tokens_to_sample": 256,
#   "stream": true
# }
#
# -----------------------------------------------------------------------------
#
# event: completion
# data: {"completion": " Hello", "stop_reason": null, "model": "claude-1.3"}
#
# event: completion
# data: {"completion": "!", "stop_reason": null, "model": "claude-1.3"}
#
# event: ping
# data: {}
#
# event: completion
# data: {"completion": " My", "stop_reason": null, "model": "claude-1.3"}
#
# event: completion
# data: {"completion": " name", "stop_reason": null, "model": "claude-1.3"}
#
# event: completion
# data: {"completion": " is", "stop_reason": null, "model": "claude-1.3"}
#
# event: completion
# data: {"completion": " Claude", "stop_reason": null, "model": "claude-1.3"}
#
# event: completion
# data: {"completion": ".", "stop_reason": null, "model": "claude-1.3"}
#
# event: completion
# data: {"completion": "", "stop_reason": "stop_sequence", "model": "claude-1.3"}
#
# event: completion
# data: {"completion": " Hello", "stop_reason": null, "model": "claude-1.3"}
#
# event: error
# data: {"error": {"type": "overloaded_error", "message": "Overloaded"}}