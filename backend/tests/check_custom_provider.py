import inspect
import cognee

print("\n=== Cognee Version ===")
print(cognee.__version__)

print("\n=== cognee.config ===")
try:
    print(cognee.config)
    print("\ndir(cognee.config):")
    for item in dir(cognee.config):
        if not item.startswith("_"):
            print(item)
except Exception as e:
    print("Error:", e)


print("\n=== Searching for config classes ===")

modules_to_check = [
    "cognee.config",
    "cognee.infrastructure.llm.config",
    "cognee.infrastructure.llm.LLMGateway",
    "cognee.modules.settings.save_llm_config",
]

for module_name in modules_to_check:
    print(f"\n--- {module_name} ---")

    try:
        module = __import__(module_name, fromlist=["*"])

        for name in dir(module):
            if name.startswith("_"):
                continue

            obj = getattr(module, name)

            if inspect.isclass(obj):
                print(f"\nCLASS: {name}")

                try:
                    attrs = [
                        attr
                        for attr in dir(obj)
                        if any(
                            keyword in attr.lower()
                            for keyword in [
                                "provider",
                                "model",
                                "api",
                                "key",
                                "custom",
                                "base_url",
                            ]
                        )
                    ]

                    if attrs:
                        print("Relevant fields:", attrs)

                    if hasattr(obj, "__annotations__"):
                        print("Annotations:")
                        print(obj.__annotations__)

                except Exception as e:
                    print("Class inspection failed:", e)

    except Exception as e:
        print("Import failed:", e)