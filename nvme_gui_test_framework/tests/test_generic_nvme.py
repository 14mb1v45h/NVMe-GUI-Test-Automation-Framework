import pytest

def test_identify(nvme_page):
    result = nvme_page.get_identify()
    assert "NVMeSSD" in result
    assert "capacity" in result.lower()

@pytest.mark.parametrize("temp_range", [(30, 50), (50, 70)])
def test_smart_log(nvme_page, temp_range):
    result = nvme_page.get_smart_log()
    temp = int(re.search(r'temperature: (\d+)', result).group(1)) if re.search(r'temperature: (\d+)', result) else 0
    assert temp_range[0] <= temp <= temp_range[1]
    assert "health" in result.lower()

def test_update_firmware(nvme_page):
    result = nvme_page.update_firmware("2.0.1")
    assert "updated" in result.lower() or "failed" in result.lower()

@pytest.mark.parametrize("lba_size", [512, 4096])
def test_format(nvme_page, lba_size):
    result = nvme_page.format_drive()
    assert "formatted" in result.lower() or "skipped" in result.lower()
    assert str(lba_size) in result.lower()

@pytest.mark.parametrize("test_type", ["short", "extended", "invalid"])
def test_device_self_test(nvme_page, test_type):
    result = nvme_page.run_self_test(test_type)
    if test_type in ["short", "extended"]:
        assert "completed" in result.lower()
        assert "pass" in result.lower()
    else:
        assert "invalid" in result.lower()