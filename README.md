# Stripe + Flask Demo (Beginner Friendly)

A minimal Flask project that demonstrates how to create a Stripe Checkout session and redirect a customer to pay. This repo is designed for beginners learning Flask and Stripe Checkout integration.

## What this project contains
- app.py — Flask application and where Stripe Checkout is created.
- templates/ — Jinja2 templates: index, success and cancel pages.
- myvenv/ — optional virtual environment (if present).

## What you'll learn
- Basic Flask routes and templates.
- How to create a Stripe Checkout session on the server.
- How to redirect users to Stripe Checkout and handle success/cancel flows.
- Important Stripe concepts: amounts are in the smallest currency unit (cents for USD) and test mode usage.

## Prerequisites
- Python 3.8+
- A Stripe account (for test API keys)
- Optional: virtualenv

## Setup (Windows)
1. Open a terminal in this project folder.
2. Activate the virtualenv (if present):
   - Command Prompt:
     ```
     myvenv\Scripts\activate
     ```
   - PowerShell:
     ```
     .\myvenv\Scripts\Activate.ps1
     ```
   If you don't have a venv, create one:
   ```
   python -m venv myvenv
   myvenv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   If `requirements.txt` doesn't exist:
   ```
   pip install flask stripe
   ```

## Configure Stripe (do NOT hard-code secret keys)
1. Get your Stripe test secret key (starts with `sk_test_...`) from the Stripe Dashboard.
2. Set an environment variable:
   - Command Prompt:
     ```
     set STRIPE_SECRET_KEY=sk_test_...
     ```
   - PowerShell:
     ```
     $env:STRIPE_SECRET_KEY="sk_test_..."
     ```
3. (Recommended) Update app.py to read the key from the environment instead of hard-coding it. See the example below.

## Run the app
1. Ensure the venv is active and STRIPE_SECRET_KEY is set.
2. Run:
   ```
   python app.py
   ```
3. Open http://127.0.0.1:5000/ in your browser and try the demo.

## Testing Stripe Checkout
- Use Stripe test cards. Example: card number `4242 4242 4242 4242`, any future expiry, any CVC, and any ZIP.
- The demo runs in test mode when using test keys — no real payments are processed.

-Example
Email: any
Card Number: 4242 4242 4242 4242
Expiry: 12 / 34
CVC: 123
Name on Card: Nicky Test
Billing ZIP: 12345






