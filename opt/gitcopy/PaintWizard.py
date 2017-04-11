# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 12:08:03 2017

@author: Administrator
"""
#PAINT WIZARD OOP

import math

unknown_size_of_room = True
while(unknown_size_of_room):
    #try function to ensure the input is an integer greater than 0
    try:
        roomsize = int(input("What is the size of the room?: "))
        if (roomsize > 0):
            unknown_size_of_room = False
        else:
            print("This is not a valid room size.")
    except (ValueError):
        print("This is not a valid room size.")

class Paint():
    #defining the input parameters of a class called Paint
    def __init__(self, size, price, coverage, brand):
        self.size = size
        self.price = price
        self.coverage = coverage
        self.brand = brand
    
    def coverage_per_tin(self):
        covg = self.size * self.coverage #area of wall covered per tin of paint
        return covg
        
    def tins_required(self):
        tins = roomsize / self.coverage_per_tin()
        return tins
        
    def full_tins_required(self):
        fulltins = math.ceil(self.tins_required()) #rounds up number of tins to integer
        return fulltins
        
    def cost_of_paint(self):
        #All print statements in this final method to avoid duplitcation in output
        covg = self.coverage_per_tin()
        print(self.brand, "covers", str(covg) + "m^2 per tin.")
        tins = self.tins_required()
        fulltins = self.full_tins_required()
        longcost = fulltins * self.price
        cost = round(longcost, 2)
        print("This room requires", str(fulltins), "tins of", self.brand + \
        ", which will cost £" + str(cost) + ".")
        if (tins == fulltins):
            sparePaint = 0
            print("There would be no paint left over.")
            return [cost, sparePaint]
        else:
            fullSparePaint = (fulltins - tins) * self.size
            sparePaint = round(fullSparePaint, 2)
            print("There would be", sparePaint, "litres of", self.brand, "paint wasted.")
            return [cost, sparePaint]
        #self.assertGreaterEqual(fulltins, tins)
            
def cheapest_option():
    resultList = []
    resultList.append(cheapoMax.cost_of_paint()) #CALLING FUNCTIONS
    resultList.append(averageJoes.cost_of_paint()) #CALLING FUNCTIONS
    resultList.append(duluxourousPaints.cost_of_paint()) #CALLING FUNCTIONS
#Price comparison    
    if (resultList[0][0] < resultList[1][0] and resultList[0][0] < resultList[2][0]):
        print("CheapoMax is the cheapest option.")
    elif (resultList[1][0] < resultList[0][0] and resultList[1][0] < resultList[2][0]):
        print("AverageJoes is the cheapest option.")
    else:
        print("DuluxourousPaints is the cheapest option.")
#Wastage comparison
    if (resultList[0][1] < resultList[1][1] and resultList[0][1] < resultList[2][1]):
        print("CheapoMax is the most efficient option.")
    elif (resultList[1][1] < resultList[0][1] and resultList[1][1] < resultList[2][1]):
        print("AverageJoes is the most efficient option.")
    elif (resultList[2][1] < resultList[0][1] and resultList[2][1] < resultList[1][1]):
        print("DuluxourousPaints is the most efficient option.")
    elif (resultList[0][1] == resultList[1][1] and resultList[0][1] < resultList[2][1]):
        print("CheapoMax and AverageJoes are equally efficient.")
    elif (resultList[0][1] == resultList[2][1] and resultList[0][1] < resultList[1][1]):
        print("CheapoMax and DuluxourousPaints are equally efficient.")
    elif (resultList[1][1] == resultList[2][1] and resultList[1][1] < resultList[0][1]):
        print("AverageJoes and DuluxourousPaints are equally efficient.")
    elif (resultList[1][1] == resultList[0][1] and resultList[1][1] == resultList[2][1]):
        print("All paint brands are equally efficient.")
#Add the actual cost/wastage values to the printed statements?        
        
        
cheapoMax = Paint(20, 19.99, 10, "CheapoMax")
averageJoes = Paint(15, 17.99, 11, "AverageJoes")
duluxourousPaints = Paint(10, 25.00, 20, "DuluxourousPaints")

#cheapoMax.tins_required()
#averageJoes.tins_required()
#duluxourousPaints.tins_required()

cheapest_option()