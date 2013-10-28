#!/bin/bash
 chown -R mysql .
 chgrp -R mysql .
 scripts/mysql_install_db --user=mysql --srcdir=/home/gfif/Code/dte
 chown -R root .
 chown -R mysql data
# Next command is optional
 cp support-files/my-medium.cnf /etc/my.cnf
 bin/mysqld_safe --user=mysql &
# Next command is optional
 cp support-files/mysql.server /etc/init.d/mysql.serve
