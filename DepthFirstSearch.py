__author__ = 'Juan Sebastian Salazar Aguirre'

## DEPTH FIRST SEARCH

## Linear Puzzle

## Import the necessary packages

from Tree import Nodo

## Define method to perform the search

def searchSolutionDFS(initialState, solution):

    solved = False
    visitedNodes = []
    edgeNodes = []
    initialNode = Nodo(initialState)
    edgeNodes.append(initialNode)

    while (not solved) and len(edgeNodes) != 0:

        ## Extract node and append it to visitedNodes

        node = edgeNodes.pop()
        visitedNodes.append(node)

        ## If the solution has been reached return it, else expand children nodes

        if node.getDatos() == solution:

            solved = True
            return node

        else:

            nodeData = node.getDatos()

            ## LEFT OPERATOR

            ## Left child has the left data truncated

            child = [nodeData[1], nodeData[0], nodeData[2], nodeData[3]]

            leftChild = Nodo(child)

            if not leftChild.isListed(visitedNodes) and not leftChild.isListed(edgeNodes):

                edgeNodes.append(leftChild)

            ## CENTRAL OPERATOR

            ## Central child has the central data truncated

            child = [nodeData[0], nodeData[2], nodeData[1], nodeData[3]]

            centralChild = Nodo(child)

            if not centralChild.isListed(visitedNodes) and not centralChild.isListed(edgeNodes):

                edgeNodes.append(centralChild)

            ## RIGHT CHILD

            ## Right child has the right data truncated

            child = [nodeData[0], nodeData[1], nodeData[3], nodeData[2]]

            rightChild = Nodo(child)

            if not rightChild.isListed(visitedNodes) and not rightChild.isListed(edgeNodes):

                edgeNodes.append(rightChild)

            ## SET CHILDREN

            node.setHijos([leftChild, centralChild, rightChild])

if __name__ == "__main__":

    initialState = [4, 2, 3, 1]
    solution = [1, 2, 3, 4]

    solutionNode = searchSolutionDFS(initialState, solution)

    ## Show result

    result = []
    node = solutionNode

    while node.getFather() != None:

        result.append(node.getDatos())
        node = node.getFather()

    result.append(initialState)
    result.reverse()
    print result

