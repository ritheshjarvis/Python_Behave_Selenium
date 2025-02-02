from behave_html_formatter.html import HTMLFormatter

class Reporters():
    
    def __init__(self, context):
        self.context = context

    def add_screenshot_to_HTMLFormatter(self, screenshot_data, caption="Screenshot123"):
        for formatter in self.context._runner.formatters:
            if "html" in formatter.name and hasattr(formatter, 'embedding') and isinstance(formatter, HTMLFormatter):
                formatter.embedding(mime_type="image/png", data=screenshot_data, caption=caption)
                print("Screenshot added ----------")
        