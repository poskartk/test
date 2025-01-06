date
ansible all -m shell -a 'date'; date
cd /home/student/
ls
vim output.txt
ls -ltr
ls -ltrh
pwd
exit
pwd
ps -ef |grep java
history
ls -ltrh
./skrypt.sh 
ls -ltrh
cat inventory2.cfg 
ip addr show
cat ansible.cfg 
cat inventory.cfg 
virsh 
man virsh
su -
pwd
top
free -h
c /opt
ls
c /opt
ls
c /opt
ls
cd /opt
ls
cd 
ls
exit
w
exit
ssh gdansk
ssh wroclaw 
ssh poznan
ansible all -m ping -a data=”Hurra” 
ansible poznan -m user -a 'name=konik comment="tescik" uid=2003'
ssh poznan
ssh gdansk
ansible gdansk -m user -a 'name=konik comment="tescik" uid=2003'
ssh gdansk 
ls
w
less output.txt 
ls -ltrh
cat output.txt 
w
ssh base
w
pwd
ls
vim inventory3.cfg
cat inventory3.cfg 
cat inventory.cfg 
ansible all -i inventory3.cfg -m command -a id
ansible-doc copy
ansible all -i inventory3.cfg -m shell -a 'cat /etc/motd'
ansible all -i inventory3.cfg -m shell -a 'cat /etc/passwd'
ansible all -i inventory3.cfg -m shell -a 'cat /etc/passwd' > passwd_all
ls -ltrh
less passwd_all 
ansible all -i inventory3.cfg -m shell -a 'top' 
cd /tmp
ls
mkdir xxx
ls -ltrh
anscd 
cd 
ls
ansible all -i inventory3.cfg -m fetch -a 'dest=/tmp/xxx src=/etc/sudoers'
cd /tmp/xxx
ls
cd poznan/
ls
cd etc
ls
ansible gdansk -m systemd -a 'name=crond state=restarted'
pwd
cd 
ansible gdansk -m systemd -a 'name=crond state=restarted'
ansible gdansk -m -vv systemd -a 'name=crond state=restarted'
ansible gdansk -vv -m  systemd -a 'name=crond state=restarted'
ansible gdansk  -m  service -a 'name=chronyd state=restarted'
curl -s http://poznan
ls
vim skrypt.sh 
./skrypt.sh 
curl -s http://gdansk
curl -s http://poznan
vim skrypt.sh 
ansible all -m ping
ssh poznan
w
ssh wroclaw
w
ansible all -i inventory.cfg -m ping
ansible all -i inventory.cfg -m shell -a id
ansible servers -m shell -a 'cat /etc/motd'
ansible all -m ping -o
cat inventory.cfg 
cat ansible.cfg 
ansible all -m ping
ansible poznan -m setup
ansible-doc file
ansible-doc archive
ansible all -m file -a 'path=/backup state=directory mode=0755'
ansible all -m dnf -a 'name=rsyslog state=present'
ansible all -m systemd -a 'name=rsyslog state=started enabled=yes'
ansible all -m file -a 'path=/backup state=directory mode=0755'
ansible all -m archive -a 'path=/etc/ dest=/backup/etc.zip format=zip'
ansible all -m fetch -a 'dest=/backup src=/backup/etc.zip'
ansible all -m fetch -a 'dest=/backup/etc/zip src=/backup'
ansible all -m fetch -a 'dest=/backup src=/backup/etc.zip'
ansible all -m file -a 'path=/backup state=directory mode=0777'
ansible all -m archive -a 'path=/etc/ dest=/backup/etc.zip format=zip'
ansible all -m fetch -a 'dest=/backup src=/backup/etc.zip'
cd /
ls
mkdir backup
su -
ansible all -m fetch -a 'dest=/backup src=/backup/etc.zip'
cd /backup
ls
cd 
ansible all -m fetch -a 'dest=/backup src=/backup/etc.zip'
cd /backup
ls
cd gdansk/
ls
cd backup/
ls
ls -ltrh
cd 
ls
find /tmp -iname "etc.zip"
find /backup -iname "etc.zip"
echo "autocmd FileType yaml setlocal ai ts=2 sw=2 et" > .vimrc
vim users.yaml
ls -ltrh
vim users.yaml 
ansible-playbook --syntax-check users.yaml 
vi users.yaml 
ansible-playbook --syntax-check users.yaml 
vi users.yaml 
ansible-playbook --syntax-check users.yaml 
vi users.yaml 

