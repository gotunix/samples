#!/usr/bin/env python3

#import yaml
#import importlib
#import json

from yaml import safe_load as yaml_safe_load
from yaml import YAMLError as yaml_YAMLError
from json import dumps as json_dumps
from envsubst import envsubst
from os import environ

def load_build_stage(stage):
    for task in stage["tasks"]:
        for argument in task["arguments"]:
            arg_val = envsubst(task["arguments"][argument])
            task["arguments"][argument] = arg_val


with open("pipeline.yml") as file:
    try:
        pipeline = yaml_safe_load(file)

    except yaml_YAMLError as error:
        print("error: {}".format(error))
        exit(1)


variables = pipeline["workflow"]["variables"]
for name in variables:
    val = pipeline["workflow"]["variables"][name]
    environ[name.upper()] = val


for stage in pipeline["workflow"]["stages"]:
    if stage["stage"] == "Build":
        load_build_stage(stage)
    if stage["stage"] == "Deployment":
        load_build_stage(stage)

print(json_dumps(pipeline, indent=4))
