#!/usr/bin/env python3

import yaml
import importlib
from datetime import datetime


with open("modules.yml") as file:
    try:
        modules = yaml.safe_load(file)
        print(modules)
    except yaml.YAMLError as error:
        print(error)

for module in modules["task"]:
    print("Loading package {} from module {}".format(module["package"], module["module"]))
    load_module = importlib.import_module(module["module"], package=module["package"])
    print(load_module)

    module_name = module["module"]
    modules = {
        module_name: {
            "object": getattr(load_module, module["package"])
        }
    }
    object = modules[module_name]["object"]
    object = object()
    object.version()
