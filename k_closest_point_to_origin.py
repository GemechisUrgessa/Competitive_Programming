class Solution(object):
    def kClosest(self, points, k):
        self.result = {}
        self.arr = []
        for point in points:
            temp = point[0]**2 + point[1]**2
            if (temp in self.result):
                self.noneV = self.result[temp]
                self.result[temp].append(point)

            else:
                self.tempArr = []             
                self.tempArr.append(point)
                self.result[temp]  = self.tempArr
                self.arr.append(temp)
                self.tempArr=[]
        self.arr.sort()
        self.ans = []
        for result in self.arr:
            if(type(self.result[result][0]) != int):
                for i in self.result[result]:
                    self.ans.append(i)
                    if (len(self.ans)==k):
                        return self.ans
 