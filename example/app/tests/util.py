from ..views import EXAMPLES


class TestEachExample(type):
    '''
    This is a (hopefully) simple metaclass that makes it possible
    to create a TestCase that runs a generic test for every
    Example in the example gallery.

    The class this metaclass is applied to must have one method
    with the following signature:

        def test(self, example):
            ...

    This single method will be used as a "template" from which
    multiple tests are created--one for every Example in the
    gallery. Each test will be called `test_XXX`, where `XXX`
    is the name of the test.
    '''

    @classmethod
    def make_test_method_for_example(cls, test, example):
        def wrapper(self):
            test(self, example)

        wrapper.__name__ = 'test_' + example.basename
        return wrapper

    def __new__(cls, name, bases, namespace):
        if 'test' not in namespace:
            raise Exception('Subclasses must implement a "test"'
                            'method that takes an Example instance.')

        test = namespace.pop('test')

        for example in EXAMPLES.values():
            test_method = cls.make_test_method_for_example(test, example)
            namespace[test_method.__name__] = test_method

        return type.__new__(cls, name, bases, namespace)
