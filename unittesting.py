import unittest

"""
I am learning how to write classes that will test how well
objects and their methods work.  At first, I learned how to
write a simple class (see below) to test the string object
and a few of its methods.  After writing this class, I wrote
the bottommost if __name__ == "__main__" function to activate 
the unittest wrapper on this python file.  I should rewrite that
part it's a mouthfull.  Anyways, anytime this file is
accessed from the terminal, it will run through the class objects
and run each test for potentially every possible value that
could pass through my program's classes, methods and overall
structure.  In other words, I'm trying to break the program in
as many ways as possible as quickly as I can.  This will help 
me design better programs that operate more fluidly, if I can 
figure out how to do it well!

Currently I'm diving into the complexity of testing my own 
objects, and the intricacies that are available and customizable
to make the process efficent.  SetUp TearDown is cool beacuse
I think it loops through the object's methods, building and
destroying a new instance of that object each time it runs
through a test.  Saving memory but also adding calculations, dunno
how fast that can be compared to somethign else.  
"""


"""
here is the basic TestStringMethods object, inheriting from
unittest.TestCase.  Here I am testing a few of the methods
of the string object.
"""


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_lower(self):
        self.assertEqual('FOO'.lower(),'foo')

    def test_title(self):
        self.assertEqual('foo'.title(),'Foo')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_islower(self):
        self.assertTrue('foo'.islower())
        self.assertFalse('FOO'.islower())

    def test_istitle(self):
        self.assertTrue('Foo'.istitle())
        self.assertFalse('foo'.istitle())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(),['hello','world'])

        with self.assertRaises(TypeError):
            s.split(2)


"""
Here is the Widget class that I use while learning how to
design tests for my own customizable objects
"""


class Widget():
    def __init__(self, name):
        self.size = (50, 50)
        self.name = name

    def resize(self,newSize):
        self.size = newSize

    def rename(self,newName):
        self.name = newName


"""
Here is the WidgetTestCase that I'm using to make my own
object tests
"""


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('the widget')

    def tearDown(self):
        self.widget = None

    def test_default_size(self):
        self.assertEqual(self.widget.size,(50,50),'incorrect default size!')

    def test_resize(self):
        self.widget.resize((100,50))
        self.assertEqual(self.widget.size,(100,50),'incorrect resize')

    def test_rename(self):
        self.widget.rename('samswidget')
        self.assertEqual(self.widget.name,'samswidget','wrong name')


"""
this is building a suite of tests from my WidgetTestCase object
note: it includes every method from an object, not always ideal
"""
suite = unittest.TestLoader().loadTestsFromTestCase(WidgetTestCase)

"""
here is a way to customize the suites that are being built, 
by providing an array of methods to be pulled from the object
this is a good way to chunk out the tests that focus on
specific parameters in a very large program

map will apply unittest.TestSuite to WidgetTestCase(tests[n])
, which seems like a generator / mix of a for loop and enum
"""


def make_suite(obj,tests):
    return unittest.TestSuite(map(obj,tests))


"""
to add multiple test suites to a single object, use TestSuite()
in the same way it is used with TestCase.
"""


suite1 = make_suite(WidgetTestCase,['test_resize','test_rename'])
suite2 = make_suite(TestStringMethods,['test_upper','test_lower'])

alltests = unittest.TestSuite([suite1,suite2])

"""
This says that if this program is called from the terminal,
execute unittest.main() which will parse the file and run its
test objects
"""

if __name__ == '__main__':
    unittest.main()

