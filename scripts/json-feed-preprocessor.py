import json
import os
import sys
from inteltypes import type_dict


# Progress Bar
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


# For Python 3.6 and above
# directory = os.fsencode('/home/ubuntu/intel/json')
directory = '/home/dna/intel/json'

target = os.fsencode('/home/dna/intel/json2')
if not os.path.exists(target):
    os.makedirs(target)

total_num_events = 0
local_event_data = dict()
progress_counter = 0
i = 1


def json_file_reader(source):
    # Uncomment for Python >= 3.6
    # source = os.fsdecode(source)
    if source.endswith(".json"):
        with open(os.path.join(directory, source), 'r') as read_file:
            return json.load(read_file)
    else:
        print('SKIPPING {}...\n'.format(source))


def json_file_writer(data, file, location):
    with open(os.path.join(location, file), 'w') as write_file:
        json.dump(data, write_file)
        write_file.write("\n")


def process_common_fields(data):
    total_events = 0
    local_event_list = list()

    # Get Header Data
    intel_info = data['Event']['info']
    intel_analysis = data['Event']['analysis']
    threat_level_id = data['Event']['threat_level_id']
    intel_timestamp = data['Event']['timestamp'] if ('timestamp' in data['Event']) else data['Event']['date']
    intel_org = data['Event']['Orgc']['name']

    if 'published' not in data['Event']:
        intel_published = ""
        print('No published timestamp. Skipping')
    else:
        intel_published = data['Event']['published']

    # Get Attribute Data
    if 'Attribute' not in data['Event']:
        print('Field "Attribute" not available. Skipping {}...'.format(filename))
    else:
        for item in data['Event']['Attribute']:
            item['threat-analysis'] = intel_analysis
            item['threat-level-id'] = threat_level_id
            item['threat-source'] = intel_info
            item['threat-organization'] = intel_org
            item['threat-published'] = intel_published
            item['threat-timestamp'] = intel_timestamp
            item['threat-category'] = item.pop('category')
            item['comments'] = item.pop('comment')
            item['threat-uuid'] = item.pop('uuid')
            item['exportable-to-ids'] = item.pop('to_ids')

            # Threat Intel Data
            item['threat-data'] = {}
            item['threat-data'].update({
                'has-types': 'false',
                'has-meta': 'false',
                'is-extended': 'false',
                'type1': item.pop('type'),
                'sub-type1': '',
                'value1': item.pop('value'),
                'meta1': '',
                'type2': '',
                'sub-type2': '',
                'value2': '',
                'meta2': '',

            })

            # Type(s) preprocessing
            if '|' in item['threat-data']['type1']:
                item['threat-data'].update({
                    'has-types': 'true',
                    'type2': item['threat-data']['type1'].split('|')[1],
                    'type1': item['threat-data']['type1'].split('|')[0],
                    'value2': item['threat-data']['value1'].split('|')[1],
                    'value1': item['threat-data']['value1'].split('|')[0]
                })

            if item['threat-data']['type1'] in type_dict.keys():
                item['threat-data'].update({
                    'sub-type1': item['threat-data']['type1'],
                    'type1': type_dict[item['threat-data']['type1']]
                })

            if item['threat-data']['type2'] in type_dict.keys():
                item['threat-data'].update({
                    'sub-type2': item['threat-data']['type2'],
                    'type2': type_dict[item['threat-data']['type2']]
                })

            local_event_list.append(item)

        total_events = len(local_event_list)

    return local_event_list, total_events


# for file in os.listdir(directory):
for filename in os.listdir(directory):

    progress(progress_counter, len(os.listdir(directory)), status='Processing...')
    progress_counter += 1

    data = json_file_reader(filename)

    events = list()
    events, file_events = process_common_fields(data)
    total_num_events += file_events

    local_event_data['Events'] = events

    json_file_writer(local_event_data, os.fsencode(filename), target)

    # Clear temporary local variables
    local_event_data.clear()

print('\nCompleted preprocessing successfully.\n')
print('Total processed events: {:,}\n'.format(total_num_events))
