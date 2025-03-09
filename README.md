# Static Site Generator

A simple static site generator built with Python. This project converts Markdown content into HTML, making it easy to create and manage static websites.

## Features
- Converts Markdown files to HTML
- Supports inline and block-level Markdown elements
- Processes images and links automatically
- Customizable templates for HTML generation
- Copies static assets (CSS, images) to the output directory

## Project Structure
```
static-site-generator
├── README.md           # Project documentation
├── build.sh            # Shell script to automate site build
├── content/            # Markdown content for the site
│   ├── blog/           # Blog posts stored as Markdown
│   ├── contact/        # Contact page
│   └── index.md        # Homepage content
├── docs/               # Generated HTML output
│   ├── blog/
│   ├── contact/
│   ├── images/
│   ├── index.css       # Stylesheet
│   └── index.html      # Main entry point
├── main.sh             # Shell script for running the generator
├── src/                # Source code for the generator
│   ├── block_markdown.py
│   ├── generate_page.py
│   ├── htmlnode.py
│   ├── inline_markdown.py
│   ├── main.py         # Main script for running the generator
│   ├── textnode.py
│   └── tests/          # Unit tests
├── static/             # Static assets (CSS, images)
│   ├── images/
│   └── index.css
├── template.html       # HTML template for rendering pages
└── test.sh             # Test script
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/static-site-generator.git
   cd static-site-generator
   ```
2. Install dependencies (if any):
   ```sh
   pip install -r requirements.txt
   ```

## Usage
To generate the static site, run:
```sh
python src/main.py
```
The generated HTML files will be placed in the `docs/` directory.

## Contributing
Contributions are welcome! Feel free to submit a pull request.

## License
This project is licensed under the MIT License.

