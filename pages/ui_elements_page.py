"""A catalogue of small widgets: /practice-different-ui-elements

Each attribute is one widget. Actions stay one line so a test reads clearly:
    ui.text_field.fill("hello")
    ui.show_notification.click()
"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class UiElementsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page, "/practice-different-ui-elements")
        self.text_field = page.get_by_test_id("ui-text-field")
        self.textarea = page.get_by_test_id("ui-textarea")
        self.single_dropdown = page.get_by_test_id("ui-single-dropdown")
        self.multi_dropdown = page.get_by_test_id("ui-multi-dropdown")
        self.single_checkbox = page.get_by_test_id("ui-single-checkbox")
        self.date_picker = page.get_by_test_id("ui-datepicker")
        self.slider = page.get_by_test_id("ui-slider")
        self.file_upload = page.get_by_test_id("ui-file-upload")
        self.click_button = page.get_by_test_id("ui-click-button")
        self.open_modal = page.get_by_test_id("ui-modal-open")
        self.show_notification = page.get_by_test_id("ui-show-notification")
        self.tooltip = page.get_by_test_id("ui-tooltip-trigger")
        self.ready = self.text_field
