#!/bin/bash
set -eux

url='2023-4/submit/COM00029I/001/A'
username='jm3017'
zip_file='exam.zip'

./zip.sh "${zip_file}"
uoy-assessment-uploader -u "${username}" -n "${url}" -f "${zip_file}"
