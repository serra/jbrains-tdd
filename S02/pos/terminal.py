class Terminal:
    def _noop_price_callback(price):
        pass

    def __init__(self, price_callback=_noop_price_callback):
        self.price_callback = price_callback
        pass

    def on_barcode(self, barcode):
        self.price_callback('25.00')