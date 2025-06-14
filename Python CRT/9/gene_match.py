# ID: geneA| MATCH: 80% |status: Good match
db = {
#key : value
  "ATGT": "geneA",  # 3/4 = 75%
  "ATGC": "geneB",  # 4/4 = 100%
  "TTAC": "geneC",  # 1/4 = 25%
  "ATGG": "geneD",  # 3/4 = 75%
  "ATCC": "geneE",  # 3/4 = 75%
  "AGGC": "geneF",  # 2/4 = 50%
  "GTGC": "geneG",  # 3/4 = 75%
  "TTGC": "geneH",  # 3/4 = 75%
}
#ID: geneA |match: 80% |status: good match
def generate_report(dna,db):
    Count_G=0
    Count_C=0
    if dna in db:
        ID=db[dna]
    for i in dna:
        Count_G=dna.count(i)
        Count_C=dna.count(i)
        GC_Count=(Count_G+Count_C)/len(dna)*100
        if(GC_Count>=80):
            status="Good Math"
        elif (GC_Count>=50 and GC_Count<80): 
            status="Moderate"
        else:
            status="Poor match" 
        print(f"ID:{ID}| Match:{GC_Count}%| status:{status}")  
sequence="ATGT"  
generate_report(sequence,db)