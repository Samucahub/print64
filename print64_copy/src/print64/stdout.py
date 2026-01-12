import sys
import base64

_original_stdout = sys.stdout


class Base64Stdout:
    def __init__(self, original_stdout):
        self.original_stdout = original_stdout
        self.buffer = ""

    def write(self, text):
        if text:
            self.buffer += text

            if text.endswith('\n'):
                text_to_encode = self.buffer.rstrip('\n')
                if text_to_encode:
                    encoded = base64.b64encode(
                        text_to_encode.encode("utf-8")
                    ).decode("ascii")
                    self.original_stdout.write(encoded + "\n")
                else:
                    self.original_stdout.write("\n")
                self.buffer = ""

    def flush(self):
        if self.buffer:
            encoded = base64.b64encode(
                self.buffer.encode("utf-8")
            ).decode("ascii")
            self.original_stdout.write(encoded)
            self.buffer = ""
        self.original_stdout.flush()


def enable():
    sys.stdout = Base64Stdout(_original_stdout)


def disable():
    sys.stdout = _original_stdout
