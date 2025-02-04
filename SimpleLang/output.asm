p DB 0
q DB 0
r DB 0
MOV p, 10
MOV q, 20
MOV r, p
CMP r, 30
JNZ END_IF
MOV r, r
END_IF: