from pages.interactions_page import SortablePage, SelectablePage


class TestInteractions:

    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before_list, after_list = sortable_page.change_list_order()
            before_grid, after_grid = sortable_page.change_grade_order()
            assert before_list != after_list, "the order of the list has not been changed"
            assert before_grid != after_grid, "the order of the grid has not been changed"

    class TestSelectable:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, "no elements were selected"
            assert len(item_grid) > 0, "no elements were selected"


