#!/usr/bin/python3
import marshal


def extract_names_from_pyc(filename):
    try:
        with open(filename, "rb") as pyc_file:
            code_object = marshal.load(pyc_file)
            names = [n for n in code_object.co_names if not n.startswith("__")]
            return sorted(names)
    except Exception as e:
        print(f"Error: {e}")
        return []


if __name__ == "__main__":
    pyc_filename = "hidden_4.pyc"
    extracted_names = extract_names_from_pyc(pyc_filename)

    for name in extracted_names:
        print(name)
