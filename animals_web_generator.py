import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    animals_data = load_data("animals_data.json")

    for animal in animals_data:

        if "name" in animal:
            print(f"Name: {animal['name']}")

        if "characteristics" in animal:
            characteristics = animal["characteristics"]

            if "diet" in characteristics:
                print(f"Diet: {characteristics['diet']}")

        if "locations" in animal:
            locations = animal["locations"]

            if locations:
                print(f"Location: {locations[0]}")

        if "characteristics" in animal:
            characteristics = animal["characteristics"]

            if "type" in characteristics:
                print(f"Type: {characteristics['type']}")

        print()


if __name__ == "__main__":
    main()