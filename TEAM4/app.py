from flask import Flask, render_template, request
import mlab
from models.subscribers import Subscribers
mlab.connect()

app = Flask(__name__)

@app.route('/thankyou')
def thankyou():
  return render_template('thankyou.html')

@app.route('/checkout')
def checkout():
  return render_template('checkout.html')

@app.route('/cart')
def cart():
  return render_template('cart.html')


@app.route('/shop')
def shop():
  mens = [
    {
      'name': 'ANGEL SKULL - CAP/ CAMOUFLAGE WASHED',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/21-copy.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'ANGEL SKULL - CAP/ RED WASHED',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/1-1-1.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'ANGEL OVERPRINTED/ L/S - CHARM PINK',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/2-copy.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'ANGEL OVERPRINTED/ L/S - SILVER BLUE',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/5-copy.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'CONTRAST POCKET TEES - CHARCOAL RED',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/1-2-.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'CONTRAST POCKET TEES - WHITE BLUE',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/Bản-sao-1-1.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'L/S FLANNEL SHIRT - BLUE',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/2.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'BURNING CROSS 2.0 - PRINTED HOODIE',
      'image': 'https://bobui.vn/wp-content/uploads/2018/12/3-0-700.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'BC ARTWORK - HOODIE/ WHITE',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/1-1.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'SLIM FIT JEANS - INDIGO',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/7.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'BOBUI SG - SHORT',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/3-1-.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'BOBUI SG - SWEATPANT',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/4-1.jpg',
      'price': '500.000đ',
    },
  ]
  return render_template('shop.html', mens=mens)

@app.route('/home', methods=['POST', 'GET'])
def home():
  sample = [
    {
      'name': 'ANGEL SKULL - CAP/ CAMOUFLAGE WASHED',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/21-copy.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'ANGEL SKULL - CAP/ RED WASHED',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/1-1-1.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'ANGEL OVERPRINTED/ L/S - CHARM PINK',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/2-copy.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'ANGEL OVERPRINTED/ L/S - SILVER BLUE',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/5-copy.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'CONTRAST POCKET TEES - CHARCOAL RED',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/1-2-.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'CONTRAST POCKET TEES - WHITE BLUE',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/Bản-sao-1-1.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'L/S FLANNEL SHIRT - BLUE',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/2.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'BURNING CROSS 2.0 - PRINTED HOODIE',
      'image': 'https://bobui.vn/wp-content/uploads/2018/12/3-0-700.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'BC ARTWORK - HOODIE/ WHITE',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/1-1.jpg',
      'price': '500.000đ',
    }
  ]
  # 1.Gui form
  if request.method == "GET":
    return render_template("index.html", sample=sample)
  elif request.method == "POST":
    # 2. Nhan form => luu
    form = request.form
    email = form['email']
    new_subscriber = Subscribers(email = email)
    new_subscriber.save()
    return "Gotcha"
  

@app.route('/shop-single')
def shopsimple():
  return render_template('shop-single.html')

@app.route('/mens')
def mens():
  mens = [
    {
      'name': 'ANGEL SKULL - CAP/ CAMOUFLAGE WASHED',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/21-copy.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'ANGEL SKULL - CAP/ RED WASHED',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/1-1-1.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'ANGEL OVERPRINTED/ L/S - CHARM PINK',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/2-copy.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'ANGEL OVERPRINTED/ L/S - SILVER BLUE',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/5-copy.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'CONTRAST POCKET TEES - CHARCOAL RED',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/1-2-.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'CONTRAST POCKET TEES - WHITE BLUE',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/Bản-sao-1-1.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'L/S FLANNEL SHIRT - BLUE',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/2.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'BURNING CROSS 2.0 - PRINTED HOODIE',
      'image': 'https://bobui.vn/wp-content/uploads/2018/12/3-0-700.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'BC ARTWORK - HOODIE/ WHITE',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/1-1.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'SLIM FIT JEANS - INDIGO',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/7.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'BOBUI SG - SHORT',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/3-1-.jpg',
      'price': '500.000đ',
    },
    {
      'name': 'BOBUI SG - SWEATPANT',
      'image': 'https://bobui.vn/wp-content/uploads/2019/01/4-1.jpg',
      'price': '500.000đ',
    },
  ]
  return render_template('mens.html', mens=mens)

if __name__ == '__main__':
  app.run(debug=True)