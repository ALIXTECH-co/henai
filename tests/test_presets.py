import pytest
from henai.core import validate
from henai.presets import PRESETS, get_preset

@pytest.mark.parametrize("name", PRESETS)
def test_presets_are_valid(name):
    preset = get_preset(name)
    result = validate(preset.model, preset.width, preset.height, preset.steps, preset.guidance, 42)
    assert result.seed == 42

def test_unknown_preset():
    with pytest.raises(ValueError):
        get_preset("unknown")
