from Bio import Entrez
Entrez.email = "uehira.takumu.83z@st.kyoto-u.ac.jp"

handle = Entrez.einfo()
result = handle.read()
print (result)