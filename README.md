

# picontrol

A small Web Application to shutdown or reboot your Raspberry Pi.


## Usage

### Preparation

Make sure to open your firewall on port 8080. **If** you use UFW you can do it like this:
```bash
    sudo ufw allow 8080
```

Install python3, Flask and waitress. python3 installation depends on your system.
With pip you can install Flask and waitress very easily:
```bash
    sudo pip3 install Flask waitress
```

### How to install, start and enable
```bash
    git clone https://github.com/xengineering/picontrol.git
    cd picontrol
    sudo useradd -rUs /usr/bin/nologin picontrol
    sudo make install
    sudo systemctl enable --now picontrol
```

### How to remove
```bash
    sudo systemctl disable --now picontrol
    sudo make uninstall  # just works from picontrol directory (the git repository you cloned)
    sudo userdel picontrol
```

### Access the Web Page

You just have to visit http://pi_IP_or_hostname:8080 in the browser of your choice.