ansible-playbook -C users.yaml 
cat users.yaml 
vim users.yaml 
ansible-playbook -C users.yaml 
vim users.yaml 
ansible-playbook -C users.yaml 
vim users.yaml 

cat users.yaml 
ansible-playbook -C -e uzytkownik=jan users.yaml 
ansible-playbook -C -e 'uzytkownik=jan group=it' users.yaml 
vim users.yaml 
vim zmienne.yaml
cat zmienne.yaml 
cat users.yaml 
ansible-playbook -C users.yaml 
vim users.yaml 
ls -ltrh
mv zmienne.yaml zmienne.yml
cat zmienne.yml 
cat users.yaml 
ansible-playbook -C users.yaml 
vim palybook.yml
ls -ltrh
ansible-playbook -C palybook.yml 
pwd
ls -ltrh
vim palybook.yml 
mv palybook.yml playbook.yml
ansible-playbook -C playbook.yml 
vim inventory.cfg 
ansible-playbook -C playbook.yml 
vim inventory.cfg 
ls -ltrh |grep inve
less inventory3.cfg
less inventory2.cfg
cat playbook.yml 
cat inventory.cfg
vim inventory.cfg
cat inventory.cfg
ansible-playbook -C playbook.yml 
vim inventory.cfg 
ansible-playbook -C playbook.yml 
cat playbook.yml 
cat inventory
cat inventory.cfg 
vim inventory.cfg 
cat inventory.cfg 
vim www.yml
ansible-playbook -C www.yml 
vim www.yml 
ansible-playbook -C www.yml 
vim www.yml 
ansible-playbook -C www.yml 
vim www.yml 
ansible-playbook -C www.yml 
cat www.yml 
vim www.yml 
ansible-playbook -C www.yml 
vim www.yml 
ansible-playbook -C www.yml 
cat www.yml 
cat inventory.cfg 
ansible-playbook --syntax-check ./www.yml
ansible-playbook ./www.yml
curl http://poznan
curl http://gdynia
curl http://gdansk
curl http://poznan
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
vim www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
cat www-multi.yml
ansible-playbook --syntax-check ./www-multi.yml
ansible-playbook ./www-multi.yml
vim paczki.yml
ansible-playbook --syntax-check ./paczki.yml 
ansible-playbook ./paczki.yml 
vim paczki.yml
ansible-playbook ./paczki.yml 
cat paczki.yml 
vim paczki.yml 
ansible-playbook -C paczki.yml 
cat paczki.yml 
vim paczki.yml 
cat paczki.yml 
ansible-playbook -C paczki.yml 
vi paczki.yml 
vim zmienne.yml
ansible-playbook -C paczki.yml 
cat paczki.yml 
cat zmienne.yml 
vim debug.yml
ansible-playbook -C debug.yml 
cat debug.yml 
vim debug1.yml
ansible-playbook -C debug1.yml 
absible poznan - setup
ansible poznan -m setup
ansible poznan -m setup > info_poznan
less info_poznan 
ansible-playbook -C debug.yml 
cat debug.yml 
less debug.yml 
vi debug.yml 
ansible-playbook -s debug.yml 
ansible-playbook -C debug.yml 
cat debug.yml 
ansible-playbook -C debug1.yml 
cat debug1.yml 
vim instalacja.yml
ansible-playbook -C instalacja.yml 
cat instalacja.yml 
ansible all -m setup ansible_memfree_mb
ansible all -m setup |grep ansible_memfree_mb
vim instalacja.yml 
cat instalacja.ymll 
cat instalacja.yml 
ansible-playbook -C instalacja.yml 
vim instalacja.yml 
ansible-playbook -C instalacja.yml 
cat instalacja.yml 
vim instalacja.yml 
cat instalacja.yml 
ansible-playbook -C instalacja.yml 
vim serwer_www.yml
ansible-playbook -C serwer_www.yml 
vim serwer_www.yml
ansible-playbook -C serwer_www.yml 
vim serwer_www.yml
cat serwer_www.yml 
vi users.yml
ansible-playbook -C users.yml
ls -ltrh
vim users.yml
ansible-playbook -C users.yml
vim users.yml
ansible-playbook -C users.yml
vim users.yml
ansible-playbook -C users.yml
vim users.yml
ansible-playbook -C users.yml
cat users.y
cat users.yml 
vim users2.ymp
ansible-playbook -C users2.yml
mv users2.ymp users2.yml
ansible-playbook -C users2.yml
vim users2.yml
ansible-playbook -C users2.yml
vim users2.yml
ansible-playbook -C users2.yml
vim users2.yml
ansible-playbook -C users2.yml
vim users2.yml
ansible-playbook -C users2.yml
vim users2.yml
ansible-playbook -C users2.yml
cat users2.yml 
ansible-playbook ./users2.yml
ansible-playbook ./users.yml
vim users2.yml
vim users3.yml
vim lista_pracownikow.yml
vim users3.yml
ansible-playbook -C users3.yml 
cat users3.yml 
cat lista_pracownikow.yml 
cat users3.yml 
ansible-playbook -C users3.yml 
vim users3.yml 
ansible-playbook -C users3.yml 
vim users3.yml 
ansible-playbook -C users3.yml 
vim users3.yml 
vim uprawnienia.yml
ansible-playbook -C uprawnienia.yml 
ansible-playbook -C users3.yml 
ansible-playbook -C uprawnienia.yml 
cat uprawnienia.yml 
vim lab6.yml
vim users3.yml 
ansible-playbook -C users3.yml 
vim users3.yml 
ansible-playbook -C users3.yml 
cat users3.yml 
ansible-playbook -C users3.yml 
ansible-playbook ./users3.yml 
ls -ltrh
rm lab6.yml 
ls -ltrh
w
exit
l s-ltrh
ls -ltrh
cay playbook.yml 
cta playbook.yml 
cat playbook.yml 
ls -ltrh
cat www.yml 
ls -ltrh
cat lista_pracownikow.yml 
vim lista_userow
vim lista_
vim lista_userow 
cat lista_
cat lista_userow 
vim lista_userow 
cat lista_userow 
ansible-doc group
ansible-doc find
vim serwerki.yml
ansible-doc find
ansible-doc at
ssh poznan
su -
ssh poznan
ssh gdansk 
ssh wroclaw 
tutaj start dniowki mojej od dzisiaj
ansible all -m ping
vim gdansk.yml
ansible-playbook -C gdansk.yml 
vim gdansk.yml 
ansible-playbook -C gdansk.yml 
vim gdansk.yml 
ansible-playbook -C gdansk.yml 
vim gdansk.yml 
vim play1.yml
ansible-playbook -C play1.yml 
vim play1.yml
ansible-playbook -C play1.yml 
vim play1.yml
ansible-playbook -C play1.yml 
vim play1.yml
ansible-playbook -C play1.yml 
vim play1.yml
ansible-playbook -C play1.yml 
vim play1.yml
ansible-playbook -C play1.yml 
ansible-playbook ./play1.yml 
ansible-playbook -C play1.yml 
vim play1.yml
ansible-playbook -C play1.yml 

