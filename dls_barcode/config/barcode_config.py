import sys

from dls_barcode.util import Color, Config, DirectoryConfigItem, ColorConfigItem, IntConfigItem, BoolConfigItem

IS_BUNDLED = getattr(sys, 'frozen', False)


class BarcodeConfig(Config):
    def __init__(self, file):
        Config.__init__(self, file)

        add = self.add

        if IS_BUNDLED:
            default_store = "./store/"
        else:
            default_store = "../store/"

        self.color_ok = add(ColorConfigItem, "Read Color", Color.Green())
        self.color_unreadable = add(ColorConfigItem, "Not Read Color", Color.Red())
        self.color_empty = add(ColorConfigItem, "Empty Color", Color.Grey())

        self.camera_number = add(IntConfigItem, "Camera Number", default=0)
        self.camera_width = add(IntConfigItem, "Camera Width", default=1920)
        self.camera_height = add(IntConfigItem, "Camera Height", default=1080)

        self.scan_beep = add(BoolConfigItem, "Beep While Scanning", default=True)
        self.scan_clipboard = add(BoolConfigItem, "Results to Clipboard", default=True)

        self.image_puck = add(BoolConfigItem, "Draw Puck", default=True)
        self.image_pins = add(BoolConfigItem, "Draw Slot Highlights", default=True)
        self.image_crop = add(BoolConfigItem, "Crop to Puck", default=True)

        self.store_directory = add(DirectoryConfigItem, "Store Directory", default=default_store)
        self.store_capacity = add(IntConfigItem, "Results History Size", default=50)

        self.console_barcodes = add(BoolConfigItem, "Print Barcode List", default=False)
        self.console_frame = add(BoolConfigItem, "Print Frame Summary", default=False)
        self.slot_images = add(BoolConfigItem, "Save Debug Images", default=False)
        self.slot_image_directory = add(DirectoryConfigItem, "Debug Directory", default="../debug-output/")

        self.initialize_from_file()

    def col_ok(self):
        return self.color_ok.value()

    def col_bad(self):
        return self.color_unreadable.value()

    def col_empty(self):
        return self.color_empty.value()
