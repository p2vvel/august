from august.metaclasses import MarkAugmentationMeta


class AugustImageMark(metaclass=MarkAugmentationMeta):
    pass


mark_augmentation = AugustImageMark.mark_augmentation
