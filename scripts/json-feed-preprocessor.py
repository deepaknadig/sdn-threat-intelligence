import json
import pprint
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
    # print('Starting {}.\n'.format(filename))
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
            item['intel-analysis'] = intel_analysis
            item['threat-level-id'] = threat_level_id
            item['intel-source'] = intel_info
            item['intel-organization'] = intel_org
            item['intel-published'] = intel_published
            item['intel-timestamp'] = intel_timestamp
            item['intel-category'] = item.pop('category')
            item['comments'] = item.pop('comment')
            item['intel-uuid'] = item.pop('uuid')
            item['exportable-to-ids'] = item.pop('to_ids')
            item['intel-value'] = item.pop('value')
            item['intel-type'] = item.pop('type')

            # Additional preprocessing
            if '|' in item['intel-type']:
                var1 = item['intel-type']
                item['intel-has-subtype'] = "true"
                item['intel-subtype-1'] = var1.split('|')[1]
                item['intel-type'] = var1.split('|')[0]
            else:
                item['intel-has-subtype'] = 'false'
                item['intel-subtype-1'] =''

            # Additional preprocessing
            if '|' in item['intel-value']:
                var2 = item['intel-value']
                item['intel-has-values'] = "true"
                item['intel-value-2'] = var2.split('|')[1]
                item['intel-value'] = var2.split('|')[0]
            else:
                item['intel-has-values'] = 'false'
                item['intel-value-2'] = ''

            if item['intel-type'] in type_dict.keys():
                item['intel-subtype-1'] = item['intel-type']
                item['intel-type'] = type_dict[item['intel-type']]

            # print(item['intel-has-subtype'] + "\t" + item['intel-type'] + "\t" + item['intel-subtype-1'])
            # print(item['intel-has-values'] + "\t" + item['intel-value'] + "\t" + item['intel-value-2'])
            # print(item['intel-type'])

            local_event_list.append(item)

        total_events = len(local_event_list)

    return local_event_list, total_events


# for file in os.listdir(directory):
for filename in os.listdir(directory):

    # print('Starting {}.'.format(filename))
    progress(progress_counter, len(os.listdir(directory)), status='Processing...')
    progress_counter += 1

    data = json_file_reader(filename)

    events = list()
    events, total_num_events = process_common_fields(data)

    for event in events:
        prefix = '{:d}'.format(i).zfill(8) + '-'
        filename1 = prefix + filename
        filename2 = os.fsencode(filename1)

        local_event_data['Event'] = [event]

        json_file_writer(local_event_data, filename2, target)

        # Clear temporary local variables
        local_event_data.clear()
        i += 1

    # Reset 'i'
    i = 1

print('\nCompleted preprocessing successfully.\n')
print('Total processed events: {:,}\n'.format(total_num_events))
