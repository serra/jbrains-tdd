class Terminal:
    def __init__(self, screen, catalog):
        self.screen = screen
        self.catalog = catalog

    def on_barcode(self, barcode):
        if barcode not in self.catalog:
            message = f'unknown product: "{barcode}"'
            self.screen.display_message(message)
        else:
            self.screen.display_price(self.catalog[barcode])
