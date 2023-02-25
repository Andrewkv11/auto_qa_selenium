import allure

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite('Interactions')
class TestInteractions:
    @allure.feature('Sortable Page')
    class TestSortablePage:

        @allure.title('Check changed sortable list and grid')
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before_list, after_list = sortable_page.change_list_order()
            before_grid, after_grid = sortable_page.change_grade_order()
            assert before_list != after_list, "the order of the list has not been changed"
            assert before_grid != after_grid, "the order of the grid has not been changed"

    @allure.feature('Selectable Page')
    class TestSelectable:

        @allure.title('Check changed selectable list and grid')
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, "no elements were selected"
            assert len(item_grid) > 0, "no elements were selected"

    @allure.feature('Resizable Page')
    class TestResizable:

        @allure.title('Check changed resizable boxes')
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert max_box == ('500px', '300px'), "maximum size not equal-to '500px', '300px'"
            assert min_box == ('150px', '150px'), "minimum size not equal-to '150px', '150x'"
            assert max_resize != min_resize, "resizable has not been changed"

    @allure.feature('Droppable Page')
    class TestDroppable:

        @allure.title('Check simple droppable')
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == "Dropped!", "The simple element has not been dropped"

        @allure.title('Check accept droppable')
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_accept, accept = droppable_page.drop_accept()
            assert not_accept == "Drop here", "The dropped element has been accepted"
            assert accept == "Dropped!", "The dropped element has not been accepted"

        @allure.title('Check prevent propogation droppable')
        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent()
            assert not_greedy == "Dropped!", "The element text has not been changed"
            assert not_greedy_inner == "Dropped!", "The element text has not been changed"
            assert greedy == "Outer droppable", "The element text has changed"
            assert greedy_inner == "Dropped!", "The element text has been changed"

        @allure.title('Check revert draggable droppable')
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will_revert')
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will_revert')
            assert will_after_move != will_after_revert, "The elements has not reverted"
            assert not_will_after_move == not_will_after_revert, "The element hes reverted"

    @allure.feature('Draggable Page')
    class TestDraggable:

        @allure.title('Check simple draggable')
        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            before, after = draggable_page.simple_drag_box()
            assert before != after, "The position of the box has not been changed"

        @allure.title('Check axis restricted draggable')
        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            top_x, left_x = draggable_page.axis_restricted_x()
            top_y, left_y = draggable_page.axis_restricted_y()
            assert top_x == [['0'], ['0']], "only X position has been changed"
            assert left_y == [['0'], ['0']], "only Y position has been changed"


