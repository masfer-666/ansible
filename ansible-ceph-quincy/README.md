## Deploy Ceph Storage Cluster with Ansible on Ubuntu 20
Adjust the IP's in playbook.yml with your env    
```
  vars:
    - mon1_ip: 192.168.200.41
    - mon2_ip: 192.168.200.42
    - mon3_ip: 192.168.200.43
    - osd1_ip: 192.168.200.44
    - osd2_ip: 192.168.200.45
    - osd3_ip: 192.168.200.46
```
Run playbook, change user [ubuntu] to your server user
```
ansible-playbook -i hosts playbook.yml -u ubuntu
```
Access ceph dashboard
```
url : https://192.168.200.41:8443
user: admin
pass: P@ssw0rd
```
