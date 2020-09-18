from time import sleep

from page.app import APP


class TestUsedPO:

    def setup(self):
        self.app = APP()
        pass

    def teardown(self):
        self.app.quit()

    def test_search(self):
        result = self.app.start().main().goto_market().goto_search().search("BRK.A")
        result.view_search()
        sleep(3)
