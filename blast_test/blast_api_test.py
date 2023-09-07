from Bio.Blast import NCBIWWW
# 検索を起動する
# qblast (プログラム名、データベース名、検索キー)
result_handle = NCBIWWW.qblast ('blastn', 'nt', '8332116') 

# 検索結果を解釈する
from Bio.Blast import NCBIXML
blast_record = NCBIXML.read (result_handle)

E_VALUE_THRESH = 0.05
for alignment in blast_record.alignments: # 個々のアラインメントを表示
  for hsp in alignment.hsps: 
    if hsp.expect < E_VALUE_THRESH: # もしE-valueが基準 (0.05) より低いなら
      print ('***Alignment***')
      print ('Sequence:', alignment.title) 
      print ('Length:', alignment.length) # アラインメント長
      print ('E value:', hsp.expect) # E-value
      print (hsp.query[0:75] + '.......') # 問い合わせ配列
      print (hsp.match[0:75] + '.......') # マッチしたか
      print (hsp.sbjct[0:75] + '.......') # ヒットした配列