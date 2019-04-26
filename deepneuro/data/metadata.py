""" Alpha code for generating 
"""

import numpy as np

from collections import defaultdict


def calculate_class_distributions(data_collection, data_group_label='ground_truth'):

    data_group = data_collection.get_data_groups([data_group_label])[0]
    data_group.metadata['distribution_indexes'] = defaultdict(list)
    data_group.metadata['classes'] = set()

    if data_collection.source == 'hdf5':
        print(data_group.data)
        for idx, value in enumerate(data_group.data):
            value = np.argmax(value)
            data_group.metadata['distribution_indexes'][idx] += [idx]
            data_group.metadata['classes'].add(value)
    else:
        for idx, (key, value) in enumerate(data_group.data.items()):
            value = value[0]
            data_group.metadata['distribution_indexes'][value] += [idx]
            data_group.metadata['classes'].add(value)

    return