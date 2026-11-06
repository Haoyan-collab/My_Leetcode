from dataclasses import dataclass
@dataclass
class Page:
    url:str
    prev:Page=None
    next:Page=None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = Page(url=homepage)

    def visit(self, url: str) -> None:
        page = Page(url=url,prev=self.cur)
        self.cur.next = page
        self.cur = page

    def back(self, steps: int) -> str:
        cnt = 0
        while self.cur.prev:
            if cnt==steps:
                return self.cur.url
            self.cur=self.cur.prev
            cnt += 1
        return self.cur.url

    def forward(self, steps: int) -> str:
        cnt = 0
        while self.cur.next:
            if cnt==steps:
                return self.cur.url
            self.cur=self.cur.next
            cnt += 1
        return self.cur.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)