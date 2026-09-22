Instructions:

- Open your desired minecraft version (from the "version" folder) .jar file with a zip program;
- Extract the "recipes" folder from inside ```data\minecraft\advancement(s)``` into the corrisponding datapack folder (where the python script is located);
- Open the terminal from inside the same folder and run the script with ```python convert_recipes.py``` (python3 if you are on Linux).

Note: make sure use the terminal to run the script from the correct directory, if (for some reason) you have a subfolder named ```recipes``` in the location you are running the script from (for example your home directory if you use VSCode with Code Runner), every JSON file present there will be overwritten!

The 1.19.4 script will change every item recipe advancement to this:
```json
{
    "parent": "minecraft:recipes/root",
    "criteria": {
        "was_crafted": {
            "conditions": {
                "items": [
                    {
                        "items": [
                            "minecraft:item_name"
                        ]
                    }
                ]
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
            "minecraft:item_name"
        ]
    }
}
```
The 1.20 to 26.2 scripts will change them to this:
```json
{
    "parent": "minecraft:recipes/root",
    "criteria": {
        "was_crafted": {
            "trigger": "minecraft:recipe_crafted",
            "conditions": {
                "recipe_id": "minecraft:item_name"
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
            "minecraft:item_name"
        ]
    }
}
```
And the 26.3 and above script will change the "was_crafted" condition to this:
```json
"conditions": {
    "recipes": [
        "minecraft:item_name"
    ]
}
```

And that's it, the datapack is ready! The 26.3 version should work with future snapshots and releases if they don't change recipe related stuff in the future, and the 1.19.4 version should also work on older versions.
You can change the ```pack_format``` version from the ```pack.mcmeta``` file if you don't want to get a warning when selecting the datapack.
