
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

    # 3. HTML-Karten für alle Tiere erstellen
    output = ""

    for animal in animals_data:

        # Eine neue Karte beginnen
        output += '<li class="cards__item">\n'

        # Tiername als Titel
        if "name" in animal:
            output += f'  <div class="card__title">{animal["name"]}</div>\n'

        # Textbereich der Karte öffnen
        output += '  <p class="card__text">\n'

        if "characteristics" in animal:
            characteristics = animal["characteristics"]

            if "diet" in characteristics:
                output += f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

        if "locations" in animal:
            locations = animal["locations"]

            if locations:
                output += f'    <strong>Location:</strong> {locations[0]}<br/>\n'

        if "characteristics" in animal:
            characteristics = animal["characteristics"]

            if "type" in characteristics:
                output += f'    <strong>Type:</strong> {characteristics["type"]}<br/>\n'

        # Textbereich und Karte schließen
        output += "  </p>\n"
        output += "</li>\n"

    # 4. Platzhalter in der HTML-Vorlage ersetzen
    new_html = html_template.replace(
        "__REPLACE_ANIMALS_INFO__", output
    )

    # 5. Fertige HTML-Datei speichern
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(new_html)

    print("animals.html wurde erfolgreich erstellt!")


if __name__ == "__main__":
    main()
