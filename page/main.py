from page.base_page import BasePage
from page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("/data/main.yaml")
        return Market(self._driver)
