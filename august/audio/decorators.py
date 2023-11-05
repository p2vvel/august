from august.metaclasses import MarkAugmentationMeta


class AugustAudioMark(metaclass=MarkAugmentationMeta):
    pass


mark_augmentation = AugustAudioMark.mark_augmentation
