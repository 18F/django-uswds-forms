import pprint
from pathlib import Path
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from .util import TestEachExample

AXE_JS = Path(__file__).resolve().parent / 'vendor' / 'axe.js'


class AxeTests(StaticLiveServerTestCase, metaclass=TestEachExample):
    '''
    Run aXe-core on every example's URL. Raise an exception if
    there are any accessibility issues and log any violations to stdout.
    '''

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.axe_js = AXE_JS.read_text()
        cls.selenium = webdriver.PhantomJS()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test(self, example):
        self.selenium.get('%s%s' % (self.live_server_url, example.url))

        result = self.selenium.execute_async_script(
            self.axe_js +
            r'''
            var callback = arguments[arguments.length - 1];
            axe.run(function(err, results) {
              callback({
                error: err && err.toString(),
                results: results
              });
            });
            ''')

        error = result['error']
        if error is not None:
            raise Exception('axe.run() failed: {}'.format(error))

        violations = [v for v in result['results']['violations']]
        if violations:
            pprint.pprint(violations)
            print("For more details, please install the aXe browser "
                  "extension.")
            print("Learn more at: https://www.deque.com/products/axe/")

            raise Exception('axe.run() found violations: ' +
                            ', '.join(v['id'] for v in violations))
