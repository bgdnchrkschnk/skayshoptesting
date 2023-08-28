
def pytest_addoption(parser):

    # Implement custom command option for pytest - setting particular browser
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Set browser on which we would like to execute tests. Available values: chrome, firefox, safari")

    # Implement custom command option for pytest - setting particular prod env
    parser.addoption("--env",
                     action="store",
                     default="prod",
                     help="Set environment - will affect on homepage url. Available values: dev, stage, prod")


# Putting received browser in
def pytest_generate_tests(metafunc):
    if "webdriver" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("-browser").split(", ")
        metafunc.parametrize("webdriver", browsers, indirect=True)
