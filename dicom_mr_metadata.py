#!/usr/bin/env python

import pydicom
import os
import json


def parse_args():
    parser = argparse.ArgumentParser(description='Crontabs manager')
    parser.add_argument("--dicom",dest='dicom_path',default=None,required=True, \
                        help='Path to DICOM file to fetch metadata from')
    parser.add_argument("--out",dest='outfile',default=None,required=False, \  #defaults to same dir and filename as dicom
                        help='Path to save JSON object')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    ds = pydicom.dcmread(args.dicom_path).to_json()
    repetion_time = ds["52009229"]['Value'][0]['00189112']['Value'][0]['00180080']['Value'][0]
    manufacturer = ds["00080070"]['Value'][0]



