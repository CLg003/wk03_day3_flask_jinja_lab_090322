from app import app
from flask import render_template
from models.order_list import games

@app.route('/orders')
def index():
    return render_template('index.html', title="Orders", games=games)

@app.route('/orders/<index>')
def order(index):
    return render_template('order.html', title="Order Details", game=games[int(index)])
