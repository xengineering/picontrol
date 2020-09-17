

# picontrol

A small Web Application to shutdown or reboot your Raspberry Pi.


## Current State

The code works but there is still documentation / automation missing.


## Usage

**Please cd into the repository to install/uninstall!**

### Installation
```bash
    sudo useradd -rUs /usr/bin/nologin picontrol
    sudo make install
```

### Activation
```bash
    sudo systemctl enable --now picontrol
```

### How to uninstall
```bash
    sudo systemctl disable --now picontrol
    sudo make uninstall
```
