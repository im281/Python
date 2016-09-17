import ChemSpiderQuery
import TextFileUtilities



#c = ChemSpiderQuery.find('Dodecanoic Acid')
c = ChemSpiderQuery.find_one('Dodecanoic Acid')
print c
c = ChemSpiderQuery.Compound(3756)
print c.commonname
print c.monoisotopicmass
print c.commonname

t = TextFileUtilities.TextUtilities()
#file = "C:\Users\Iman\Desktop\Nist.txt"
#t.ChemSpiderSearchFile(file)
t.WriteTextFile('testing.txt')

