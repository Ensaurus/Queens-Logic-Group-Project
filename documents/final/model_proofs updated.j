CONJECTUREPANEL Conjectures
PROOF "Swn∨Sws∨Swm∨Swl, P500∨P100∨P50∨P20∨P0, P500∨P100→Swl, Swl→P500∨P100, (Ra∨Rw)∧(Ssu∨Ssp)→Swm∨Swl ⊢ (¬(P500∨P100))∧(Ra∨Rw)∧(Ssu∨Ssp)→Swm"
INFER Swn∨Sws∨Swm∨Swl,
     P500∨P100∨P50∨P20∨P0,
     P500∨P100→Swl,
     Swl→P500∨P100,
     (Ra∨Rw)∧(Ssu∨Ssp)→Swm∨Swl 
     ⊢ (¬(P500∨P100))∧(Ra∨Rw)∧(Ssu∨Ssp)→Swm 
FORMULAE
0 ⊥,
1 Swm,
2 ¬Swl,
3 Swl,
4 Swm∨Swl,
5 (Ra∨Rw)∧(Ssu∨Ssp),
6 (Ra∨Rw)∧(Ssu∨Ssp)→Swm∨Swl,
7 Ssu∨Ssp,
8 Ra∨Rw,
9 (¬(P500∨P100))∧(Ra∨Rw)∧(Ssu∨Ssp),
10 (¬(P500∨P100))∧(Ra∨Rw),
11 ¬(P500∨P100),
12 Swl→P500∨P100,
13 P500∨P100,
14 ¬(P500∨P100)∧(Ra∨Rw),
15 P500∨P100∨P50∨P20∨P0,
16 P500∨P100→Swl,
17 Swn∨Sws∨Swm∨Swl 
IS
SEQ ("→ intro"[A,B\9,1]) (cut[B,C\10,1]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\10,7]) (hyp[A\9])) (cut[B,C\8,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\11,8]) (hyp[A\14])) (cut[B,C\11,1]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\11,8]) (hyp[A\14])) (cut[B,C\2,1]) ("→ MT"[A,B\3,13]) (hyp[A\12]) (hyp[A\11]) (cut[B,C\7,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\10,7]) (hyp[A\9])) (cut[B,C\5,1]) ("∧ intro"[A,B\8,7]) (hyp[A\8]) (hyp[A\7]) (cut[B,C\4,1]) ("→ elim"[A,B\5,4]) (hyp[A\6]) (hyp[A\5]) ("∨ elim"[A,B,C\1,3,1]) (hyp[A\4]) (hyp[A\1]) (cut[B,C\0,1]) ("¬ elim"[B\3]) (hyp[A\3]) (hyp[A\2]) ("contra (constructive)"[B\1]) (hyp[A\0])
END
CONJECTUREPANEL Conjectures
PROOF "¬((P500∧P100)∨(P500∧P50)∨(P500∧P20)∨(P500∧P0)∨(P100∧P50)∨(P100∧P20)∨(P100∧P0)∨(P50∧P20)∨(P50∧P0)∨(P20∧P0)), ¬((Ssu∧Ssp)∨(Ssu∧Sf)∨(Ssu∧Sw)∨(Ssp∧Sf)∨(Ssp∧Sw)∨(Sf∧Sw)), (Sw∧(P500∨P100))∨(Rw∧¬(P20∨P0)∧¬Ssu)→Bl, Bl→(Sw∧(P500∨P100))∨(Rw∧¬(P20∨P0)∧¬Ssu) ⊢ ((Rw∧P50∧Ssp)→Bl)∧((Ra∧P100∧Ssu)→¬Bl)"
INFER ¬((P500∧P100)∨(P500∧P50)∨(P500∧P20)∨(P500∧P0)∨(P100∧P50)∨(P100∧P20)∨(P100∧P0)∨(P50∧P20)∨(P50∧P0)∨(P20∧P0)),
     ¬((Ssu∧Ssp)∨(Ssu∧Sf)∨(Ssu∧Sw)∨(Ssp∧Sf)∨(Ssp∧Sw)∨(Sf∧Sw)),
     (Sw∧(P500∨P100))∨(Rw∧¬(P20∨P0)∧¬Ssu)→Bl,
     Bl→(Sw∧(P500∨P100))∨(Rw∧¬(P20∨P0)∧¬Ssu)
     ⊢ ((Rw∧P50∧Ssp)→Bl)∧((Ra∧P100∧Ssu)→¬Bl)
