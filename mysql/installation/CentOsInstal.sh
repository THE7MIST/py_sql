sudo dnf install mariadb-server -y
sudo systemctl start mariadb
sudo systemctl enable mariadb
mysql -u root
#mysql -u root -p
# password is "root"

# sudo apt update
# sudo apt install mysql-server -y
# sudo systemctl start mysql