sudo apt-get install patch
wget http://webupd8.googlecode.com/files/vmware802fixlinux320.tar.gz
tar -xvzf vmware802fixlinux320.tar.gz
mv ~/vmware802fixlinux320/vmware3.2.0.patch ~
sudo ~/vmware802fixlinux320/patch-modules_3.2.0.sh
rm vmware802fixlinux320.tar.gz
rm -r vmware802fixlinux320
rm ~/vmware3.2.0.patch
