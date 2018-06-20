class Terminal:
    def __init__(self, screen, catalog):
        self.screen = screen
        self.catalog = catalog

    def on_barcode(self, barcode):
        try:
            price = self.catalog[barcode]
            self.screen.display_price(price)
        except (KeyError):
            price = f'unknown product: "{barcode}"'
            self.screen.display_price(price)
