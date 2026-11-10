class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        Is4, Is6 = True,True
        if '.' in queryIP:
            q = queryIP.split('.')
            if len(q) != 4:
                return "Neither"
            for s in q:
                if (not s or
                    not s.isascii() or
                    not s.isdigit() or
                    (len(s) > 1 and s[0] == '0') or
                    int(s) > 255):
                    return "Neither"
            if Is4:
                return "IPv4"
        
        else:
            q = queryIP.split(':')
            if len(q) != 8:
                return "Neither"
            for s in q:
                if len(s)<1 or len(s)>4:
                    Is6 = False
                    return "Neither"
                for c in s:
                    if not c.isdigit():
                        if ord('a')<=ord(c)<=ord('f') or ord('A')<=ord(c)<=ord('F'):
                            continue
                        else:
                            return "Neither"
            if Is6:
                return "IPv6"