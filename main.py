#!/bin/python3

import getopt
import subprocess
import sys
from datetime import datetime
import pysftp
import config
import os
import shutil
from os import path

cnopts = pysftp.CnOpts()



def run_job(job_number):
    command = f'echo execute job number {job_number}'
    print(command)
    # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    # process.wait()
    # print(process.returncode)


def file_prep_for_send(job_type, companyname, name, date_time):
    # make a duplicate of an existing file
    source_file = f"{name}.csv"
    source_dir = f"{config.local_file_dir}/{companyname}/{job_type}/Source"
    target_dir = f"{config.local_file_dir}/{companyname}/{job_type}/Send"
    target_file = f"{config.prefix}_{name}_{date_time}.csv"
    if path.exists(f'{source_dir}/{source_file}'):
        # get the path to the file in the current directory
        src = path.realpath(f'{target_dir}/{target_file}');
        # rename the original file
        os.rename(f'{source_dir}/{source_file}', f'{target_dir}/{target_file}')
        return path.realpath(f'{target_dir}/{target_file}');


if __name__ == '__main__':
    job_type = ''
    company_name = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:c:", ["type=", "company="])
    except getopt.GetoptError:
        print('main.py -t <type> -c <company>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -t <type> -c <company>')
            sys.exit()
        elif opt in ("-t", "--type"):
            job_type = arg
        elif opt in ("-c", "--company"):
            company_name = arg
    for company in config.companies:
        now = datetime.now()  # current date and time
        date_time = now.strftime(config.date_time_format)
        if company['company'] == company_name:
            for task in company['tasks']:
                if task['type'] == job_type:
                    run_job(task['job_number'])
                    for integration in task['integrations']:
                        filename = file_prep_for_send(task['type'], company['company'], integration['name'],
                                                      date_time)
                        basedir = f"{task['base_directory']}/{integration['folder']}"
                        print(
                            f"Put {filename} in folder {basedir} ")
                        with pysftp.Connection(company['host'], username=company['username']) as sftp:
                            with sftp.cd(basedir):
                                sftp.put(filename)
