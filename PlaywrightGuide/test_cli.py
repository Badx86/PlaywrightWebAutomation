

def test_cli(page):
    page.goto("https://youtube.com")

    # playwright install --help
    # playwright codegen youtube.com --save-storage=auth.json
    # playwright open --load-storage=auth.json 'app_name'

    # playwright wk wikipedia.org
    # playwright open --device="iPhone 11" youtube.com
    # playwright open --viewport-size=800,600

    # playwright pdf https://en.wikipedia.org/wiki/PDF wiki.pdf