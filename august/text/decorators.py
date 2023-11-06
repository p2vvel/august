from august.metaclasses import MarkAugmentationMeta


class AugustTextMark(metaclass=MarkAugmentationMeta):
    pass


mark_augmentation = AugustTextMark.mark_augmentation
