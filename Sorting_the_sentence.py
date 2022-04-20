class Solution(object):
    def sortSentence(self, s):
        self.list = s.split(' ')
        for i in range(len(self.list)):
            for j in range(i,len(self.list)):
                if (self.list[j][-1] == str(i+1)):
                    self.list[i],self.list[j]= self.list[j],self.list[i]
        self.result = ''
        for i in range(len(self.list)):
            self.ind = self.list[i].split()
            for j in self.ind[0]:
                if (str(i+1) != j):
                    self.result +=j
            if ( i != len(self.list)-1):
                self.result+=' '
        self.result+=''
        return self.result 