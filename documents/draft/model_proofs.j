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
15 ¬(P500∨P100),
16 (¬(P500∨P100))∧(Ra∨Rw)∧(Ssu∨Ssp),
17 (Ra∨Rw)∧(Ssu∨Ssp)→Swm∨Swl,
18 P500∨P100∨P50∨P20∨P0,
19 P500∨P100→Swl,
20 Swn∨Sws∨Swm∨Swl 
IS
SEQ ("→ intro"[A,B\16,1]) (cut[B,C\10,1]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\10,7]) (hyp[A\9])) (cut[B,C\8,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\15,8]) (hyp[A\14])) (cut[B,C\15,1]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\15,8]) (hyp[A\14])) (cut[B,C\2,1]) ("→ MT"[A,B\3,13]) (hyp[A\12]) (hyp[A\11]) (cut[B,C\7,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\10,7]) (hyp[A\9])) (cut[B,C\5,1]) ("∧ intro"[A,B\8,7]) (hyp[A\8]) (hyp[A\7]) (cut[B,C\4,1]) ("→ elim"[A,B\5,4]) (hyp[A\6]) (hyp[A\5]) ("∨ elim"[A,B,C\1,3,1]) (hyp[A\4]) (hyp[A\1]) (cut[B,C\0,1]) ("¬ elim"[B\3]) (hyp[A\3]) (hyp[A\2]) ("contra (constructive)"[B\1]) (hyp[A\0])
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
16 Ssu∨Ssp→¬Tm∧¬Tl,
17 Rt∧(Ssu∨Ssp)
IS
SEQ ("→ intro"[A,B\17,1]) (cut[B,C\14,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\11,14]) (hyp[A\13])) (cut[B,C\15,1]) ("→ elim"[A,B\14,15]) (hyp[A\16]) (hyp[A\14]) (cut[B,C\2,1]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\4,2]) (hyp[A\15])) (cut[B,C\4,1]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\4,2]) (hyp[A\15])) (cut[B,C\11,1]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\11,14]) (hyp[A\13])) (cut[B,C\6,1]) ("→ elim"[A,B\11,6]) (hyp[A\12]) (hyp[A\11]) ("∨ elim"[A,B,C\9,3,1]) (hyp[A\10]) ("∨ elim"[A,B,C\8,5,1]) (hyp[A\9]) ("∨ elim"[A,B,C\7,1,1]) (hyp[A\8]) (cut[B,C\0,1]) ("¬ elim"[B\7]) (hyp[A\7]) (hyp[A\6]) ("contra (constructive)"[B\1]) (hyp[A\0]) (hyp[A\1]) (cut[B,C\0,1]) ("¬ elim"[B\5]) (hyp[A\5]) (hyp[A\4]) ("contra (constructive)"[B\1]) (hyp[A\0]) (cut[B,C\0,1]) ("¬ elim"[B\3]) (hyp[A\3]) (hyp[A\2]) ("contra (constructive)"[B\1]) (hyp[A\0])
END
