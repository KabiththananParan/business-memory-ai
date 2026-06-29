import cognee

print("Cognee version:", cognee.__version__)
print()

functions = [
    "set_llm_provider",
    "set_llm_model",
    "set_llm_api_key",
]

for fn in functions:
    print(f"{fn}: {hasattr(cognee, fn)}")

print("\nAvailable Cognee attributes containing 'llm':")
for item in dir(cognee):
    if "llm" in item.lower():
        print("-", item)