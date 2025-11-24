from typing import Pattern
from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class SidebarListItemComponent(BaseComponent):

    def __init__(self, page: Page, indentifier: str) -> None:
        super().__init__(page)

        self.icon = page.get_by_test_id(f"{indentifier}-drawer-list-item-icon")
        self.title = page.get_by_test_id(f"{indentifier}-drawer-list-item-title-text")
        self.button = page.get_by_test_id(f"{indentifier}-drawer-list-item-button")

    def check_visible(self, title: str) -> None:
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        expect(self.button).to_be_visible()

    def navigate(self, expected_url: Pattern[str]) -> None:
        self.button.click()
        expect(self.page).to_have_url(expected_url)