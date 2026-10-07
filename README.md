# Aqua Medicines

A Flask-based aquaculture supplies store.

## Features

- User registration and login
- Product catalogue and details
- Shopping cart and quantity updates
- Checkout and order history
- Admin dashboard
- Admin product creation, editing, and hiding
- SQLite database by default

## Install on Ubuntu

```bash
sudo apt update
sudo apt install -y python3-venv python3-pip

cd /opt/aqua-medicines
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
nano .env# aqua-medicines
