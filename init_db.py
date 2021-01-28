import argparse
import json
import os
import glob
from datetime import datetime
from api.incident_service import IncidentService

def clean_timestamp(obj, timestamp_keys):
    for key in timestamp_keys:
            if obj.get(key):
                timestamp = obj[key]
                obj[key] = datetime.fromisoformat(timestamp)

def load_data(fpath):
    with open(fpath) as f:
        data = json.load(f, parse_int=int, parse_float=float)
    #
    if data.get('description'):
        clean_timestamp(data['description'], ["event_closed", "event_opened", "first_unit_arrived", "first_unit_dispatched", "first_unit_enroute", "loi_search_complete"])
    if len(data.get('apparatus', [])) > 0:
        for apparatus in data['apparatus']:
            unit_status = apparatus.get('unit_status', {})
            for k, v in unit_status.items():
                if isinstance(v, dict) and v.get('timestamp'):
                    unit_status[k]['timestamp'] = datetime.fromisoformat(v['timestamp'])
    service = IncidentService()
    service.add_incident(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Adds data to the MongoDB.")
    parser.add_argument(
        '-f',
        '--file',
        help='Input json to be inserted into the MongoDB.',
        type=str,
        default=None
        )
    parser.add_argument(
        '-d',
        '--directory',
        help='Input directory containing the files to be inserted into the MongoDB.',
        type=str,
        default='./tests/data'
        )
    args = parser.parse_args()
    if args.file and os.path.isfile(args.file):
        load_data(fpath)
    elif os.path.isdir(args.directory):
        files = glob.glob(f"{args.directory}/*.json")
        for file in files:
            load_data(file)

