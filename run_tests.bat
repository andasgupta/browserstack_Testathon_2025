@echo off
echo Setting BrowserStack credentials...
set BROWSERSTACK_USERNAME=anikdasgupta_sW03Uz
set BROWSERSTACK_ACCESS_KEY=gFspSApHHEnMSwGzeHk8

echo Installing dependencies...
python -m pip install -r requirements.txt

echo Running BDD tests on BrowserStack...
browserstack-sdk pytest tests/step_defs/ --platform=0

echo Tests completed. Check reports/report.html for detailed results.