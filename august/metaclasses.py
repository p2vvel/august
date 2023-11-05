from typing import Callable


class MarkAugmentationMeta(type):
    """
    Metaclass for marking methods as augmentations of some type,
    every type of data should have its own class with this metaclass

    @mark_augmentation should be used to mark methods as augmentations

    augmentation methods are available under .methods attribute

    """

    augmentations: list[Callable]

    def __new__(cls, name, bases, attrs):
        cls = super().__new__(cls, name, bases, attrs)
        cls.augmentations = []
        return cls

    def mark_augmentation(cls, func):
        cls.augmentations.append(func)
        return func
