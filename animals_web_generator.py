
import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    # 1. Tierdaten aus der JSON-Datei laden
    animals_data = load_data("animals_data.json")

    # 2. HTML-Vorlage einlesen
    with open("animals_template.html", "r", encoding="utf-8") as file:
        html_template = file.read()

    # 3. Einen String mit allen Tierinformationen erstellen
    output = ""

    for animal in animals_data:

        if "name" in animal:
            output += f"Name: {animal['name']}\n"

        if "characteristics" in animal:
            characteristics = animal["characteristics"]

            if "diet" in characteristics:
                output += f"Diet: {characteristics['diet']}\n"

        if "locations" in animal:
            locations = animal["locations"]

            if locations:
                output += f"Location: {locations[0]}\n"

        if "characteristics" in animal:
            characteristics = animal["characteristics"]

            if "type" in characteristics:
                output += f"Type: {characteristics['type']}\n"

        output += "\n"

    # 4. Platzhalter durch unsere Tierinformationen ersetzen
    new_html = html_template.replace(
        "__REPLACE_ANIMALS_INFO__", output
    )

    # 5. Neue HTML-Datei erstellen
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(new_html)

    print("animals.html wurde erfolgreich erstellt!")


if __name__ == "__main__":
    main()
