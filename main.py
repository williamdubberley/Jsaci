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

class Workfile:
    def __init__(self, source, target):
        self.source = source
        self.target = target

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
    print(f'{source_dir}/{source_file}')
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
                        with pysftp.Connection(company['host'], username=task['username'],
                               private_key=task['private_key']) as sftp:
                            for integration in task['integrations']:
                                filename = file_prep_for_send(task['type'], company['company'], integration['name'],
                                                            date_time)
                                work_file=Workfile(filename, f"{task['base_directory']}/{integration['folder']}")
                                work_files.append(work_file)
                            for work_file in work_files:
                                file=open(work_file.source)
                                reader=csv.reader(file)
                                lines=len(list(reader))
                                if lines>1:
                                     print(f"Put {work_file.source} in folder {work_file.target} ")
                                     sftp.chdir('..')
                                     sftp.chdir(f'{work_file.target}')
                                     print(sftp.pwd)
                                     sftp.put(work_file.source)

    for f in work_files:
        print(f"archiving {f.source}")
        zipObj.write(f.source)
        print(f"removing {f.source}")
        os.remove(f.source)
    zipObj.close()

