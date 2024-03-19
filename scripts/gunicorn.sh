#!/usr/bin/bash

sudo rm -f /etc/systemd/system/gunicorn.socket
sudo rm -f /etc/systemd/system/gunicorn.service

sudo cp /home/ubuntu/dekhoghar/gunicorn/gunicorn.socket /etc/systemd/system/gunicorn.socket
sudo cp /home/ubuntu/dekhoghar/gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service

sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service
