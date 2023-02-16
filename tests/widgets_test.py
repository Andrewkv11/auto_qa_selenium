import time

from pages.widgets_page import AccordianPage, AutoCompletePage


class TestWidgets:

    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'first accordian is incorrect'
            assert second_title == 'Where does it come from?' and first_content > 0, 'second accordian is incorrect'
            assert third_title == 'Why do we use it?' and first_content > 0, 'third accordian is incorrect'

    class TestAutoComplete:
        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result, 'the added colors are missing in the input'

        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            autocomplete_page.remove_value_from_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before - 1 == count_value_after, 'value was not deleted'

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result, 'the added color is missing in the input'

