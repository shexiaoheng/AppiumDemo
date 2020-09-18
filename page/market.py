from page.base_page import BasePage
from page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../data/market.yaml")
        return Search(self._driver)
