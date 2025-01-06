#!/bin/bash

#tworzenie partycji vdb1
ansible gdansk -m parted -a 'device=/dev/vdb number=1 state=present part_end=2GiB'

#tworzenie FS xfs
ansible gdansk -m filesystem -a 'fstype=xfs dev=/dev/vdb1'

#tworzenie miejsca montowania
ansible gdansk -m file -a 'path=/backup owner=root group=root mode=0644 state=directory'

#montowanie partycji
ansible gdansk -m mount -a 'path=/backup src=/dev/vdb1 fstype=xfs state=present'
