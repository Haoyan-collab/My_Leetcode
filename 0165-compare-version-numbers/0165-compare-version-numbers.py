class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i,j = 0,0
        m = len(version1)
        n = len(version2)
        li,lj = 0,0
        while i<m or j<n:
            li,lj = i,j
            n1,n2 = 0,0
            while i<m and version1[i]!='.':
                n1 = n1*10 + int(version1[i])
                i += 1
            while j<n and version2[j]!='.':
                n2 = n2*10 + int(version2[j])
                j += 1
            if n1>n2:
                return 1
            elif n1<n2:
                return -1
            i += 1
            j += 1

        
        return 0