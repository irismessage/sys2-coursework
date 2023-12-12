#!/bin/bash
set -eux
xfreerdp \
    CS_SYS_Networks.rdp \
    /p:'Mikrotik12!$' \
    /dynamic-resolution \
    /floatbar
