from Bio.Blast import Applications
cline = Applications.NcbimakeblastdbCommandline(input_file='test_0907', dbtype='nucl')
print(cline)
stdout, stderr = cline()
print(stdout)