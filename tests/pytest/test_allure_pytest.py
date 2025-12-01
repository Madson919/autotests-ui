import allure

@allure.step("Open browser")
def open_browser():
    with allure.step("Get browser"):
        pass
    with allure.step("Start browser"):
        pass

@allure.step("Closer browser")
def close_browser():
    pass

@allure.step("Close browser with title '{title}'")
def create_course(title: str):
    pass


def test_feature():
    open_browser()
    create_course(title="Test Course")
    close_browser() 