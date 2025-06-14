#task is to simulate a basic BLAST - like match using substring matching logic.
'''write a funtion find_matches(query: str,db:dict)->list that:
use membership operator;
takes a query DNa string and a dictonary of sequence Ids and sequences.
Returns a list of sequence IDs where the query is found as a substring.
Enter the query="ATGC"
["seq1","seq3"]'''
def find_matches(query: str, db: dict) -> list:
    matched_ids = []
    for seq_id, sequence in db.items():
        if query in sequence:
            matched_ids.append(seq_id)
    return matched_ids
db = {
    "seq001": "ATGCGGAATT",
    "seq002": "CGTACGTAGC",
    "seq003": "TTATGCATTA",
    "seq004": "GGAATCCGTA",
    "seq005": "CATGCCGTAGC",
    "seq006": "GGGCGTGCAT",
    "seq007": "AATGCTAGCTA",
    "seq008": "CGCGATGCGC",
    "seq009": "TATATATATA",
    "seq010": "ATGCGGATGCA"
}
query = "ATGC"
result = find_matches(query, db)
print(result)
