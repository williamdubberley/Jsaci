#!/bin/python3

import getopt
import subprocess
import sys
from datetime import datetime
import pysftp
import config
import os
from zipfile import ZipFile
from os import path
from os.path import basename


def run_job(job_number):
    command = f'/home/tomcat/rj/public/bin/etl {job_number} -account 1000'
    print(command)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(process.returncode)


def file_prep_for_send(job_type, companyname, name, date_time):
    # make a duplicate of an existing file
    source_file = f"{name}.csv"
    source_dir = f"{config.local_file_dir}/{companyname}/{job_type}/Source"
    files = os.listdir(source_dir)
    # for f in files:
    #     print(f)
    #     source_file = f
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
    now = datetime.now()  # current date and time
    date_time = now.strftime(config.date_time_format)
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
    zipObj = ZipFile(f"{config.local_file_dir}/{company_name}/{job_type}/Processed/{company_name}.{date_time}.zip", 'w')
    work_files = []
    for company in config.companies:

        if company['company'] == company_name:
            for task in company['tasks']:
                if task['type'] == job_type:
                    run_job(task['job_number'])
                    for integration in task['integrations']:
                        filename = file_prep_for_send(task['type'], company['company'], integration['name'],
                                                      date_time)
                        work_files.append(filename)
                        basedir = f"{task['base_directory']}/{integration['folder']}"

                        print(
                            f"Put {filename} in folder {basedir} ")
                        with pysftp.Connection(company['host'], username=company['username'],
                                               private_key=company['private_key']) as sftp:
                            with sftp.cd(basedir):
                                sftp.put(filename)
    for f in work_files:
        print(f"archiving {f}")
        zipObj.write(f)
        print(f"removing {f}")
        os.remove(f)
    zipObj.close()
