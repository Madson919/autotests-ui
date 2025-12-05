import allure

from playwright.sync_api import Page, expect
from tools.logger import get_logger
from typing import Pattern


logger = get_logger("BASE_COMPONENT")

class BaseComponent:
    def __init__(self, page: Page) -> None:
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]) -> None:
        step = f"Verify that the current page URL matches the {expected_url.pattern} pattern."

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
