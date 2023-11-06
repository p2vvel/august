import random
from pathlib import Path

import click

from august.audio.audio import AugustAudio
from august.audio.config import AugustAudioConfig
from august.images.config import AugustImageConfig
from august.images.images import AugustImage
from august.text.config import AugustTextConfig
from august.text.text import AugustText
from august.utils.dirs import files_with_extensions, get_directory


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
    "--min_temperature_ratio", help="Min color temperature change ratio", default=-50, type=int
)
@click.option("--max_temperature_ratio", help="Max color temperature change ratio", default=50, type=int)
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
    image_files = files_with_extensions(source, (".jpg", ".jpeg", ".png"))
    files_to_augment = random.choices(image_files, k=n)
    for index, img in enumerate(files_to_augment):
        img_path = Path(img)
        print("IMG: ", img_path)
        aug_img = AugustImage(audio_path=img_path, config=config)
        aug_img.augment()
        aug_img.save(dest_path / (f"{index}_{img_path.name}"))
    print("Images function")


@click.command()
@click.option("--source", "-s", help="Source directory with audio", required=True)
@click.option("--destination", "-d", help="Destination directory for augmented audio", required=True)
@click.option("--n", "-n", help="Number of augmented audio", required=True, type=int)
@click.option("--time_shift_p", help="Time shift probability", default=0.5, type=float)
@click.option(
    "--min_shift", help="Minimal shift as a fraction of total length", default=-0.5, type=float
)
@click.option("--max_shift", help="Maximum shift as a fraction of total length", default=0.5, type=float)
@click.option("--time_stretch_p", help="Time stretch probability", default=0.5, type=float)
@click.option("--min_stretch_factor", help="Minimal time stretch factor", default=0.5, type=float)
@click.option("--max_stretch_factor", help="Maximum time stretch factor", default=1.5, type=float)
@click.option("--invert_polarity_p", help="Invert polarity probability", default=0.5, type=float)
@click.option("--pitch_scale_p", help="Pitch scale probability", default=0.5, type=float)
@click.option("--min_semitones", help="Minimal pitch scale semitones", default=-6, type=int)
@click.option("--max_semitones", help="Maximum pitch scale semitones", default=6, type=int)
@click.option("--random_gain_p", help="Random gain probability", default=0.5, type=float)
@click.option("--min_gain_factor", help="Minimal gain factor", default=0.5, type=float)
@click.option("--max_gain_factor", help="Maximum gain factor", default=1.5, type=float)
@click.option("--gaussian_noise_p", help="Gaussian noise probability", default=0.5, type=float)
@click.option("--min_gain_amplitude", help="Minimal gain amplitude", default=0.001, type=float)
@click.option("--max_gain_amplitude", help="Maximum gain amplitude", default=0.015, type=float)
@click.option("--time_mask_p", help="Time mask probability", default=0.5, type=float)
@click.option("--min_mask_part", help="Minimal mask part", default=0.01, type=float)
@click.option("--max_mask_part", help="Maximum mask part", default=0.5, type=float)
@click.option("--low_pass_filter_p", help="Low pass filter probability", default=0.5, type=float)
@click.option("--min_low_pass_freq", help="Minimal low pass filter frequency", default=150, type=float)
@click.option("--max_low_pass_freq", help="Maximum low pass filter frequency", default=7500, type=float)
@click.option("--high_pass_filter_p", help="High pass filter probability", default=0.5, type=float)
@click.option("--min_high_pass_freq", help="Minimal high pass filter frequency", default=20, type=float)
@click.option(
    "--max_high_pass_freq", help="Maximum high pass filter frequency", default=2400, type=float
)
@click.option("--room_p", help="Room effect probability", default=0.5, type=float)
def audio(source: str, destination: str, n: int, **kwargs) -> None:
    config = AugustAudioConfig(**kwargs)
    dest_path = Path(get_directory(destination))
    audio_files = files_with_extensions(source, (".mp3", ".wav", ".m4a"))
    files_to_augment = random.choices(audio_files, k=n)
    for index, aud in enumerate(files_to_augment):
        audio_path = Path(aud)
        print("AUDIO: ", audio_path)
        augio = AugustAudio(audio_path=audio_path, config=config)
        augio.augment()
        augio.save(dest_path / (f"{index}_{audio_path.name}"))
    print("Audio function")


@click.option("--source", "-s", help="Source directory with text", required=True)
@click.option("--destination", "-d", help="Destination directory for augmented text", required=True)
@click.option("--n", "-n", help="Number of augmented text", required=True, type=int)
@click.option("--synonym_replace_p", help="Probability of synonym replacement", default=0.3, type=float)
@click.option("--antonym_replace_p", help="Probability of antonym replacement", default=0.3, type=float)
@click.option("--ocr_p", help="Probability of OCR distortion", default=0.3, type=float)
@click.option("--keyboard_p", help="Probability of keyboard typos", default=0.3, type=float)
@click.option(
    "--random_character_p", help="Probability of random character insertion", default=0.3, type=float
)
@click.option(
    "--random_word_delete_p", help="Probability of random word delete", default=0.3, type=float
)
@click.option(
    "--random_word_substitute_p", help="Probability of random word substitute", default=0.3, type=float
)
@click.option("--random_word_swap_p", help="Probability of random word swap", default=0.3, type=float)
@click.option("--spelling_p", help="Probability of misspelling ", default=0.3, type=float)
@click.command()
def text(source: str, destination: str, n: int, **kwargs) -> None:
    config = AugustTextConfig(**kwargs)
    dest_path = Path(get_directory(destination))
    text_files = files_with_extensions(source, (".txt",))
    files_to_augment = random.choices(text_files, k=n)
    for index, txt in enumerate(files_to_augment):
        txt_path = Path(txt)
        print("TEXT: ", txt_path)
        with open(txt_path, "r") as f:
            text_content = f.read()
        txt_aug = AugustText(text=text_content, config=config)
        txt_aug.augment()
        txt_aug.save(dest_path / (f"{index}_{txt_path.name}"))
    print("Text function")


cli.add_command(images)
cli.add_command(audio)
cli.add_command(text)
