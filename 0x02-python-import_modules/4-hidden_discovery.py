#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    file_path = "hidden_4pyc"
    spec = importlib.util.spec_from_file_location("hidden_4p", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    #Extract the names that do not start with "__"
    names = sorted(
                names = sorted(
                    name
                    for name in dir(module)
                    if not name.startswith("__")
                )
                #Print the name
                
                for name in names:
                    print(name)
