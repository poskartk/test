#!/bin/bash

#instalacja Japacza
ansible poznan -m dnf -a 'name=httpd state=latest'

#konfigurcja firewalld
ansible poznan -m firewalld -a 'service=http permanent=yes immediate=yes state=enabled'

#Zawartosc index.html
ansible poznan -m copy -a 'dest=/var/www/html/index.html content="Witaj w swiecie Ansible"'

#uruchamianie serwisu
ansible poznan -m systemd -a 'state=started enabled=yes name=httpd'
