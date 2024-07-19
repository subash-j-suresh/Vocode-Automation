import importlib
import os
import pkgutil


def import_packages(packages):
    for package_name in packages:
        package_dir = os.path.join(os.path.dirname(__file__), package_name)
        for _, module_name, _ in pkgutil.iter_modules([package_dir]):
            full_module_name = f"{package_name}.{module_name}"
            importlib.import_module(full_module_name)


def validate_first_arg(args, expected_type):
    if not args or not isinstance(args[0], expected_type):
        raise TypeError(f"First argument must be of type {expected_type.__name__}")
