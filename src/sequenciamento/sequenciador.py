from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# sequencia nucleotideo
s = Seq('ACTCCACTG')

print('\n')
print('sequencia normal - %s' % s)# sequencia normal
print('complementar - %s' % s.complement())# complementar
print('complementar reverso - %s ' % s.reverse_complement())# reverso complementar

'''
Transcribe

dna: ACTGCT
rna: ACUGCU
'''
print('\n')
dna = Seq('ACTGCT', IUPAC.unambiguous_dna)
print('DNA: %s' % dna)

rna = dna.transcribe()
print('RNA: %s' % rna)


'''
Translate
'''
print('\n')
rna = Seq('AUCUGGACUUAG', IUPAC.unambiguous_rna)
proteina = rna.translate()

print('rna: %s' % rna)
print('proteina: %s' % proteina)
print('\n')

dna = Seq('ACTGCTTAG', IUPAC.unambiguous_dna)
proteina2 = dna.translate()
print('dna: %s' % dna)
print('proteina: %s' % proteina2)