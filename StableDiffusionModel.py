from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class StableDiffusionModel:
    prompt: str = ""
    negative_prompt: str = "easynegative"
    styles: List[str] = field(default_factory=lambda: ["string"])
    seed: int = -1
    subseed: int = -1
    sampler_name: str = "Euler a"
    scheduler: str = ""
    batch_size: int = 1
    n_iter: int = 1
    steps: int = 20
    cfg_scale: float = 7.0
    width: int = 512
    height: int = 512
    send_images: bool = True
    save_images: bool = True

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
