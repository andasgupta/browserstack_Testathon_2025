@echo off
echo Setting BrowserStack credentials...
set BROWSERSTACK_USERNAME=anikdasgupta_sW03Uz
set BROWSERSTACK_ACCESS_KEY=gFspSApHHEnMSwGzeHk8

echo Running BDD tests directly with pytest...
python -m pytest tests/step_defs/ --platform=0 -v

echo Tests completed. Check reports/report.html for detailed results.