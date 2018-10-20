#!/usr/bin/env python

import random

class Node:
    def __init__(self,x=0,y=0,hValue=0,gValue=0,walkable=True):
        self._row = x
        self._col = y
        self.gValue = gValue
        self.hValue = hValue
        self.isWalkable = walkable
        self.up = None 

    @property
    def row(self): 
        return self._row
    @property
    def col(self):
        return self._col

    def get_gValue(self):
        return self.gValue
    def set_gValue(self,value):
        self.gValue = value
        
    def get_hValue(self):
        return self.hValue
    def set_hValue(self,value):
        self.hValue = value

    def get_fValue(self):
        if self.isWalkable == True:
            return self.hValue+self.gValue
        else:
            return 0

    def get_walkable(self):
        return self.isWalkable

    def set(self,x,y,gValue=0,hValue=0,walkable=True):
        self._row = x
        self._col = y
        self.hValue = gValue
        self.gValue = hValue
        self.isWalkable = walkable

    def setBlocked(self):
        self.isWalkable = False
        self.hValue = None
        self.gValue = None
        self.value = None

    def setParents(self,aNode):
        self.up =aNode


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

class Graph:
    def __init__(self,x,y,start,end):    
        self.graph = [[Node() for row in range(x)] for column in range(y)] 
        self.startNode = start
        self.endNode = end  
        for row in range(len(self.graph)):
            for column in range(len(self.graph[row])):
                self.graph[row][column]=Node(row,column)
        print ("this is a graph init")
    def setNode(self,aNode):
        x = aNode.row
        y = aNode.col
        self.graph[x][y]=aNode

    def printGraph(self):
        '''
        S for start node
        E for end node
        B for blocked node
        '''

        for row in range(len(self.graph)):
            for column in range(len(self.graph[row])):
                if row == self.startNode.row and column == self.startNode.col:
                    print('[S]', end = '\t')
                elif row == self.endNode.row and column == self.endNode.col:
                    print('[E]', end = '\t')
                elif self.graph[row][column].get_walkable() == True:
                    print(self.graph[row][column].get_fValue(), end = '\t')
                elif self.graph[row][column].get_walkable() == False:
                    print('[B]', end = '\t')
            print('\n')
        print ("================graph is printing================ \n")

    def getNeighborhood(self,aNode):
        x = aNode.row
        y = aNode.col
        nodeList = []
        if x-1 >= 0 and self.graph[x-1][y].get_walkable() == True:
            print("   up node(",x-1,y, ") append")
            upNode = self.graph[x-1][y]
            nodeList.append(upNode)
        if x+1 <= len(self.graph) and self.graph[x+1][y].get_walkable() == True :
            print(" down node(",x+1,y, ") append")
            downNode = self.graph[x+1][y]
            nodeList.append(downNode)
        if y-1 >= 0 and self.graph[x][y-1].get_walkable() == True:
            print(" left node(",x,y-1, ") append")
            leftNode = self.graph[x][y-1]
            nodeList.append(leftNode)
        if y+1 <= len(self.graph[0]) and self.graph[x][y+1].get_walkable() == True:
            print("right node(",x,y+1, ") append")
            rightNode = self.graph[x][y+1]
            nodeList.append(rightNode)
        return nodeList

def get_minfvalue(aList):
    min = openList[0].get_fValue()
    index = 0
    for i in range(len(openList)):
        if min > openList[i].get_fValue():
            min = openList[i].get_fValue()
            index = i
    
    aNode = openList[index]
    openList.pop(index)
    #print ("index is ",index)
    #print ("f value is ",aNode.get_fValue())
    return aNode

def calculateG(a,b):
    rowDistance = a.row - b.row
    colDistance = a.col - b.col
    gValue = abs(rowDistance)+abs(colDistance)
    return gValue

def calculateH(a,b):
    rowDistance = a.row - b.row
    colDistance = a.col - b.col
    hValue = abs(rowDistance)+abs(colDistance)
    return hValue

def updateValues(openList,startNode,endNode):
    for i in range(len(openList)):
        '''
        growDistance = startNode.row - openList[i].row
        gcolDistance = startNode.col - openList[i].col
        gValue = abs(growDistance)+abs(gcolDistance)
        hrowDistance = endNode.row - openList[i].row
        hcolDistance = endNode.col - openList[i].col
        hValue = abs(hrowDistance)+abs(hcolDistance)
        '''
        gValue = calculateG(startNode,openList[i])
        hValue = calculateH(endNode,openList[i])
        openList[i].set_gValue(gValue)
        openList[i].set_hValue(hValue)
if __name__== "__main__":

    print("Hello A star World!")
    #define graphy size
    GRAPH_ROW = 4 #index is (0 ~ 3)
    GRAPH_COLUMN = 6 #index is (0 ~ 5)

    #generate start node and end node
    startNode = Node(0,0)
    endNode = Node(3,5)

    #generate blocks
    b1 = Node(0,3,0,0,False)
    b2 = Node(1,3,0,0,False)
    b3 = Node(2,3,0,0,False)

    #openlist:going to visit list
    #closelist:visited list
    openList = []
    closeList = []
    closeList.append(startNode)

    g = Graph(GRAPH_COLUMN,GRAPH_ROW,startNode,endNode)
    ''' #configure blocked node
    g.setNode(b1)
    g.setNode(b2)
    g.setNode(b3)
    '''
    #end of configure all graph

    neighbourList = g.getNeighborhood(startNode)
    openList.extend(neighbourList)

    updateValues(openList,startNode,endNode)
    currentNode = get_minfvalue(openList)
    closeList.append(currentNode)
    
    '''while True:

        if currentNode == endNode:
            break
        #if end node is found then
        #break
    else:
        print('no path to end node')
    '''

    g.printGraph()
 

    