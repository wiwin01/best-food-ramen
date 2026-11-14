"""make.fun entry for food-picture-01: copy the food picture to entry.png."""
import os
import shutil
from pathlib import Path

ASSET = Path(__file__).resolve().parent / "food.jpg"


def main() -> None:
    # The gate is hard: entry.png must be at most 1 MiB and 1024x1024.
    # Fail loudly here rather than submit an invalid image.
    size = ASSET.stat().st_size
    assert size <= 1_048_576, f"asset too large: {size} bytes"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ASSET, out_dir / "entry.png")


if __name__ == "__main__":
    main()
