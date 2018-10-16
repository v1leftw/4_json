import json
import os
import argparse


def load_data(filepath):
    try:
        os.path.isfile(filepath)
        with open(filepath, "r", encoding="utf8") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print("File not found")
        return None
    except ValueError:
        print("That is not json-file")
        return None


def pretty_print_json(data_from_json):
    return json.dumps(data_from_json,
                      sort_keys=True,
                      indent=4,
                      ensure_ascii=False)


def get_args():
    parser = argparse.ArgumentParser(description="Enter the path directory:")
    parser.add_argument("-file", required=True, help="Path to file")
    return parser.parse_args()


if __name__ == '__main__':
    path_to_file = get_args().file
    json_data = load_data(path_to_file)
    if json_data is not None:
        print(pretty_print_json(json_data))
