from pathlib import Path

import click

from august.images.config import AugustImageConfig
from august.images.images import AugustImage
from august.utils.dirs import get_directory, images_in_directory


# cli = click.group("august")
@click.group()
def cli() -> None:
    pass


@click.command()
@click.option("--source", "-s", help="Source directory with images", required=True)
@click.option("--destination", "-d", help="Destination directory for augmented images", required=True)
@click.option("--n", "-n", help="Number of augmented images", required=True, type=int)
@click.option("--mirror_p", help="Mirror probability", default=0.5, type=float)
@click.option("--flip_p", help="Flip probability", default=0.5, type=float)
@click.option("--color_p", help="Color change probability", default=0.5, type=float)
@click.option("--temperature_p", help="Color temperature probability", default=0.5, type=float)
@click.option(
    "--min_temperature_ratio", help="Minimal color temperature change ratio", default=-50, type=int
)
@click.option(
    "--max_temperature_ratio", help="Maximum color temperature change ratio", default=50, type=int
)
@click.option("--rotate_p", help="Rotate probability", default=0.5, type=float)
@click.option("--min_angle", help="Minimal rotate angle", default=-89, type=int)
@click.option("--max_angle", help="Maximum rotate angle", default=89, type=int)
@click.option("--blur_p", help="Blur probability", default=0.5, type=float)
@click.option("--min_pixel_radius", help="Minimal blur pixel radius", default=1, type=int)
@click.option("--max_pixel_radius", help="Maximum blur pixel radius", default=5, type=int)
@click.option("--offset_p", help="Offset probability", default=0.5, type=float)
@click.option("--min_x_offset", help="Minimal offset in x axis", default=-0.5, type=float)
@click.option("--max_x_offset", help="Maximum offset in x axis", default=0.5, type=float)
@click.option("--min_y_offset", help="Minimal offset y in y axis", default=-0.5, type=float)
@click.option("--max_y_offset", help="Maximum offset y in y axis", default=0.5, type=float)
@click.option("--crop_p", help="Crop probability", default=0.5, type=float)
@click.option("--min_x_crop", help="Minimal crop width", default=0.6, type=float)
@click.option("--max_x_crop", help="Maximum crop width", default=0.9, type=float)
@click.option("--min_y_crop", help="Minimal crop height", default=0.6, type=float)
@click.option("--max_y_crop", help="Maximum crop height", default=0.9, type=float)
def images(source: str, destination: str, n: int, **kwargs) -> None:
    config = AugustImageConfig(**kwargs)
    dest_path = Path(get_directory(destination))
    images = images_in_directory(source)
    for img in images:
        img_path = Path(img)
        print("IMG: ", img_path)
        aug_img = AugustImage(img_path=img_path, config=config)
        aug_img.augment()
        aug_img.save(dest_path / ("aug_" + img_path.name))
    print("Images function")


@click.command()
def audio() -> None:
    print("Audio function")


@click.command()
def text() -> None:
    print("Text function")


cli.add_command(images)
cli.add_command(audio)
cli.add_command(text)
