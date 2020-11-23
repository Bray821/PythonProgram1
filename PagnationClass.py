class Pagination:
    def __init__(self,items = [], pageSize = 10):
        self.items = items
        self.pageSize = pageSize
        self.totalPages = 0
        self.currentPage = 1
        self.dictonary = {1:[]}
        self.table = []
        counter = 1
        for section in self.items:
            self.dictonary[counter].append(section)
            if len(self.dictonary[counter])>= self.pageSize:
                counter += 1
                self.dictonary[counter] = []
    def getItems(self):
       return self.items
    def getPageSize(self):
        return self.pageSize
    def getCurrentPage(self):
        return self.currentPage
    def prevPage(self):
        if self.currentPage>1:
            self.currentPage += -1
        else:
            self.currentPage =1
    def nextPage(self):
        if self.currentPage<=len(self.items)//self.pageSize:
            self.currentPage+= 1
        else:
            self.currentPage = 1
    def firstPage(self):
        self.currentPage = 1
    def lastPage(self):
        self.currentPage = len(self.items)//self.pageSize
    def goToPage(self,num):
        if self.currentPage<=len(self.items)//self.pageSize:
            self.currentPage = num
    def getVisibleItems(self):
        return self.dictonary[self.currentPage]


alphababatize =list("abcdefghijklmnopqrs")

alpha = Pagination(alphababatize,None)
print(alpha.getCurrentPage())
print(alpha.getItems())
print(alpha.getVisibleItems())
