import random
from typing import Callable, Protocol


class _HasAugmentationsProtocol(Protocol):
    @property
    def _augmentations(self) -> list[Callable]:
        """A property that should return a list of callable functions representing data augmentation methods."""
        ...


class ExecuteAugmentationMixin(_HasAugmentationsProtocol):
    def augment(self) -> None:
        """Execute methods marked with @mark_augmentation decorator (specifically for each data augmentation).

        This method applies data augmentation methods to the current object in a randomized order.
        The augmentation methods are determined by the list returned by _augmentations property.
        """
        augmentations = self._augmentations[:]
        random.shuffle(augmentations)
        for aug in augmentations:
            aug(self)
