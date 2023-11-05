from pydantic import BaseModel, Field


class AugustImageConfig(BaseModel):
    mirror_p: float = Field(0.5, description="Mirror probability", ge=0, le=1)
    flip_p: float = Field(0.5, description="Flip probability", ge=0, le=1)
    color_p: float = Field(0.5, description="Color change probability", ge=0, le=1)

    temperature_p: float = Field(0.5, description="Color temperature probability", ge=0, le=1)
    min_temperature_ratio: int = Field(-50, description="Minimal color temperature change ratio")
    max_temperature_ratio: int = Field(50, description="Maximum color temperature change ratio")

    rotate_p: float = Field(0.5, description="Rotate probability", ge=0, le=1)
    min_angle: int = Field(-89, description="Minimal rotate angle")
    max_angle: int = Field(89, description="Maximum rotate angle")

    blur_p: float = Field(0.5, description="Blur probability", ge=0, le=1)
    min_pixel_radius: int = Field(1, description="Minimal blur pixel radius")
    max_pixel_radius: int = Field(5, description="Maximum blur pixel radius")

    offset_p: float = Field(0.5, description="Offset probability", ge=0, le=1)
    min_x_offset: float = Field(-0.5, description="Minimal offset in x axis", ge=-1, le=1)
    max_x_offset: float = Field(0.5, description="Maximum offset in x axis", ge=-1, le=1)
    min_y_offset: float = Field(-0.5, description="Minimal offset y in y axis", ge=-1, le=1)
    max_y_offset: float = Field(0.5, description="Maximum offset y in y axis", ge=-1, le=1)

    crop_p: float = Field(0.5, description="Crop probability", ge=0, le=1)
    min_x_crop: float = Field(0.6, description="Minimal crop width", ge=0, le=1)
    max_x_crop: float = Field(0.9, description="Maximum crop width", ge=0, le=1)
    min_y_crop: float = Field(0.6, description="Minimal crop height", ge=0, le=1)
    max_y_crop: float = Field(0.9, description="Maximum crop height", ge=0, le=1)
