# 🐶 Mini DOGE Exchange (Django)

A simple mini crypto exchange built with Django that allows users to simulate buying and selling Dogecoin (DOGE) using real-time price data.

---

## 🚀 Features

- 📈 Real-time DOGE price (via Nobitex API)
- 💰 Fake wallet system (IRT & DOGE)
- 🟢 Buy DOGE
- 🔴 Sell DOGE
- 🌐 Simple frontend using HTML, CSS, JS (fetch API)

---

## 🧱 Tech Stack

- Backend: Django
- Frontend: HTML, CSS, JavaScript
- API: Nobitex Orderbook API
- Database: SQLite

---

## 📂 Project Structure

```
core/
 ├── core/
 ├── exchange/
 │    ├── models.py
 │    ├── views.py
 │    ├── urls.py
 │    └── services.py
 ├── templates/
 │    └── index.html
 └── manage.py
```

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/mini-doge-exchange.git
cd mini-doge-exchange/core

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## 🌍 Usage

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🧠 How It Works

- Fetches DOGE price from Nobitex orderbook API
- Calculates price using best bid/ask average
- Stores wallet data in SQLite
- Uses simple API endpoints:
  - `/api/price/`
  - `/api/wallet/`
  - `/api/buy/`
  - `/api/sell/`

---

## 🔥 Future Improvements

- Multi-coin support (BTC, ETH, etc)
- User authentication
- Transaction history
- Charts (price visualization)
- Real trading integration

---

## 📌 Note

This project is for educational purposes only and does not perform real trading.

---

## 👨‍💻 Author

Built by a Django learner 🚀
