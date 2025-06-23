import pytest
import re

@pytest.mark.parametrize("group_id, min_life", [("group0", 90), ("group1", 0)])
def test_endurance_group(nvme_page, group_id, min_life):
    result = nvme_page.get_endurance_group(group_id)
    life = int(re.search(r'remaining_life: (\d+)', result).group(1)) if re.search(r'remaining_life: (\d+)', result) else 0
    assert life >= min_life

@pytest.mark.parametrize("state, expected_result", [("PS0", True), ("PS1", True), ("PS2", False)])
def test_autonomous_power_state(nvme_page, state, expected_result):
    result = nvme_page.set_power_state(state)
    assert state in result.lower() if expected_result else "invalid" in result.lower()

@pytest.mark.parametrize("min_errors", [0, 1])
def test_telemetry(nvme_page, min_errors):
    result = nvme_page.get_telemetry()
    errors = int(re.search(r'errors: (\d+)', result).group(1)) if re.search(r'errors: (\d+)', result) else 0
    assert "timestamp" in result.lower()
    assert errors >= min_errors