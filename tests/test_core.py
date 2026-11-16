import pytest
from henai.core import validate, MODELS

def test_models():
    assert "FLUX.1-schnell" in MODELS
    assert "SDXL Turbo" in MODELS

def test_seed_reproducibility():
    assert validate("FLUX.1-schnell", 1024, 1024, 4, 0, 123).seed == 123

def test_random_seed():
    assert 0 <= validate("SDXL Turbo", 512, 512, 1, 0, -1).seed < 2**32

@pytest.mark.parametrize("width,height", [(300, 512), (1024, 0), (1600, 1024)])
def test_invalid_dimensions(width, height):
    with pytest.raises(ValueError):
        validate("SDXL Turbo", width, height, 1, 0, 0)

def test_invalid_model():
    with pytest.raises(ValueError):
        validate("fake", 512, 512, 1, 0, 0)
