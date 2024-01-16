#!/bin/bash
set -eux

# first start the system at
# https://labs.azure.com

exec xfreerdp \
    CS_SYS_Networks.rdp \
    /p:'Mikrotik12!$' \
    /dynamic-resolution \
    /floatbar
