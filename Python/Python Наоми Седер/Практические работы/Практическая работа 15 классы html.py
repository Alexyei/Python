class htmlelement():
    def __init__(self, tag, text=None, subelement=None):
        self.text = text
        self.subelement = subelement
        self._tag = tag
        # print(type(super), type(super()))

    def __str__(self):
        text = f"<{self._tag}>\n"
        if self.text is not None:
            text += self.text + "\n"
        if self.subelement is not None:
            text += str(self.subelement)
        text += f"</{self._tag}>\n"
        return text


class html(htmlelement):
    def __init__(self, text=None, subelement=None):
        # print(type(super), type(super()), "1")
        super().__init__("html", text, subelement)


class body(htmlelement):
    def __init__(self, text=None, subelement=None):
        super().__init__("body", text, subelement)


class p(htmlelement):
    def __init__(self, text=None, subelement=None):
        super().__init__("p", text, subelement)


def main():
    para = p(text="this is some body text")
    doc_body = body(text="This is the body", subelement=para)
    doc = html(subelement=doc_body)
    print(doc, end="")


if __name__ == "__main__":
    main()
