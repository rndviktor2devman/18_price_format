import argparse


def format_price(price):
    price = float(price)

    if price % 1 != 0:
        return '{:,.2f}'.format(price).replace(',', ' ')
    else:
        return '{:,.0f}'.format(price).replace(',', ' ')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("price", type=float, help="Price for format")
    args = parser.parse_args()
    print(format_price(args.price))

