from __future__ import annotations

import unittest

from scripts.bump_version import bump_version


class BumpVersionTests(unittest.TestCase):
    def test_patch_stable_starts_next_patch_dev_release(self) -> None:
        self.assertEqual("0.1.1.dev1", bump_version("0.1.0", "patch"))

    def test_patch_dev_increments_dev_number(self) -> None:
        self.assertEqual("0.1.1.dev2", bump_version("0.1.1.dev1", "patch"))

    def test_finalize_patch_dev_advances_to_next_patch_release(self) -> None:
        self.assertEqual("0.1.2", bump_version("0.1.1.dev2", "finalize"))

    def test_minor_stable_starts_next_minor_dev_release(self) -> None:
        self.assertEqual("0.2.2.dev1", bump_version("0.1.2", "minor"))

    def test_minor_dev_advances_minor_and_resets_dev_number(self) -> None:
        self.assertEqual("0.3.2.dev1", bump_version("0.2.2.dev1", "minor"))

    def test_finalize_minor_dev_drops_dev_suffix(self) -> None:
        self.assertEqual("0.3.2", bump_version("0.3.2.dev1", "finalize"))

    def test_finalize_stable_release_fails(self) -> None:
        with self.assertRaises(ValueError):
            bump_version("0.3.2", "finalize")


if __name__ == "__main__":
    unittest.main()
