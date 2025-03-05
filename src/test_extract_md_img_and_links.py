import unittest

from extract_md_img_and_links import (
    extract_markdown_images,
    extract_markdown_links
)


class TestExtractLinksAndImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is a text with a [google](https://www.google.com)"
        )
        self.assertListEqual([("google", "https://www.google.com")], matches)

if __name__ == "__main__":
    unittest.main()