import os

import music21 as m21


def read_ensemble_xml_file(path: str):
    with open(path) as file:
        xml_parser = m21.musicxml.xmlToM21.MusicXMLImporter()
        score = xml_parser.scoreFromFile(file)

        for part in score.parts:
            unprocessed_instrument = part.getInstrument()
            try:
                instrument: m21.instrument.Instrument = m21.instrument.fromString(
                    unprocessed_instrument.bestName()
                )
                if instrument.transposition != unprocessed_instrument.transposition:
                    print(
                        f">>> WARNING: mismatched transposition for "
                        f"{unprocessed_instrument.bestName()} "
                        f"=> {instrument.bestName()}: "
                        f"{unprocessed_instrument.transposition} "
                        f"!= {instrument.transposition}"
                    )
                    print(
                        f">>> setting {unprocessed_instrument.transposition} "
                        f"transposition for {instrument.bestName()}"
                    )
                    instrument.transposition = unprocessed_instrument.transposition
            except m21.instrument.InstrumentException:
                print(
                    f">>> WARNING: failed to process "
                    f"{unprocessed_instrument.bestName()} "
                    f"into designated Instrument class"
                )
                instrument = unprocessed_instrument

            print(instrument)


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
