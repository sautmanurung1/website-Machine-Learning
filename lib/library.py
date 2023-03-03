import re
from collections import Counter
import csv
import requests
import os

def reader(filename):
    with open(filename) as f:
        log = f.read()
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips_list = re.findall(regexp, log)
        return ips_list

def count(ips_list):
    return Counter(ips_list)

def write_csv(counter):
    with open('../dataset/output-IP-logs.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IP', 'Frequency']
        writer.writerow(header)
        for item in counter:
            writer.writerow( (item, counter[item]) )

def nslookup(filename):
    with open(filename, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        token = '31a497f53d0e6a'
        next(csv_reader, None)
        for row in csv_reader:
            if len(row) > 0:
                ip_address = row[0]
                url = f"https://ipinfo.io/{ip_address}/json?token={token}"
                response = requests.get(url)
                data = response.json()
                print(data)

if __name__ == '__main__':
    write_csv(count(reader('../dataset/access.log')))
    nslookup('../dataset/output-IP-logs.csv')