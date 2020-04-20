<p><b>Code in this github fork has been modified/updated from the origin to support Python3 and add functionality.</b></p>

<p><b>Fork is based on most recent code from origin available on 2020-04-15.</b></p>

<p><b>Below are instuctions for staging Raspbian, or other Ubuntu/Debian based distributions, for executing SkyWeather. Additionally instructions available from the fork origin for executing SkyWeather have been updated at the bottom of this file.</b></p>

---

<p><b>The below instructions are valid for Raspbian and Ubuntu. If you are not comfortable with using the terminal please revert to writing one of the available SD card image files to bootable media.</b></p>

<p><b>The below code will install all packages needed to run the SkyWeather code using Python 2.7 OR Python 3. If your wish is to use Python 3 only please omit all python-* packages and pip install* commands (i.e. Only install python3 packages and run pip3 commands).</b></p>

<pre>
sudo raspi-config

<p><b>*THIS IS A COMMENT NOT A COMMAND TO EXECUTE: USe raspi-config via terminal or the GUI to enable: camera, ssh, vnc, spi, i2c, serial port. Enabling SSH and/or VNC is optional; SSH allows remote terminal sessions, VNC allows remote GUI sessions</b></p>

sudo su

apt-get update
apt-get full-upgrade

reboot

sudo su

pip install pip --upgrade
pip3 install pip3 --upgrade
apt-get install zram-tools

reboot

sudo su

cd /home/pi

wget https://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
apt-key add mosquitto-repo.gpg.key

cd /etc/apt/sources.list.d/

wget http://repo.mosquitto.org/debian/mosquitto-buster.list

cd /home/pi

apt-get update

apt-get install vim git gfortran mariadb-server mariadb-client libatlas-base-dev libhdf5-dev libi2c-dev scons swig pigpio mosquitto mosquitto-clients

apt-get install python-mysqldb python3-pymysql python-numpy python3-numpy python-scipy python3-scipy python-matplotlib python3-matplotlib python-smbus python3-smbus python-pandas python3-pandas python-sympy python3-sympy python-nose python3-nose python-httplib2 python3-httplib2 python-dev python3-dev

apt-get install ipython python-ipython python3-ipython python-notebook python3-notebook python-opencv python3-opencv python-mpltoolkits.basemap python3-mpltoolkits.basemap python-apscheduler python3-apscheduler python-seaborn python3-seaborn python-h5py python3-h5py python-paho-mqtt python3-paho-mqtt

pip install setuptools --upgrade

pip3 install setuptools --upgrade

pip install h5py --upgrade

pip3 install h5py --upgrade 

pip install imutils

pip3 install imutils

pip3 install --ignore-installed tensorflow

systemctl enable mosquitto

mysql_secure_installation

</pre>

<p><b>*THIS IS A COMMENT NOT A COMMAND TO EXECUTE: The password you set here MUST be updated in the config.py or conflocal.py file! You can answer Y for all prompts aside from the password.*</b></p>

<pre>

git clone https://github.com/switchdoclabs/SDL_Pi_SkyWeather.git

cd /home/pi/SDL_Pi_SkyWeather/SkyWeatherSQL

mysql -u root -p < WeatherPiStructure.sql

</pre>

---

<p><b>Make a copy of config.py as conflocal.py so that all configuration changes are saved in the event of a SkyWeather code update</b></p>

<pre>

cd /home/pi/SDL_Pi_SkyWeather

cp config.py conflocal.py

</pre>

---

<p><b>Starting the SkyWeather.py program is done using three commands (first command used to ensure you're in the correct directory). In the case below Python 3 (python3) is used; you may use python instead (i.e. remove the number 3) to execute the code using Python 2.7</b></p>

<pre>

cd /home/pi/SDL_Pi_SkyWeather

sudo pigpiod

sudo python3 SkyWeather.py

</pre>

---

<p><b>Set up your rc.local for start on boot. Insert the following into /etc/rc.local before the exit 0 statement. This can be achieved using a text editor or vim from the terminal (i.e. sudo vim /etc/rc.local). Notice the below commands are essentially the same commands used to manually execute SkyWeather.</b></p>

<pre>

sudo pigpiod

cd /home/pi/SDL_Pi_SkyWeather

nohup sudo python3 SkyWeather.py

</pre>