vim play1.yml
ansible-playbook -C play1.yml 
vim play1.yml
ansible-doc group
vim play1.yml
ansible-playbook -C play1.yml 
vim play1.yml
ls -ltrh
vim gdansk.yml 
ansible-playbook -C gdansk.yml 
vim gdansk.yml 
ansible-playbook -C gdansk.yml 
vim gdansk.yml 
ansible-playbook -C gdansk.yml 
vim gdansk.yml 
ansible-playbook -C gdansk.yml 
vim gdansk.yml 
ansible-playbook -C gdansk.yml 
vim gdansk.yml 
ansible-playbook -C gdansk.yml 
vat gdansk.yml 
cat gdansk.yml 
vim gdansk.yml 
ansible-playbook -C gdansk.yml 
vim gdansk.yml 
ansible-playbook -C gdansk.yml 
cat gdansk.yml 
ansible all -m find -a 'path=/var/log/' -size >=1MB
ansible all -m find -a "path='/var/log/' size>=1m"
ansible poaznan -m find -a "path='/var/log/' size>=1m"
ansible all -m find -a "path='/var/log/' size>=1m"
ansible all -m find -a "path='/var/log/' size=1m"
ansible all -m find -a "path='/var/log/' size=>1m"
ansible all -m find -a "path='/var/log/' size=1m"
ls -ltrh
cat play1.yml 
ansbile pozna -m shell -a 'head /etc/chrony.conf'
ansbile poznan -m shell -a 'head /etc/chrony.conf'
ans[Cbile poznan -m shell -a 'head /etc/chrony.conf'
ansible poznan -m shell -a 'head /etc/chrony.conf'
vim zegarek.yml
ansible-playbook -C zegarek.yml 
ansible-playbook zegarek.yml 
cat zegarek.yml 
vim zegarek.yml 
ansible-playbook zegarek.yml 
cat zegarek.yml 
vim inst.yml
yum history
sudo dnf serach screen
vim when.yml
ansible-playbook -C when.yml 
vim when.yml
ansible-playbook -C when.yml 
vim when.yml
ansible-playbook -C when.yml 
vim when.yml
ansible-playbook -C when.yml 
vim when.yml
ansible-playbook -C when.yml 
vim when.yml
ansible-playbook -C when.yml 
vim when.yml
cat inventory.cfg 
vim inventory.cfg 
ansible-playbook -C when.yml 
cat when.yml 
vim petle.yml
ansible-playbook -C petle.yml 
ansible-playbook  petle.yml 
ssh krzysiek@gdansk 
cat petle.yml 
vim handlers.yml
ansible servers -m yum -a \
ansible servers -m yum -a 'name=policycoreutils-python'
ansible servers -m yum -a \'name=policycoreutils-python'
ansible servers -m yum -a 'name=policycoreutils-python'
vim statusyzadan.yml
ansible-playbook -C statusyzadan.yml 
vim statusyzadan.yml
ansible-playbook -C statusyzadan.yml 
vim statusyzadan.yml
ansible-playbook -C statusyzadan.yml 
vim statusyzadan.yml
ansible-playbook statusyzadan.yml 
vim statusyzadan.yml
ansible-playbook -C statusyzadan.yml 
vim statusyzadan.yml
vim handlers.yml
sudo dnf search policycore
ansible servers -m yum -a 'name=policycoreutils-python-utils'
vim handlers.yml
ansible-playbook -C handlers.yml 
vim handlers.yml
ansible-playbook -C handlers.yml 
vim handlers.yml
ansible-playbook -C handlers.yml 
cat handlers.yml 
ansible-playbook  handlers.yml 
ssh root@gdansk
ansible-playbook  handlers.yml 
vim statusyzadan.yml 
ansible-playbook -C statusyzadan.yml 
cat statusyzadan.yml 
ansible-playbook statusyzadan.yml 
cat statusyzadan.yml 
vim statusyzadan.yml 
ansible-playbook statusyzadan.yml 
vim statusyzadan.yml 
ansible-playbook statusyzadan.yml 
vim statusyzadan.yml 
ansible-playbook statusyzadan.yml 
cat statusyzadan.yml 
vim statusyzadan.yml 
ansible-playbook statusyzadan.yml 
vim statusyzadan.yml 
ansible-playbook statusyzadan.yml 
vim statusyzadan.yml 
ansible-playbook statusyzadan.yml 
cat statusyzadan.yml 
vim statusyzadan.yml 
ansible-playbook statusyzadan.yml 
vim statusyzadan.yml 
cat statusyzadan.yml 
ansible-playbook statusyzadan.yml 
vim statusyzadan.yml 
cat statusyzadan.yml 
ansible-playbook statusyzadan.yml 
vim block.yml
ls -ltrh
rm block.yml 
ls -ltrh
ls -ltrh |grep chro
ls -ltrh
vim block.yml
ansible-playbook -C block.yml 
vim block.yml
ansible-playbook  block.yml 
vim block.yml
ansible-playbook  block.yml 
vim block.yml
ansible-playbook  block.yml 
cat block.yml 
vim ftp-vars.yml
ansible-playbook -C ftp-vars.yml 
ansible-playbook  ftp-vars.yml 
ftp poznan
ssh poznan
ansible - v
ansoble -version
ansible -version
ansible-playbook --version
ansible --version
ftp poznan
vsftp poznan
ansible-playbook  ftp-vars.yml 
cp ftp-vars.yml ftp-vars-wroclaw.yml
ls -ltrh
vim ftp-vars-wroclaw.yml 
vim vars.yml
ansible-playbook -C ftp-vars-wroclaw.yml 
vim ftp-vars-wroclaw.yml 
ansible-playbook -C ftp-vars-wroclaw.yml 
vim ftp-vars-wroclaw.yml 
ansible-playbook -C ftp-vars-wroclaw.yml 
vim ftp-vars-wroclaw.yml 
ansible-playbook -C ftp-vars-wroclaw.yml 
vim ftp-vars-wroclaw.yml 
ansible-playbook -C ftp-vars-wroclaw.yml 
ls -ltrh
vim ftp-vars.yml
ansible-playbook ftp-vars-wroclaw.yml 
ftp wroclaw
man ftp
sudo yum install ftp
su -
man ftp
ftp poznan
ftp wroclaw
cp ftp-vars-wroclaw.yml ftp-vars-gdansk.yml
vim ftp-vars-gdansk.yml
ansible-playbook ftp-vars-gdansk.yml
vim ftp-vars-gdansk.yml
ansible-playbook ftp-vars-gdansk.yml
ftp gdansk
ls -ltrh
cat ftp-vars.yml
cat ftp-vars-wroclaw.yml
cat ftp-vars-gdansk.yml
cat vars.yml
ls -ltrh
ansible-playbook ftp-vars.yml ; ansible-playbook ftp-vars-wroclaw.yml; ansible-playbook ftp-vars-gdansk.yml
ftp poznan
ftp gdansk
ftp wroclaw 
vim bloczek.yml
ansible-playbook -C bloczek.yml 
vim bloczek.yml
ansible-playbook -C bloczek.yml 
vim bloczek.yml
ansible-playbook -C bloczek.yml 
vim bloczek.yml
ansible-playbook -C bloczek.yml 
vim bloczek.yml
ansible-playbook -C bloczek.yml 
vim bloczek.yml
ansible-playbook -C bloczek.yml 
vim bloczek.yml
ansible-playbook -C bloczek.yml 
cat bloczek.yml 
ansible-playbook  bloczek.yml 
vim koniec.yml
ansible-playbook -C koniec.yml 
vim koniec.yml
ansible-playbook -C koniec.yml 
cp koniec.yml koniec_bckp_yml
ls -ltrh
vim koniec.yml 
cp users3.yml koniec.yml
vim koniec.yml 
ansible-playbook -C koniec
ansible-playbook -C koniec.ymp
ansible-playbook -C koniec.yml
ansible-playbook  koniec.yml
cat koniec.yml 
exit
ls -ltrh
cat bloczek.yml 
vim gruposy.yml
cat gruposy.yml 
cat lista_pracownikow.yml 
vim gruposy.yml 
cat lista_pracownikow.yml 
vi gruposy.yml 
cat gruposy.yml 
vim grou
vim gruposy.yml 
cat gruposy.yml 
ssh poznan
exit
ls -ltrh
ansible poznan -m setup
ansible poznan -m setup > info_poznan
less info_poznan 
vim zadanie1.yml
ansible-playbook -C zadanie1.yml 
vim zadanie1.yml 
ansible-playbook -C zadanie1.yml 
vim zadanie1.yml
ansible-playbook -C zadanie1.yml 
vim zadanie1.yml
ivm zadanie2.yml
vim zadanie2.yml
ansible-playbook -C zadanie2.yml 
vim zadanie2.yml 
ansible-playbook -C zadanie2.yml 
vim zadanie2.yml 
ansible-playbook -C zadanie2.yml 
vim zadanie2.yml 
ansible-playbook -C zadanie2.yml 
vim zadanie2.yml 
ansible-playbook -C zadanie2.yml 
vim zadanie2.yml 
ansible-playbook -C zadanie2.yml 
vim zadanie2.yml 
ansible-playbook -C zadanie2.yml 
vim zadanie2.yml 
ansible-playbook -C zadanie2.yml 
vim zadanie2.yml 
ansible-playbook -C zadanie2.yml 
vim zadanie2.yml 
ansible-playbook -C zadanie2.yml 
vim zadanie2.yml 
ansible-playbook -C zadanie2.yml 
vim zadanie2.yml 
ansible-playbook -C zadanie2.yml 
vim zadanie2.yml 
ansible-playbook -C zadanie2.yml 
vim zadanie2.yml 
ansible-playbook -C zadanie2.yml 
vim zadanie2.yml 
cat zadanie2.yml 
ansible-playbook zadanie2.yml 
vim zadanie2a.yml
ansible-playbook -C zadanie2a.yml 
vim zadanie2a.yml 
ansible-playbook zadanie2a.yml 
cat zadanie2a.yml 
ls -ltrh
touch test
top > test
ls -ltrh
: > test
ls -ltrh
rm test
ls -ltrh
cd group_vars/
ls
ls -ltrh
cd ..
cd host_vars/
ls
touch poznan
rm poznan 
mkdir poznan
cd poznan/
vim 1.yml
cd ..
cd group_vars/
ls
cd www
ls
ls -ltrh
rm bazy www
ls
mkdir www
cd www
ls
vim 1.yml
cd ..
ls -ltrh
cat group_vars/www/1.yml 
cat host_vars/poznan/1.yml 
cat inventory.cfg
vim inventory.cfg 
cat inventory.cfg
tree
ansible servers -m debug -a "var=zmienna"
vim inventory.cfg 
ansible servers -m debug -a "var=zmienna"
vim inventory.cfg 
ansible servers -m debug -a "var=zmienna"
vim inventory.cfg 
ansible servers -m debug -a "var=zmienna"
cat inventory.cfg 
ansible gdansk -m setup
ls -ltrh
cat zadanie1.yml 
cp zadanie1.yml fakty.yml
vim fakty.yml 
ansible-playbook -C fakty.yml 
vim fakty.yml 
cat inventory.cfg 
vim inventory
vim inventory.cfg 
ansible-playbook -C fakty.yml 
vim fakty.yml 
ansible-playbook -C fakty.yml 
ansible-playbook ./facts.yml
ansible-playbook  fakty.yml 
cat fakty.yml 
vim gdansk-facts.yml
ansible-playbook -C gdansk-facts.yml 
vim gdansk-facts.yml
ansible-playbook -C gdansk-facts.yml 
vim gdansk-facts.yml
ansible-playbook -C gdansk-facts.yml 
ansible-playbook  gdansk-facts.yml 
ansible gdansk -m shell -a "rpm -q screen"
ansible gdansk -m shell -a "rpm -q samba"
ansible localhost -m debug -a 'var=hostvars["localhost"]'
ansible localhost -m debug -a 'var=hostvars["localhost"]["groups"]["all"]'
ansible localhost -m debug -a 'var=hostvars["localhost"]["groups"]["prod"]'
ansible localhost -m debug -a 'var=hostvars["localhost"]["groups"]["www"]'
ansible localhost -m debug -a 'var=hostvars["localhost"]["groups"]["db"]'
ansible localhost -m debug -a 'var=hostvars["localhost"]["groups"]["servers"]'
ansible localhost -m debug -a 'var=hostvars["localhost"]["groups"]["all"]'
ansible localhost -m debug -a 'var=hostvars["localhost"]["groups"]'
ansible poznan -m setup
less dane 
vim wyciagnijdane.yml
ansible-playbook -C wyciagnijdane.yml 
vim wyciagnijdane.yml
ansible-playbook -C wyciagnijdane.yml 
cat wyciagnijdane.yml 
ansible-playbook  wyciagnijdane.yml 
ls -ltrh
cp wyciagnijdane.yml dzien4
cd dzien4/
ls
ls -ltrh
cd ..
ls -ltrh
su -
vim password.yml 
ansible-vault create password.yml
rm password.yml
ansible-vault create password.yml
cat password.yml
ansible-vault view ./password.yml
ansible-vault edit password.yml
vim jakis.yml
ansible-playbook -ask-vault-pass jakis.yml 
ansible-playbook -C jakis.yml 
ansible-playbook -ask-vault-pass jakis.yml 
ansible-playbook --ask-vault-pass jakis.yml 
su -
rm password.yml 
ansible-vault create password.yml
cat password.yml 
ansible-vault view ./password.yml
vim jakis.yml 
ansible-playbook --ask-vault-pass jakis.yml 
ansible-playbook  jakis.yml --ask-vault-pass
cat jakis.yml 
ssh secretuser@poznan
ssh poznan
ls
ls -ltrh
mkdir roles
cd roles/
ansible-galaxy init users
ls
ls -ltrh
tree
tree users
ls
vim users/tasks/main.yml 
cat users/tasks/main.yml 
vim users/vars/main.yml 
cat users/vars/main.yml 
echo "plik nr 1" > users/files/plik1
echo "plik nr 2" > users/files/plik2
cd ..
pwd
vim rola_users.yml
cat rola_users.yml 
ansible-playbook -C rola_users.yml 
ls -ltrh
vim vars.ym
vim issue.j2
ls -ltrh
vim ostatni.yml
ansible-playbook -C ostatni.yml 
cat vars.ym
mv vars.ym vars.yml
cat vars.yml
ansible-playbook -C ostatni.yml 
ansible-playbook  ostatni.yml 
cat ostatni.yml 
exit
ssh gdansk
ssh wroclaw 
exit
ssh wroclaw 
ansible-playbook  ostatni.yml 
ansible-playbook ostatni.yml 
cat vars.yml
cat issue.j2
vim vars.yml
ansible-playbook ostatni.yml 
vim vars.yml
cat vars.yml
vim ostatni.yml 
cat ostatni.yml 
vim virtualhost.j2
vim virtualhost-template.yml
ansible-playbook -C virtualhost-template.yml 
vim virtualhost-template.yml
ansible-playbook -C virtualhost-template.yml 
cat  virtualhost-template.yml 
ansible-playbook  virtualhost-template.yml 
ls -ltrh
ansible-playbook ostatni.yml 
cat ostatni.yml
exit
ls -ltrh
cat ostatni.yml 
exit
w
ls -ltrh
pwd
ls -ld /home
cd home
ls
cd h/home
ls
pwd
cd ..
ls
cd student/
ls
ls -ltrh
rm '=1MB'
ls -ltrh
df -h
free -h
ansible-doc setup
ansible-doc register
man register
ls -ltrh
cat ftp-vars.yml
ls -ltrh |grep chron
less chrony.sh
vim zadanie1.yml 
ansible-playbook -C zadanie1.yml 
vim zadanie1.yml 
ansible-playbook -C zadanie1.yml 
ansible-playbook zadanie1.yml 
cat zadanie1.yml
vim zadanie1.yml
cat zadanie1.yml 
mkdir backup
ls -ltrh
cat zadanie1.yml 
vim zadanie2.yml 
cd /tmp
ls
mkdir plik1
mkdir plik2
cd 
ls -ltrh
ls -ltrh |grep yml
cat inventory.cfg
vim inventory.cfg
pwd
mkdir group_vars
mkdir host_vars
ls -ltrh
cd tmp
ls
cd backup/
ls
cd poznan/
ls
cd 
ls
pwd
cd 
ls -ltrh
cd group_vars/
touch bazy
touch www
ls
cd ..
pwd
mkdir dzien4
cp *yml /home/student/dzien4/
cp *cfg /home/student/dzien4/
cp *sh /home/student/dzien4/
cd  dzien4/
ls
ls -ltrh
ls |wc
cd ..
pwd
vim inventory.cfg 
cat inventory.cfg 
pwd
vim inventory.cfg 
ansible poznan -m setup > dane
pwd
 ansible gdansk -m setup > dane
less dane 
ssh gdansk
less dane 
ssh poznan:22
ssh poznan 22
ssh student@poznan:22
exit
