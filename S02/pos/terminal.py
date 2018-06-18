class Terminal:
    def _noop_price_callback(price):
        pass

    def __init__(self, price_callback=_noop_price_callback):
        self.price_callback = price_callback
        self.catalog = dict()

    def on_barcode(self, barcode):
        price = self.catalog[barcode]
        self.price_callback(price)

    def add_item(self, barcode, price):
        self.catalog[barcode] = price