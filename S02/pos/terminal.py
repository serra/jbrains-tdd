class Terminal:
    def __init__(self, price_callback, catalog):
        self.price_callback = price_callback
        self.catalog = catalog

    def on_barcode(self, barcode):
        try:
            price = self.catalog[barcode]
            self.price_callback(price)
        except (KeyError):
            pass

    def add_item(self, barcode, price):
        self.catalog[barcode] = price