from PIL import Image as PILImage

class AugustImage(PILImage):
    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.