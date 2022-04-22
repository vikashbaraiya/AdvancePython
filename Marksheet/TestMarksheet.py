import MarksheetBean
from MarksheetDao import *
import MarksheetDao
from MarksheetDao import *

def testAdd():
    mb = markSheetBean()

    mb.setName('abhi')
    #mb.setRollNo(1016)
    mb.setPhysics(34)
    mb.setChemistry(45)
    mb.setMaths(54)

    md = MarksheetDao()
    md.add(mb)

    print("----Data Inserted Successfully----")

def testUpdate():
    mb = markSheetBean()

    mb.setName('karan')
    mb.setRollNo(1016)
    mb.setPhysics(34)
    mb.setChemistry(45)
    mb.setMaths(54)

    md = MarksheetDao()
    md.update(mb)
    print("----Data Update Successfully----")


def testDelete():
    mb = markSheetBean()
    mb.setRollNo(1016)

    md = MarksheetDao()
    md.delete(mb)

    print("----Data Delete Successfully----")


def testRollNo():
    mb = markSheetBean()
    mb.setRollNo(1010)
    md = MarksheetDao()
    md.getRollNo(mb)




def testGetMeritList():
    md = MarksheetDao()
    md.getMeritList()

def testSearch():
    md = MarksheetDao()
    md.search()

def testNext():
    md = MarksheetDao()
    print(md.nextPk())


# ---OUTPUT---

testAdd()
#testUpdate()
#testRollNo()
#testDelete()
#testGetMeritList()
#testSearch()
#testNext()












