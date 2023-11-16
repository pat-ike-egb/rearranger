import os

import music21 as m21


def read_ensemble_xml_file(path: str):
    with open(path) as file:
        xml_parser = m21.musicxml.xmlToM21.MusicXMLImporter()
        score = xml_parser.scoreFromFile(file)

        for part in score.parts:
            print(part.getInstrument().bestName())


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)

    # a file pointing to the specification of the instrument
    # players in the desired ensemble
    target_ensemble_path = os.path.join(
        base_dir, "resources", "ensembles", "test.musicxml"
    )

    read_ensemble_xml_file(target_ensemble_path)

    # a MusicXML file pointing to the input score, (instruments and parts, arrangement)
    input_score_path = ""

    # a MusicXML file representing the original music mapped/arranged
    # to the target ensemble specification
    output_score_path = ""
