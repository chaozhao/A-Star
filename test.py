#!/usr/bin/env python
class Player:
     def __init__(self, name):  # We will pass it a name in the class constructor (__init__)
        self.name = name  # this is the name we pass
        # self.lives = 3  # Player will have 3 lives initially. Use this initially without getter/setter
        self._lives = 3  # Use this with getter and setter. We hide lives attribute by prefixing it with underscore
        self.level = 1  # Player starts at level 1
        self.score = 0 # Player start with score 0
        
class NodeList:
    def __init__(self, value):
        self.value = value
        self.parent = []

    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    def appendChild(self, node):
        self.parent.append(node)

    def __iter__(self):
        return iter(self.parent)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

if __name__== "__main__":
    print("go")
    #p =Player("p1")
    #p.score = 1

    '''
    def updateGValues(self):
        aNode = self.startNode 
        for row in range(len(self.graph)):
            for column in range(len(self.graph[row])):
                if self.graph[row][column].get_walkable() == False:
                    self.graph[row][column].set_gValue(-1)
                else:
                    gValue = abs(row-aNode.getRow())+abs(column-aNode.getCol())
                    self.graph[row][column].set_gValue(gValue) 
                #print (self.graph[row][column].get_gValue(),end = '\t')
            #print('\n')
    
    def updateHValues(self):
        aNode = self.endNode
        for row in range(len(self.graph)):
            for column in range(len(self.graph[row])):
                if self.graph[row][column].get_walkable() == False:
                    self.graph[row][column].set_hValue(-2)
                else:
                    hValue = abs(row-aNode.getRow())+abs(column-aNode.getCol())
                    self.graph[row][column].set_hValue(hValue)
                #print (self.graph[row][column].get_hValue(),end = '\t')
            #print('\n')
    '''