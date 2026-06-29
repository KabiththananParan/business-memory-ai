from cognee.infrastructure.llm.structured_output_framework \
    .litellm_instructor.llm.get_llm_client import LLMProvider

print("Available LLM Providers:\n")

for provider in LLMProvider:
    print(f"- {provider.name}: {provider.value}")