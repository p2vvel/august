import random
from typing import Callable, Protocol


class _HasAugmentationsProtocol(Protocol):
    @property
    def _augmentations(self) -> list[Callable]:
        ...


class ExecuteAugmentationMixin(_HasAugmentationsProtocol):
    def augment(self) -> None:
        """Execute methods marked with @mark_augmentation decorator (specifically for each data augmentation)"""
        augmentations = self._augmentations[:]
        random.shuffle(augmentations)
        for aug in augmentations:
            aug(self)
