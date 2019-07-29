import types
import typing
import unittest

from gmail_permutator import gmail_permutator


class MyTestCase(unittest.TestCase):

    def test_is_generator(self):
        gp = gmail_permutator("test@gmail.com")

        self.assertIsInstance(gp, types.GeneratorType)
        self.assertIsInstance(gp, typing.Generator)

    def test_less_dots(self):
        gp = gmail_permutator("test@gmail.com", return_only_base=True)

        refs = [
            "t.est",
            "te.st",
            "t.e.st",
            "tes.t",
            "t.es.t",
            "te.s.t",
            "t.e.s.t"
        ]
        gens = [next(gp) for _ in range(len(refs))]
        self.assertEqual(refs, gens)

    def test_more_dots(self):
        gp = gmail_permutator("test@gmail.com", return_only_base=True)

        refs = [
            "t.est",
            "te.st",
            "t.e.st",
            "tes.t",
            "t.es.t",
            "te.s.t",
            "t.e.s.t",
            "t..e.s.t",
            "t.e..s.t",
            "t..e..s.t",
            "t.e.s..t",
            "t..e.s..t",
            "t.e..s..t",
            "t..e..s..t",
            "t...e..s..t"
        ]
        gens = [next(gp) for _ in range(len(refs))]
        self.assertEqual(refs, gens)

    def test_limit(self):
        gp = gmail_permutator("test@gmail.com", -1, return_only_base=True)
        self.assertEqual(0, len(list(gp)))

        gp = gmail_permutator("test@gmail.com", 0, return_only_base=True)
        self.assertEqual(0, len(list(gp)))

        gp = gmail_permutator("test@gmail.com", 1, return_only_base=True)
        self.assertEqual(1, len(list(gp)))

        gp = gmail_permutator("test@gmail.com", 10, return_only_base=True)
        self.assertEqual(10, len(list(gp)))

    def test_appending_base(self):
        gp = gmail_permutator("test@gmail.com")

        refs = [
            "t.est@gmail.com",
            "te.st@gmail.com",
            "t.e.st@gmail.com"
        ]
        gens = [next(gp) for _ in range(len(refs))]
        self.assertEqual(refs, gens)


if __name__ == '__main__':
    unittest.main()
