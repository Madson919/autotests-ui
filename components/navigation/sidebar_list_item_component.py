import allure

from typing import Pattern
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text
from elements.button import Button

class SidebarListItemComponent(BaseComponent):

    def __init__(self, page: Page, indentifier: str) -> None:
        super().__init__(page)

        self.icon = Icon(page, f"{indentifier}-drawer-list-item-icon", "Sidebar")
        self.title = Text(page, f"{indentifier}-drawer-list-item-title-text", "Sidebar Title")
        self.button = Button(page, f"{indentifier}-drawer-list-item-button", "Sidebar Description")

    @allure.step("Check visible '{title}' sidebar list item")
    def check_visible(self, title: str) -> None:
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]) -> None:
        self.button.click()
        self.check_current_url(expected_url)