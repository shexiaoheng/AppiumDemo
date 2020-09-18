from page.base_page import BasePage


class Search(BasePage):
    def search(self, value):
        self._params["value"] = value
        self.steps("../data/search.yaml")
        return self

    def view_search(self):
        self.steps("../data/view_search.yaml")