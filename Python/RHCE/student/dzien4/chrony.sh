#!/bin/bash

#konfig serrwera base
ansible localhost -m lineinfile -a 'path=/etc/chrony.conf line="local stratum 10"'
ansible localhost -m lineinfile -a 'path=/etc/chrony.conf line="allow 10.10.0.0/16"'

#retstart uslugi na base
ansible localhost -m systemd -a 'name=chronyd state=restarted'

#zmiana pliku conf w /etc/chrony.conf
ansible all -m lineinfile -a 'path=/etc/chrony.conf regexp="pool2.centos.pool.ntp.org iburst" line="server base iburst"'

#restart uslugi
ansible all -m systemd -a 'name=chronyd state=restarted'

