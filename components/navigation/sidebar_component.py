import re
import allure

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent

class SidebarComponent(BaseComponent):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page, "logout")
        self.dashboard_list_item = SidebarListItemComponent(page, "dashboard")
        self.courses_list_item = SidebarListItemComponent(page, "courses")

    @allure.step("Check visible sidebar")
    def check_visible(self) -> None:
        self.logout_list_item.check_visible("Logout")
        self.dashboard_list_item.check_visible("Dashboard")
        self.courses_list_item.check_visible("Courses")

    @allure.step("Click logout in sidebar")
    def click_logout(self) -> None:
        self.logout_list_item.navigate(expected_url=re.compile(r".*/#/auth/login"))
    
    @allure.step("Click dashboard in sidebar")
    def click_dashboard(self) -> None:
        self.dashboard_list_item.navigate(expected_url=re.compile(r".*/#/dashboard"))

    @allure.step("Click courses in sidebar")
    def click_courses(self) -> None:
        self.courses_list_item.navigate(expected_url=re.compile(r".*/#/courses"))