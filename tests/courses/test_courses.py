import pytest
from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage

@pytest.mark.regression
@pytest.mark.courses
class TestCourses:
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible(username="username")
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(url="https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="",
            description="",
            estimated_time="",
            min_score="0",
            max_score="0"
        )
        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image(file="./testdata/files/image.png")

        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            estimated_time="2 weeks",
            max_score=100,
            min_score=10
        )

    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_form.fill(
            title="New Course",
            description="New Course",
            estimated_time="1 hour",
            min_score="10",
            max_score="100"
        )
        create_course_page.image_upload_widget.upload_preview_image(file="./testdata/files/image.png")
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.course_view.check_visible(
            index=0,
            title="New Course",
            estimated_time="1 hour",
            min_score=10,
            max_score=100
        )

        courses_list_page.course_menu.click_edit(index=0)

        create_course_page.create_course_form.fill(
            title="Edit Course",
            description="Edit Course",
            estimated_time="1 day",
            min_score="1",
            max_score="45"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.course_view.check_visible(
            index=0,
            title="Edit Course",
            estimated_time="1 day",
            min_score=1,
            max_score=45
        )