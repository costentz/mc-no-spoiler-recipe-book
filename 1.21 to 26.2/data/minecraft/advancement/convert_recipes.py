import os, json

# Snapshot 24w21a (1.21) renamed the "advancements" folder to "advancement"

print(f"No Spoiler Recipe Book script running from '{os.getcwd()}'")

recipes_folder = "./recipes"

if (os.path.exists(recipes_folder)):
    input(f"All json files in the 'recipes' subfolder will be converted, press any key to continue.\n")
else:
    input(f"The 'recipes' subfolder could not be found! Press any key to quit.\n")
    quit()

converted_files = 0

for root, dirs, files in os.walk(recipes_folder):
    for file in files:
        if file.endswith(".json"):
            filepath = os.path.join(root, file)
            print(filepath, end="")
            if file.startswith("root.json"):
                os.remove(filepath)
                print(" - deleted")
            else:
                with open(filepath, 'w') as f:
                    json_string = json.dumps({
                        "parent": "minecraft:recipes/root",
                        "criteria": {
                            "was_crafted": {
                                "trigger": "minecraft:recipe_crafted",
                                "conditions": {
                                    "recipe_id": "minecraft:{}".format(file[:len(file)-5])  # remove .json
                                }
                            }
                        },
                        "requirements": [
                            [
                                "was_crafted"
                            ]
                        ],
                        "rewards": {
                            "recipes": [
                                "minecraft:{}".format(file[:len(file)-5])
                            ]
                        }
                    }, indent=4)
                    f.write(json_string)
                converted_files += 1
                print(" ✓")

input(f"\nThe datapack is ready ({converted_files} files converted). Press any key to quit.\n")
