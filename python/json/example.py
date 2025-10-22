#!/usr/bin/env python3
import json
import random
import secrets
import signal
import sys

# Seed pseudorandom number generator with high-entropy value.
random.seed(secrets.randbits(64))

signal.signal(signal.SIGTERM, lambda sig, frame: exit(0))

NULL_SEQ = "\\N"

random_item_names = [
    "keyboard",
    "mouse",
    "monitor",
    "printer",
    "desk",
    "chair",
    "lamp",
    "notebook",
    "pen",
    "headphones",
]


def parse_json(text: str) -> dict | list | None:
    if text == NULL_SEQ:
        return None
    return json.loads(text)


def dump_json(json_data: dict | list | None) -> str:
    if json_data is None:
        return NULL_SEQ
    return json.dumps(json_data)


def transform_json(json_data: dict | list) -> dict | list | None:
    """
    This is a main transformation function that modifies the input JSON data.
    You can implement any transformation logic here as per your requirements.
    """
    if json_data is None:
        # Is Null (meaning None) keep it as is
        return None
    result = []
    for item in json_data:
        if "id" in item:
            # Add 1000 to the id
            item["id"] = item["id"] + 1000
        if "item" in item:
            # Replace item name with a random choice
            item["item"] = random.choice(random_item_names)
        if "price" in item:
            # Replace price with a random float between 10.0 and 500.0
            item["price"] = round(random.uniform(10.0, 500.0), 2)
        result.append(item)

    return json_data

def write_output(raw_data: str):
    sys.stdout.write(raw_data)
    sys.stdout.write("\n")
    sys.stdout.flush()

#  [{ "id": 1, "item": "keyboard", "price": 49.99 }, { "id": 2, "item": "mouse", "price": 19.99 }]
def transform(message: str):
    # remove trailing newline
    message = message.rstrip("\n")
    json_data = parse_json(message)
    new_value = transform_json(json_data)
    new_raw_data = dump_json(new_value)
    write_output(new_raw_data)

def main():
    for data in sys.stdin:
        # Writing the result to stdout with new line and flushing the buffer
        transform(data)

if __name__ == "__main__":
    main()
