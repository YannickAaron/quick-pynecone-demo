#!/usr/bin/python

import subprocess
import sys

import toml


def update_dependencies(dependencies: list, isDev: bool = False) -> list[str]:
    failed = []

    for dep in dependencies:
        extras = ""
        dep_version = dependencies[dep]

        # Don't try to update python
        if dep == "python":
            continue

        # If the dependency is a git dependency, don't update it
        # TODO: Add support for git dependencies
        if "git" in dep_version:
            print(f"{dep}: {dep_version} is a git dependency, skipping")
            continue

        # Check if dependency has extra dependencies
        # Example: uvicorn = { extras = ["standard"], version = "^0.17.5" }
        if "extras" in dep_version:
            extras = dep_version["extras"]

        # Update the dependency
        try:
            cmdDep = f"{dep}{extras}@latest"
            cmd = f"poetry add {cmdDep} --group dev" if isDev else f"poetry add {cmdDep}"
            print(f"Running: {cmd}")
            if isDev:
                subprocess.run(cmd, check=True, text=True, shell=True)
            else:
                subprocess.run(cmd, check=True, text=True, shell=True)
        except subprocess.CalledProcessError as e:
            # sys.exit(f"Failed for {dep}\n{e}")
            # append to failed
            failed.append(dep)

    return failed


with open("pyproject.toml", encoding="utf-8") as f:
    failed = []

    # Parse the TOML file
    pyproject = toml.load(f)

    # Get dependencies
    dependencies = pyproject["tool"]["poetry"]["dependencies"]
    dev_dependencies = pyproject["tool"]["poetry"]["group"]["dev"]["dependencies"]

    # update dependencies
    print("Updating dependencies")
    failed += update_dependencies(dependencies)

    # update dev dependencies
    print("Updating dev dependencies")
    failed += update_dependencies(dev_dependencies, True)


# Run a extra 'poetry update' for fun
try:
    cmd = "poetry update"
    print(f"Running: {cmd}")
    subprocess.run(
        cmd,
        check=True,
        text=True,
        shell=True,
    )
except subprocess.CalledProcessError as e:
    sys.exit(f"Failed to run final update\n{e}")

# Print failed
if failed:
    print("Failed to update:")
    for dep in failed:
        print(dep)
