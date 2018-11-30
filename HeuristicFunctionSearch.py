__author__ = 'Juan Sebastian Salazar Aguirre'

## HEURISTIC FUNCTION SEARCH

## Linear Puzzle

## Import the necessary packages

from Tree import Nodo

def searchSolutionH(initialNode, solution, visitedNodes):

    visitedNodes.append(initialNode.getDatos())

    if initialNode.getDatos() == solution:

        return initialNode

    else:

        ## Expand children

        nodeData = initialNode.getDatos()

        ## LEFT OPERATOR

        ## Left child has the left data truncated

        child = [nodeData[1], nodeData[0], nodeData[2], nodeData[3]]

        leftChild = Nodo(child)

        ## CENTRAL OPERATOR

        ## Central child has the central data truncated

        child = [nodeData[0], nodeData[2], nodeData[1], nodeData[3]]

        centralChild = Nodo(child)

        ## RIGHT CHILD

        ## Right child has the right data truncated

        child = [nodeData[0], nodeData[1], nodeData[3], nodeData[2]]

        rightChild = Nodo(child)

        ## Set children nodes

        initialNode.setHijos([leftChild, centralChild, rightChild])

        ## Visit the children nodes

        for childNode in initialNode.getHijos():

            if not childNode.getDatos() in visitedNodes and improve(initialNode, childNode):

                ## Recursive call

                search = searchSolutionH(childNode, solution, visitedNodes)

                if search != None:

                    return search

    return None

def improve(parentNode, childNode):

    qualityParent = 0
    qualityChild = 0

    parentData = parentNode.getDatos()
    childData = childNode.getDatos()

    for n in range(1, len(parentData)):

        if (parentData[n] > parentData[n - 1]):

            qualityParent = qualityParent + 1

        if (childData[n] > childData[n - 1]):

            qualityChild = qualityChild + 1

    if qualityChild >= qualityParent:

        return True

    else:

        return False

if __name__ == "__main__":

    initialState = [4, 2, 3, 1]
    solution = [1, 2, 3, 4]

    solutionNode = None
    visitedNodes = []
    initialNode = Nodo(initialState)

    node = searchSolutionH(initialNode, solution, visitedNodes)

    ## Show result

    result = []

    while node.getFather() != None:

        result.append(node.getDatos())
        node = node.getFather()

    result.append(initialState)
    result.reverse()
    print result