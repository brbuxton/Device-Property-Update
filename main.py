#! /usr/bin/env python

"""
This is a small script to read a CSV file with fields of: serial number, device name, device tags, address, notes.
"""

import os
import csv
import meraki


def load_data(csv_file):
    """
    Load the CSV file and return a list
    :param csv_file:
    :return: return_list
    :rtype: list
    """
    print("Enter load_data")
    return_list = []
    with open(csv_file, 'r') as data:
        for line in csv.DictReader(data):
            print(line)
            return_list.append(line)
    return return_list


def update_devices(data_list: list, dashboard_object: object) -> object:
    """
    Update the device name, tags, address and notes for serials in the data_list
    :rtype: None
    """
    print("Enter update_devices")
    for line in data_list:
        dashboard_object.devices.updateDevice(
            serial=line['Serial'],
            name=line['Name'],
            address=line['Address'],
            notes=line['Notes'],
            tags=line['Tags'].split(),
            moveMapMarker=True
        )
    return


if __name__ == '__main__':
    dashboard = meraki.DashboardAPI(api_key=os.environ.get('API-KEY'))
    test_dict = {}
    update_devices(load_data("sample_bulk_network_creator.csv"), dashboard)
