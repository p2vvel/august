# August
### Data augumentation module


August is a simple and straightforward Python library designed to streamline the process of data augmentation for various machine learning use cases. Whether you are working with image, audio, or text data, August provides a set of basic augmentations and lets you to create your own.

### Augmentations Out of the Box:

* Images:
    - rotation
    - color space (bw, sepia, warm, cold)
    - mirror, flip
    - noise
    - blur
    - crop
    - offset
- Audio:
    - Time shifting
    - Time stretching
    - Pitch scaling
    - Noise addition
    - Impulse response addition
    - Filters
    - Polarity Inversion
    - Random gain
    - Time masking 
    - Frequency masking
- Text:
    - synonym replacement
    - random insertion
    - random swap
    - random deletion
    - shuffle sentences randomly
    - exclude duplicates

## Command line use
```
august --help

Options:
  --help  Show this message and exit.

Commands:
  audio
  images
  text
```

```
august images --help

Options:
  -s, --source TEXT               Source directory with images  [required]
  -d, --destination TEXT          Destination directory for augmented images
                                  [required]
  -n, --n INTEGER                 Number of augmented images  [required]
  --mirror_p FLOAT                Mirror probability
  --flip_p FLOAT                  Flip probability
  --color_p FLOAT                 Color change probability
  --temperature_p FLOAT           Color temperature probability
  --min_temperature_ratio INTEGER
                                  Min color temperature change ratio
  --max_temperature_ratio INTEGER
                                  Max color temperature change ratio
  --rotate_p FLOAT                Rotate probability
  --min_angle INTEGER             Minimal rotate angle
  --max_angle INTEGER             Maximum rotate angle
  --blur_p FLOAT                  Blur probability
  --min_pixel_radius INTEGER      Minimal blur pixel radius
  --max_pixel_radius INTEGER      Maximum blur pixel radius
  --offset_p FLOAT                Offset probability
  --min_x_offset FLOAT            Minimal offset in x axis
  --max_x_offset FLOAT            Maximum offset in x axis
  --min_y_offset FLOAT            Minimal offset y in y axis
  --max_y_offset FLOAT            Maximum offset y in y axis
  --crop_p FLOAT                  Crop probability
  --min_x_crop FLOAT              Minimal crop width
  --max_x_crop FLOAT              Maximum crop width
  --min_y_crop FLOAT              Minimal crop height
  --max_y_crop FLOAT              Maximum crop height
  --help                          Show this message and exit.
```

```
august.main audio --help

Options:
  -s, --source TEXT           Source directory with audio  [required]
  -d, --destination TEXT      Destination directory for augmented audio
                              [required]
  -n, --n INTEGER             Number of augmented audio  [required]
  --time_shift_p FLOAT        Time shift probability
  --min_shift FLOAT           Minimal shift as a fraction of total length
  --max_shift FLOAT           Maximum shift as a fraction of total length
  --time_stretch_p FLOAT      Time stretch probability
  --min_stretch_factor FLOAT  Minimal time stretch factor
  --max_stretch_factor FLOAT  Maximum time stretch factor
  --invert_polarity_p FLOAT   Invert polarity probability
  --pitch_scale_p FLOAT       Pitch scale probability
  --min_semitones INTEGER     Minimal pitch scale semitones
  --max_semitones INTEGER     Maximum pitch scale semitones
  --random_gain_p FLOAT       Random gain probability
  --min_gain_factor FLOAT     Minimal gain factor
  --max_gain_factor FLOAT     Maximum gain factor
  --gaussian_noise_p FLOAT    Gaussian noise probability
  --min_gain_amplitude FLOAT  Minimal gain amplitude
  --max_gain_amplitude FLOAT  Maximum gain amplitude
  --time_mask_p FLOAT         Time mask probability
  --min_mask_part FLOAT       Minimal mask part
  --max_mask_part FLOAT       Maximum mask part
  --low_pass_filter_p FLOAT   Low pass filter probability
  --min_low_pass_freq FLOAT   Minimal low pass filter frequency
  --max_low_pass_freq FLOAT   Maximum low pass filter frequency
  --high_pass_filter_p FLOAT  High pass filter probability
  --min_high_pass_freq FLOAT  Minimal high pass filter frequency
  --max_high_pass_freq FLOAT  Maximum high pass filter frequency
  --room_p FLOAT              Room effect probability
  --help                      Show this message and exit.
```

```
august text --help

Options:
  --spelling_p FLOAT              Probability of misspelling
  --random_word_swap_p FLOAT      Probability of random word swap
  --random_word_substitute_p FLOAT
                                  Probability of random word substitute
  --random_word_delete_p FLOAT    Probability of random word delete
  --random_character_p FLOAT      Probability of random character insertion
  --keyboard_p FLOAT              Probability of keyboard typos
  --ocr_p FLOAT                   Probability of OCR distortion
  --antonym_replace_p FLOAT       Probability of antonym replacement
  --synonym_replace_p FLOAT       Probability of synonym replacement
  -n, --n INTEGER                 Number of augmented text  [required]
  -d, --destination TEXT          Destination directory for augmented text
                                  [required]
  -s, --source TEXT               Source directory with text  [required]
  --help                          Show this message and exit.
```


## Extending Augmentation Classes

August has been built with extensibility in mind. If you want to write your own augmentation method, just write it and decrorate it with proper @mark_augmentation decorator.

Example augmentation extensions:
```
from august.image.decorators import mark_augmentation as image_augmentation
from august.audio.decorators import mark_augmentation as audio_augmentation
from august.text.decorators import mark_augmentation as text_augmentation

@image_augmentation
def image_augmentation(self) -> None:
  self.image = self.image
  
@text_augmentation
def text_augmention(self) -> None:
  self.text = "hello world"
    
@audio_augmentation
 def audio_augmentation(self) -> None:
  self.y = self.y / 2
  
```