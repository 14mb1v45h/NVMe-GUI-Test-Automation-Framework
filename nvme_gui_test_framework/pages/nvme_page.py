from selenium.webdriver.common.by import By
from .base_page import BasePage

class NVMePage(BasePage):
    # Locators (example IDs/classes - adjust based on actual GUI)
    IDENTIFY_BUTTON = (By.ID, "identify-btn")
    SMART_LOG_BUTTON = (By.ID, "smart-log-btn")
    FIRMWARE_UPDATE_BUTTON = (By.ID, "firmware-update-btn")
    FORMAT_BUTTON = (By.ID, "format-btn")
    SELF_TEST_BUTTON = (By.ID, "self-test-btn")
    ENDURANCE_GROUP_INPUT = (By.ID, "endurance-group-input")
    POWER_STATE_DROPDOWN = (By.ID, "power-state-dropdown")
    TELEMETRY_BUTTON = (By.ID, "telemetry-btn")
    RESULT_TEXT = (By.ID, "result-text")

    def navigate(self):
        self.driver.get("http://localhost:5000")
        logger.info("Navigated to NVMe GUI")

    def get_identify(self):
        self.click(self.IDENTIFY_BUTTON)
        return self.find_element(self.RESULT_TEXT).text

    def get_smart_log(self):
        self.click(self.SMART_LOG_BUTTON)
        return self.find_element(self.RESULT_TEXT).text

    def update_firmware(self, version):
        self.click(self.FIRMWARE_UPDATE_BUTTON)
        input_field = self.find_element((By.ID, "firmware-version"))
        input_field.clear()
        input_field.send_keys(version)
        self.click((By.ID, "update-confirm"))
        return self.find_element(self.RESULT_TEXT).text

    def format_drive(self):
        self.click(self.FORMAT_BUTTON)
        return self.find_element(self.RESULT_TEXT).text

    def run_self_test(self, test_type):
        self.click(self.SELF_TEST_BUTTON)
        dropdown = self.find_element((By.ID, "test-type-dropdown"))
        dropdown.send_keys(test_type)
        self.click((By.ID, "start-test"))
        return self.find_element(self.RESULT_TEXT).text

    def get_endurance_group(self, group_id):
        self.find_element(self.ENDURANCE_GROUP_INPUT).send_keys(group_id)
        self.click((By.ID, "get-endurance"))
        return self.find_element(self.RESULT_TEXT).text

    def set_power_state(self, state):
        dropdown = self.find_element(self.POWER_STATE_DROPDOWN)
        dropdown.send_keys(state)
        self.click((By.ID, "set-power"))
        return self.find_element(self.RESULT_TEXT).text

    def get_telemetry(self):
        self.click(self.TELEMETRY_BUTTON)
        return self.find_element(self.RESULT_TEXT).text