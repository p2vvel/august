from typing import Callable


class MarkMeta(type):
    """
    Metaclass for marking methods as augmentations of some type,
    every type of data should have its own class with this metaclass

    @mark_augmentation should be used to mark methods as augmentations

    augmentation methods are available under .methods attribute

    """

    methods: list[Callable]

    def __new__(cls, name, bases, attrs):
        cls = super().__new__(cls, name, bases, attrs)
        cls.methods = []
        return cls

    def mark_augmentation(cls, func):
        cls.methods.append(func)
        return func
