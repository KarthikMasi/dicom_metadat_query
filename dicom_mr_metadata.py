#!/usr/bin/env python

import pydicom
import os
import json
import argparse

def get_out_path(args):
    if(args.outfile):
        return args.outfile
    else:
        return os.path.dirname(args.dicom_path)+'/metadata.json'

def parse_args():
    parser = argparse.ArgumentParser(description='Crontabs manager')
    parser.add_argument("--dicom",dest='dicom_path',default=None,required=True, \
                        help='Path to DICOM file to fetch metadata from')
    parser.add_argument("--out",dest='outfile',default=None,required=False,   #defaults to same dir and filename as dicom \
                        help='Path to save JSON object')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    ds = pydicom.dcmread(args.dicom_path).to_json_dict()
    repetion_time = ds["52009229"]['Value'][0]['00189112']['Value'][0]['00180080']['Value'][0]
    manufacturer = ds["00080070"]['Value'][0]
    model = ds["00081090"]['Value'][0]
    mag_field_strength = ds["00180087"]['Value'][0]
    echo_time = ds["52009230"]['Value'][0]['2005140F']['Value'][0]['00180081']['Value'][0]
    flip_angle = ds["52009230"]['Value'][0]['2005140F']['Value'][0]['00181314']['Value'][0]
    number_of_slices = ds["20011018"]['Value'][0]
    spacing_btw_slices = ds["52009230"]['Value'][0]['2005140F']['Value'][0]['00180088']['Value'][0]
    export_dict = {
        "RepetitionTime": repetion_time,
        "Manufacturer": manufacturer,
        "ManufacturerModelName": model,
        "MagneticFieldStrength": mag_field_strength,
        "EchoTime": echo_time,
        "FlipAngle": flip_angle,
        "NumberOfSlices": number_of_slices,
        "SpacingBetweenSlices": spacing_btw_slices
    }
    out_file_name = get_out_path(args)
    with open(out_file_name, 'w') as outfile:
        json.dump(export_dict,outfile)
