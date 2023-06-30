Kenapa ansible host pada variable global "vars" menggunakan IP private? karena nama yg digunakan sebagai hostname machine pada inventory file "hosts" pada setiap group nya sama sehingga ansible me "replace" informasi detail setiap hosts nya dengan detail dari hostname tersebut pada informasi terakhir.  Ansible memperlakukan semua informasi yang berada pada inventory, vars file, dan ansible.cfg menjadi sebuah variable beserta value nya dan ansible memiliki mekanisme dimana dia akan mengumpulkan semua informasi tersebut lalu di bundle pada sebuah global variable yang bernama "vars" dengan format json. Khusus untuk kasus ini dimana kita sedang menganalisa host yang kita buat pada file inventory "hosts", ansible akan menggunakan hostname pada file tersebut sebagai sebuah variable yang menampung informasi-informasi lebih detail tentang vm yang memiliki hostname tersebut. Sumua informasi itu dibentuk dalam bentuk dictionary atau list pada format json. 

Contoh group a punya member sebuah vm dengan hostname b dan IP 192.168.1.2, lalu di line selanjutnya dibuat group c yang mempunyai member sebuah vm dengan hostname b juga namun dengan IP 192.168.1.3. Maka pada global variable "vars" rincian dari vm dengan hostname b tersebut yang dipakai adalah rincian yang ada pada member group c yang berarti yang memiliki IP 192.168.1.3 bukan 192.168.1.2. Hal ini terjadi karena member dari group a dan c memiliki hostname yg sama, yaitu: b. Sehingga setelah ansible memasukan detail dari properties b (yang salah satu nya adalah IP) ke global variable "vars", ansible akan melanjutkan mencatat semua properties yg ada pada group c beserta membernya. Masalahnya member dari group c memiliki hostname yang sama dengan group c, yaitu b sehingga ansible mengasumsikan bahwa ini merupakan vm yang sama dengan yang sebelumnya sudah di write pada global variable "vars" hanya saja dengan detail informasi yang berbeda(dalam hal ini IP nya yg berbeda) dan ansible pada akhirnya tidak menuliskan informasi baru ke global variable "vars" melainkan menulis ulang ke dalam properties vm b yang tadi sudah dibuat sebelumnya. Itulah mengapa yang terbaca oleh ansible IP untuk vm b adalah IP vm b yang berada pada group c (192.168.1.3) bukan group a (192.168.1.2).

# ansible-initial
Scripts configuration of rancher2 server in GCE centos instances using ansible version 2.10.

### Note

> If you need ansible script for build the vpc, subnetworks, firewall rules, and simple cluster of gce instances, it can be found:
  - [networking](https://github.com/rvn40/ansible-gce-network-simple)
  - [gce-simple-cluster](https://github.com/rvn40/ansible-gce-simple-cluster)
> If you are using ansible scripts from [gce-simple-cluster](https://github.com/rvn40/ansible-gce-simple-cluster) repository to deploy your cluster instances, it's strongly recommended to use your pre-built gce image in order to help you use these scritps easier but you had to installed, at least, python3, pip3, dnf, gcloud-sdk in your pre-built image as well. Then, you can change 'image' key in the 'vars' file from [gce-simple-cluster](https://github.com/rvn40/ansible-gce-simple-cluster) repository with your own pre-built image. However, you don't have to run 'preconfiguration_rancher.yml' playbook.

# Requirements
When you use this ansible scripts, make sure you have installed all of these packages in advance on your ansible host:

- Python3
- Python3-pip
- Git

It's also necessary to install all of these packages requirements using pip:

- ansible==2.10
- requests>=2.18.4
- google-auth>=1.3.0
- docker>=1.8.0 
- boto
- boto3

Update hosts file with list of vm inventories that you want to configure with these scripts and prepare all of neccesary files like serviceaccount, ssh keys, bash, ssl, etc. Recommended to place those files under directory called "files".

# How to use

```
ansible-playbook configuration_rancher.yml
```
