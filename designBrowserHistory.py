class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.current = homepage
        self.backward = [] # stack
        self.forwardHist = [] # stack
        

    def visit(self, url: str) -> None:
        self.forwardHist = []
        self.backward.append(self.current)
        self.current = url
        

    def back(self, steps: int) -> str:
        self.forwardHist.append(self.current)
        
        while len(self.backward) > 0 and steps > 0:
            self.forwardHist.append(self.backward.pop())
            steps -= 1
            
        self.current = self.forwardHist.pop()
        return self.current
        

    def forward(self, steps: int) -> str:
        self.backward.append(self.current)
        
        while len(self.forwardHist) > 0 and steps > 0:
            self.backward.append(self.forwardHist.pop())
            steps -= 1
            
        self.current = self.backward.pop()
        return self.current
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)