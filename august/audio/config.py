from pydantic import BaseModel, Field


class AugustAudioConfig(BaseModel):
    time_shift_p: float = Field(0.5, description="Time shift probability", ge=0, le=1)
    min_shift: float = Field(
        -0.5, description="Minimal shift as a fraction of total length", ge=-1, le=1
    )
    max_shift: float = Field(0.5, description="Maximum shift as a fraction of total length", ge=-1, le=1)

    time_stretch_p: float = Field(0.5, description="Time stretch probability", ge=0, le=1)
    min_stretch_factor: float = Field(0.5, description="Minimal time stretch factor")
    max_stretch_factor: float = Field(1.5, description="Maximum time stretch factor")

    invert_polarity_p: float = Field(0.5, description="Invert polarity probability", ge=0, le=1)

    pitch_scale_p: float = Field(0.5, description="Pitch scale probability", ge=0, le=1)
    min_semitones: int = Field(-6, description="Minimal pitch scale semitones")
    max_semitones: int = Field(6, description="Maximum pitch scale semitones")

    random_gain_p: float = Field(0.5, description="Random gain probability", ge=0, le=1)
    min_gain_factor: float = Field(0.5, description="Minimal gain factor")
    max_gain_factor: float = Field(1.5, description="Maximum gain factor")

    gaussian_noise_p: float = Field(0.5, description="Gaussian noise probability", ge=0, le=1)
    min_gain_amplitude: float = Field(0.001, description="Minimal gain amplitude")
    max_gain_amplitude: float = Field(0.015, description="Maximum gain amplitude")

    time_mask_p: float = Field(0.5, description="Time mask probability", ge=0, le=1)
    min_mask_part: float = Field(0.01, description="Minimal mask part", ge=0, le=1)
    max_mask_part: float = Field(0.5, description="Maximum mask part", ge=0, le=1)

    low_pass_filter_p: float = Field(0.5, description="Low pass filter probability", ge=0, le=1)
    min_low_pass_freq: float = Field(150, description="Minimal low pass filter frequency")
    max_low_pass_freq: float = Field(7500, description="Maximum low pass filter frequency")

    high_pass_filter_p: float = Field(0.5, description="High pass filter probability", ge=0, le=1)
    min_high_pass_freq: float = Field(20, description="Minimal high pass filter frequency")
    max_high_pass_freq: float = Field(2400, description="Maximum high pass filter frequency")

    room_p: float = Field(0.5, description="Room effect probability", ge=0, le=1)
