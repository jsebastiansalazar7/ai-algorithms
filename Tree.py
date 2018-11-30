__author__ = 'Juan Sebastian Salazar Aguirre'

## TREE STRUCTURE

## Definition of the class Nodo

class Nodo:

    ## Define constructor of the class
    ## It receives a data to store on a node and optionally a list of children

    def __init__(self, datos, hijos = None):

        self.datos = datos
        self.hijos = None
        self.padre = None
        self.coste = None
        self.setHijos(hijos)

    ## Define method to set children
    ## Assigns a list of children to the node

    def setHijos(self, hijos):

        self.hijos = hijos

        if self.hijos != None:

            for h in self.hijos:

                h.padre = self

    ## Define method to get children
    ## Returns a list with the children of the node

    def getHijos(self):

        return self.hijos

    ## Define method to get the father
    ## Returns the parent node

    def getFather(self):

        return self.padre

    ## Define method to set father
    ## Assigns the parent node of the current node

    def setPadre(self, padre):

        self.padre = padre

    ## Define method to set data
    ## Assigns a data to the current node

    def setDatos(self, datos):

        self.datos = datos

    ## Define method to get data
    ## Return the stored data of the node

    def getDatos(self):

        return self.datos

    ## Define method to set cost
    ## Define a weight for the node in the tree

    def setCoste(self, coste):

        self.coste = coste

    ## Define method to get cost
    ## Return the weight of the node in the tree

    def getCoste(self):

        return self.coste

    ## Define method

    def igual(self, nodo):

        if self.getDatos() == nodo.getDatos():

            return True

        else:

            return False

    ## Define method

    def isListed(self, listaNodos):

        Listed = False

        for n in listaNodos:

            if self.igual(n):

                Listed = True

        return Listed

    ## Define method

    def __str__(self):

        return str(self.getDatos())
