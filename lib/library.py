import re
from collections import Counter
import csv
import requests

def reader(filename):
    with open(filename) as f:
        log = f.read()
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips_list = re.findall(regexp, log)
        return ips_list

def count(ips_list):
    return Counter(ips_list)

def write_csv(counter):
    with open('output-IP.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IP', 'Frequency']
        writer.writerow(header)
        for item in counter:
            writer.writerow( (item, counter[item]) )

def nslookup(filename):
    with oepn(filename, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader, None)
        if len(row) > 0:
            ip_address = row[0]
            url = f"https://ipinfo.io/{ip_address}/json?token=31a497f53d0e6a"
            response = requests.get(url)
            data = response.json()
            print(data)