FORMULAE
0 (Ra∧P100∧Ssu)→¬Bl,
1 (Rw∧P50∧Ssp)→Bl,
2 ⊥,
3 ¬Ssu,
4 Ssu,
5 Rw∧¬(P20∨P0)∧¬Ssu,
6 Rw∧¬(P20∨P0),
7 ¬((Ssu∧Ssp)∨(Ssu∧Sf)∨(Ssu∧Sw)∨(Ssp∧Sf)∨(Ssp∧Sw)∨(Sf∧Sw)),
8 (Ssu∧Ssp)∨(Ssu∧Sf)∨(Ssu∧Sw)∨(Ssp∧Sf)∨(Ssp∧Sw)∨(Sf∧Sw),
9 (Ssu∧Ssp)∨(Ssu∧Sf)∨(Ssu∧Sw)∨(Ssp∧Sf)∨(Ssp∧Sw),
10 Sf∧Sw,
11 (Ssu∧Ssp)∨(Ssu∧Sf)∨(Ssu∧Sw)∨(Ssp∧Sf),
12 Ssp∧Sw,
13 (Ssu∧Ssp)∨(Ssu∧Sf)∨(Ssu∧Sw),
14 Ssp∧Sf,
15 Ssu∧Sw,
16 (Ssu∧Ssp)∨(Ssu∧Sf),
17 Sw,
18 Sw∧(P500∨P100),
19 P500∨P100,
20 Sw∧(P500∨P100)∨Rw∧¬(P20∨P0)∧¬Ssu,
21 Sw∧(P500∨P100),
22 Bl,
23 Bl→(Sw∧(P500∨P100))∨(Rw∧¬(P20∨P0)∧¬Ssu),
24 (Sw∧(P500∨P100))∨(Rw∧¬(P20∨P0)∧¬Ssu),
25 Ra∧P100∧Ssu,
26 Ra∧P100,
27 ¬Bl,
28 Ra,
29 P100,
30 ((Rw∧P50∧Ssp)→Bl)∧((Ra∧P100∧Ssu)→¬Bl),
31 (Sw∧(P500∨P100))∨(Rw∧¬(P20∨P0)∧¬Ssu)→Bl,
32 Ssu∧Ssp,
33 Ssu∧Sf,
34 Ssp,
35 ¬(P20∨P0),
36 Rw,
37 ¬((P500∧P100)∨(P500∧P50)∨(P500∧P20)∨(P500∧P0)∨(P100∧P50)∨(P100∧P20)∨(P100∧P0)∨(P50∧P20)∨(P50∧P0)∨(P20∧P0)),
38 (P500∧P100)∨(P500∧P50)∨(P500∧P20)∨(P500∧P0)∨(P100∧P50)∨(P100∧P20)∨(P100∧P0)∨(P50∧P20)∨(P50∧P0)∨(P20∧P0),
39 (P500∧P100)∨(P500∧P50)∨(P500∧P20)∨(P500∧P0)∨(P100∧P50)∨(P100∧P20)∨(P100∧P0)∨(P50∧P20)∨(P50∧P0),
40 P20∧P0,
41 P50∧P0,
42 (P500∧P100)∨(P500∧P50)∨(P500∧P20)∨(P500∧P0)∨(P100∧P50)∨(P100∧P20)∨(P100∧P0)∨(P50∧P20),
43 P0,
44 P50,
45 P50∧P20,
46 (P500∧P100)∨(P500∧P50)∨(P500∧P20)∨(P500∧P0)∨(P100∧P50)∨(P100∧P20)∨(P100∧P0),
47 P20,
48 P20∨P0,
49 Rw∧P50∧Ssp,
50 Rw∧P50,
51 ¬((Ssu∧Ssp)∨(Ssu∧Sf)∨(Ssu∧Sw)∨(Ssp∧Sf)∨(Ssp∧Sw)∨(Sf∧Sw)),
52 ¬((P500∧P100)∨(P500∧P50)∨(P500∧P20)∨(P500∧P0)∨(P100∧P50)∨(P100∧P20)∨(P100∧P0)∨(P50∧P20)∨(P50∧P0)∨(P20∧P0))
IS
SEQ (cut[B,C\1,30]) ("→ intro"[A,B\49,22]) (cut[B,C\50,22]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\50,34]) (hyp[A\49])) (cut[B,C\36,22]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\36,44]) (hyp[A\50])) (cut[B,C\44,22]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\36,44]) (hyp[A\50])) (cut[B,C\34,22]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\50,34]) (hyp[A\49])) (cut[B,C\35,22]) ("¬ intro"[A\48]) ("∨ elim"[A,B,C\47,43,2]) (hyp[A\48]) (cut[B,C\45,2]) ("∧ intro"[A,B\44,47]) (hyp[A\44]) (hyp[A\47]) (cut[B,C\42,2]) (LAYOUT "∨ intro" (0) ("∨ intro(R)"[B,A\46,45]) (hyp[A\45])) (cut[B,C\39,2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\41,42]) (hyp[A\42])) (cut[B,C\38,2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\40,39]) (hyp[A\39])) (cut[B,C\2,2]) ("¬ elim"[B\38]) (hyp[A\38]) (hyp[A\37]) (hyp[A\2]) (cut[B,C\41,2]) ("∧ intro"[A,B\44,43]) (hyp[A\44]) (hyp[A\43]) (cut[B,C\39,2]) (LAYOUT "∨ intro" (0) ("∨ intro(R)"[B,A\42,41]) (hyp[A\41])) (cut[B,C\38,2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\40,39]) (hyp[A\39])) (cut[B,C\2,2]) ("¬ elim"[B\38]) (hyp[A\38]) (hyp[A\37]) (hyp[A\2]) (cut[B,C\6,22]) ("∧ intro"[A,B\36,35]) (hyp[A\36]) (hyp[A\35]) (cut[B,C\3,22]) ("¬ intro"[A\4]) (cut[B,C\32,2]) ("∧ intro"[A,B\4,34]) (hyp[A\4]) (hyp[A\34]) (cut[B,C\16,2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\33,32]) (hyp[A\32])) (cut[B,C\13,2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\15,16]) (hyp[A\16])) (cut[B,C\11,2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\14,13]) (hyp[A\13])) (cut[B,C\9,2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\12,11]) (hyp[A\11])) (cut[B,C\8,2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\10,9]) (hyp[A\9])) (cut[B,C\2,2]) ("¬ elim"[B\8]) (hyp[A\8]) (hyp[A\7]) (hyp[A\2]) (cut[B,C\5,22]) ("∧ intro"[A,B\6,3]) (hyp[A\6]) (hyp[A\3]) (cut[B,C\24,22]) (LAYOUT "∨ intro" (0) ("∨ intro(R)"[B,A\21,5]) (hyp[A\5])) (cut[B,C\22,22]) ("→ elim"[A,B\24,22]) (hyp[A\31]) (hyp[A\24]) (hyp[A\22]) (cut[B,C\0,30]) ("→ intro"[A,B\25,27]) (cut[B,C\26,27]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\26,4]) (hyp[A\25])) (cut[B,C\28,27]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\28,29]) (hyp[A\26])) (cut[B,C\29,27]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\28,29]) (hyp[A\26])) (cut[B,C\4,27]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\26,4]) (hyp[A\25])) ("¬ intro"[A\22]) (cut[B,C\24,2]) ("→ elim"[A,B\22,24]) (hyp[A\23]) (hyp[A\22]) ("∨ elim"[A,B,C\21,5,2]) (hyp[A\20]) (cut[B,C\17,2]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\17,19]) (hyp[A\18])) (cut[B,C\15,2]) ("∧ intro"[A,B\4,17]) (hyp[A\4]) (hyp[A\17]) (cut[B,C\13,2]) (LAYOUT "∨ intro" (0) ("∨ intro(R)"[B,A\16,15]) (hyp[A\15])) (cut[B,C\11,2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\14,13]) (hyp[A\13])) (cut[B,C\9,2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\12,11]) (hyp[A\11])) (cut[B,C\8,2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\10,9]) (hyp[A\9])) (cut[B,C\2,2]) ("¬ elim"[B\8]) (hyp[A\8]) (hyp[A\7]) (hyp[A\2]) (cut[B,C\3,2]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\6,3]) (hyp[A\5])) (cut[B,C\4,2]) (hyp[A\4]) (cut[B,C\2,2]) ("¬ elim"[B\4]) (hyp[A\4]) (hyp[A\3]) (hyp[A\2]) ("∧ intro"[A,B\1,0]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Conjectures
PROOF "Rt→¬Tn, Ssu∨Ssp→¬Tm∧¬Tl, Tn∨Ts∨Tm∨Tl ⊢ Rt∧(Ssu∨Ssp)→Ts"
INFER Rt→¬Tn,
     Ssu∨Ssp→¬Tm∧¬Tl,
     Tn∨Ts∨Tm∨Tl 
     ⊢ Rt∧(Ssu∨Ssp)→Ts 
FORMULAE
0 ⊥,
1 Ts,
2 ¬Tl,
3 Tl,
4 ¬Tm,
5 Tm,
6 ¬Tn,
7 Tn,
8 Tn∨Ts,
9 Tn∨Ts∨Tm,
10 Tn∨Ts∨Tm∨Tl,
11 Rt,
12 Rt→¬Tn,
13 Rt∧(Ssu∨Ssp),
14 Ssu∨Ssp,
15 ¬Tm∧¬Tl,
16 Ssu∨Ssp→¬Tm∧¬Tl 
IS
SEQ ("→ intro"[A,B\13,1]) (cut[B,C\14,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\11,14]) (hyp[A\13])) (cut[B,C\15,1]) ("→ elim"[A,B\14,15]) (hyp[A\16]) (hyp[A\14]) (cut[B,C\2,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\4,2]) (hyp[A\15])) (cut[B,C\4,1]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\4,2]) (hyp[A\15])) (cut[B,C\11,1]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\11,14]) (hyp[A\13])) (cut[B,C\6,1]) ("→ elim"[A,B\11,6]) (hyp[A\12]) (hyp[A\11]) ("∨ elim"[A,B,C\9,3,1]) (hyp[A\10]) ("∨ elim"[A,B,C\8,5,1]) (hyp[A\9]) ("∨ elim"[A,B,C\7,1,1]) (hyp[A\8]) (cut[B,C\0,1]) ("¬ elim"[B\7]) (hyp[A\7]) (hyp[A\6]) ("contra (constructive)"[B\1]) (hyp[A\0]) (hyp[A\1]) (cut[B,C\0,1]) ("¬ elim"[B\5]) (hyp[A\5]) (hyp[A\4]) ("contra (constructive)"[B\1]) (hyp[A\0]) (cut[B,C\0,1]) ("¬ elim"[B\3]) (hyp[A\3]) (hyp[A\2]) ("contra (constructive)"[B\1]) (hyp[A\0])
END
