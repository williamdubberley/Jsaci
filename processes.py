import config

import os
from os import path


def file_prep_for_send(type, company, name, date_time):
    # make a duplicate of an existing file
    source_file = f"{name}.csv"
    source_dir = f"{config.local_file_dir}/{company}/{type}/Source"
    target_dir = f"{config.local_file_dir}/{company}/{type}/Send"
    target_file = f"{config.prefix}_{name}_{date_time}.csv"
    if path.exists(f'{source_dir}/{source_file}'):
        # get the path to the file in the current directory
        src = path.realpath(f'{source_dir}/{source_file}');

        # rename the original file
        os.rename(f'{source_dir}/{source_file}', f'{target_dir}/{target_file}')


file_prep_for_send('dev', 'medifast', 'report', '20211018064233')
