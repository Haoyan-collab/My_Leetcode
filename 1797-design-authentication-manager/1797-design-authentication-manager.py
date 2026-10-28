class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tkmap = {}
        self.length = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tkmap[tokenId] = currentTime + self.length

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tkmap and self.tkmap[tokenId] > currentTime:
            self.tkmap[tokenId] = currentTime + self.length

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for key,value in self.tkmap.items():
            if value > currentTime:
                cnt += 1
        return cnt


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)