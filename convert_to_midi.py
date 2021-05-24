import argparse
import pandas as pd
import pickle
import sys

sys.path.append('./src/')
from midi_decoder import convert_events_to_midi

from chord_processor import ChordProcessor

parser = argparse.ArgumentParser()
parser.add_argument('input_csv')
parser.add_argument('output_midi')
args = parser.parse_args()


if __name__ == '__main__':
    input_csv_file = args.input_csv
    out_midi_file = args.output_midi

    chord_processor = pickle.load(open('pickles/chord_processor.pkl', 'rb'))
    df = pd.read_csv(input_csv_file)
    events = list((df.EVENT + '_' + df.VALUE).values)

    for i, event in enumerate(events):
        if event.startswith('Position') or event.startswith('Note-Duration'):
            events[i] = events[i] + '/64'

    print(events)

    convert_events_to_midi(events, out_midi_file, chord_processor, use_structure=True)