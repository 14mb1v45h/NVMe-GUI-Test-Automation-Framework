# NVMe GUI Test Automation Framework
A pytest-based framework using Selenium for testing an NVMe SSD management GUI application.

## Features
- Tests for generic NVMe features (Identify, SMART, Firmware Update, Format, Self-Test).
- NVMe 2.0 features (Endurance Groups, Autonomous Power State Transitions, Telemetry).
- Logging, HTML reporting, and parameterized tests.
- Selenium automation for web GUI testing.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Start the GUI app (e.g., `python app.py` for localhost:5000)
3. Run tests: `pytest --html=report.html --self-contained-html`

## Future Improvements
- Add cross-browser testing (e.g., Firefox).
- Integrate with CI/CD pipelines.