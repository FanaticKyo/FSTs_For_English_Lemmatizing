#!/usr/bin/python
# -*- coding: UTF-8 -*-

from fststr import fststr
import pywrapfst as fst

class Lemmatizer:
    def e_insertion():
        st = fststr.symbols_table_from_alphabet(fststr.EN_SYMB)
        compiler = fst.Compiler(isymbols=st, osymbols=st, keep_isymbols=True, keep_osymbols=True)
        fst_file = open('e-insertion.txt').read()
        print(fst_file, file=compiler)
        c = compiler.compile()
        fststr.expand_other_symbols(c)
        return c

    def k_insertion():
        st = fststr.symbols_table_from_alphabet(fststr.EN_SYMB)
        compiler = fst.Compiler(isymbols=st, osymbols=st, keep_isymbols=True, keep_osymbols=True)
        fst_file = open('k-insertion.txt').read()
        print(fst_file, file=compiler)
        c = compiler.compile()
        fststr.expand_other_symbols(c)
        return c

    def get_morphotactics():
        suffix = ['', 's', 'ed', 'en', 'ing']
        st = fststr.symbols_table_from_alphabet(fststr.EN_SYMB)
        compiler = fst.Compiler(isymbols=st, osymbols=st, keep_isymbols=True, keep_osymbols=True)
        c = compiler.compile()
        
        for s in suffix:
            compiler = fst.Compiler(isymbols=st, osymbols=st, keep_isymbols=True, keep_osymbols=True)
            compiler.write('0 0 <other> <other>\n')
            compiler.write('0 1 +Guess <^>\n')
            l = len(s)
            for i in range(l):
                compiler.write(str(i+1) + ' ' + str(i+2) + ' <epsilon> ' + s[i] + '\n')
            compiler.write(str(l+1) + ' ' + str(l+2) + ' <epsilon> <#>\n')
            compiler.write(str(l+2))
            suffix_rule = compiler.compile()
            c = c.union(suffix_rule)
        fststr.expand_other_symbols(c)
        return c

    def general():
        st = fststr.symbols_table_from_alphabet(fststr.EN_SYMB)
        compiler = fst.Compiler(isymbols=st, osymbols=st, keep_isymbols=True, keep_osymbols=True)
        compiler.write('0 0 <other> <other>\n')
        compiler.write('0 0 <#> <#>\n')
        compiler.write('0\n')
        # for special cases
        # compiler.write('0 1 i i\n')
        # compiler.write('1 2 n n\n')
        # compiler.write('2 3 g g\n')
        # compiler.write('3 4 <^> <^>\n')
        
        compiler.write('0 1 <^> <epsilon>\n')
        compiler.write('1 0 <other> <other>\n')
        compiler.write('1 0 <#> <#>\n')
        c = compiler.compile()
        fststr.expand_other_symbols(c)
        return c

    def e_deletion():
        st = fststr.symbols_table_from_alphabet(fststr.EN_SYMB)
        compiler = fst.Compiler(isymbols=st, osymbols=st, keep_isymbols=True, keep_osymbols=True)
        fst_file = open('silent-e-deletion.txt').read()
        print(fst_file, file=compiler)
        c = compiler.compile()
        fststr.expand_other_symbols(c)
        return c 

    def ch_sh_e_insertion():
        st = fststr.symbols_table_from_alphabet(fststr.EN_SYMB)
        compiler = fst.Compiler(isymbols=st, osymbols=st, keep_isymbols=True, keep_osymbols=True)
        fst_file = open('ch_sh_e_insertion.txt').read()
        print(fst_file, file=compiler)
        c = compiler.compile()
        fststr.expand_other_symbols(c)
        return c

    def y_replacement():
        st = fststr.symbols_table_from_alphabet(fststr.EN_SYMB)
        compiler = fst.Compiler(isymbols=st, osymbols=st, keep_isymbols=True, keep_osymbols=True)
        fst_file = open('y_replacement.txt').read()
        print(fst_file, file=compiler)
        c = compiler.compile()
        fststr.expand_other_symbols(c)
        return c

    def del_sharp():
        st = fststr.symbols_table_from_alphabet(fststr.EN_SYMB)
        compiler = fst.Compiler(isymbols=st, osymbols=st, keep_isymbols=True, keep_osymbols=True)
        compiler.write('0\n')
        compiler.write('0 0 <other> <other>\n')
        compiler.write('0 1 <#> <epsilon>\n')
        compiler.write('1\n')
        c = compiler.compile()
        fststr.expand_other_symbols(c)
        return c

    def consonant_doubling():
        st = fststr.symbols_table_from_alphabet(fststr.EN_SYMB)
        compiler = fst.Compiler(isymbols=st, osymbols=st, keep_isymbols=True, keep_osymbols=True)
        consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        vowel = ['a', 'e', 'i', 'o', 'u']
        compiler.write('0\n')
        compiler.write('0 0 <other> <other>\n')
        compiler.write('0 0 <#> <#>\n')
        for v in vowel:
            compiler.write('0 2 ' + v + ' ' + v + '\n')
        for c in consonant:
            compiler.write('0 1 ' + c + ' ' + c + '\n')
            compiler.write('1 1 ' + c + ' ' + c + '\n')
        for v in vowel:
            compiler.write('1 2 ' + v + ' ' + v + '\n')
        compiler.write('2 2 i i\n')
        compiler.write('2 2 u u\n')
        for i in range(len(consonant)):
            compiler.write('2 ' + str(i+3) + ' ' + consonant[i] + ' ' + consonant[i] + '\n')
            compiler.write(str(i+3) + ' ' + str(len(consonant)+3) + ' ' + '<^>' + ' ' + consonant[i] + '\n')
            compiler.write(str(i+3) + ' ' + str(len(consonant)+6) + ' ' + '<^>' + ' ' + consonant[i] + '\n')
            for c in consonant:
                compiler.write(str(i+3) + ' 1 ' + c + ' ' + c + '\n')
            for v in vowel:
                compiler.write(str(i+3) + ' 2 ' + v + ' ' + v + '\n')
        compiler.write(str(len(consonant)+3) + ' ' + str(len(consonant)+4) + ' e e' + '\n')
        compiler.write(str(len(consonant)+4) + ' ' + str(len(consonant)+5) + ' d d' + '\n')
        compiler.write(str(len(consonant)+5) + ' 0 <#> <#>' + '\n')
        compiler.write(str(len(consonant)+6) + ' ' + str(len(consonant)+7) + ' i i' + '\n')
        compiler.write(str(len(consonant)+7) + ' ' + str(len(consonant)+8) + ' n n' + '\n')
        compiler.write(str(len(consonant)+8) + ' ' + str(len(consonant)+5) + ' g g' + '\n')
        c = compiler.compile()
        fststr.expand_other_symbols(c)
        return c

    st = fststr.symbols_table_from_alphabet(fststr.EN_SYMB)

    lemma = []
    allomorphy = []

    with open("in_vocab_dictionary_verbs.txt", "r") as f:
        for line in f.readlines():
            lemma.append(line.split(',')[0])
            allomorphy.append(line.split(',')[1])

    compiler = fst.Compiler(isymbols=st, osymbols=st, keep_isymbols=True, keep_osymbols=True)
    rule = compiler.compile()

    for index in range(len(lemma)):
        compiler = fst.Compiler(isymbols=st, osymbols=st, keep_isymbols=True, keep_osymbols=True)
        if len(allomorphy[index]) >= len(lemma[index]):
            for i in range(len(allomorphy[index])):
                if i < len(lemma[index]):
                    compiler.write(str(i) + ' ' + str(i+1) + ' ' + allomorphy[index][i] + ' ' + lemma[index][i] + '\n')
                else:
                    compiler.write(str(i) + ' ' + str(i+1) + ' ' + allomorphy[index][i] + ' <epsilon>' + '\n')
            l = len(allomorphy[index])
            compiler.write(str(l) + ' ' + str(l+1) + ' <epsilon>' + ' +Known\n')
            compiler.write(str(l+1))
            rule.union(compiler.compile())
        else:
            for i in range(len(lemma[index])):
                if i < len(allomorphy[index]):
                    compiler.write(str(i) + ' ' + str(i+1) + ' ' + allomorphy[index][i] + ' ' + lemma[index][i] + '\n')
                else:
                    compiler.write(str(i) + ' ' + str(i+1) + ' <epsilon>' + ' ' + lemma[index][i] + '\n')
            l = len(lemma[index])
            compiler.write(str(l) + ' ' + str(l+1) + ' <epsilon>' + ' +Known\n')
            compiler.write(str(l+1))
            rule.union(compiler.compile())

    de_iv_rule = rule.copy().invert()

    morphotactics_rule = get_morphotactics()
    e_insertion_rule = e_insertion()
    k_insertion_rule = k_insertion()
    e_deletion_rule = e_deletion()
    general_rule = general()
    ch_sh_e_insertion_rule = ch_sh_e_insertion()
    y_replacement_rule = y_replacement()
    del_sharp_rule = del_sharp()
    consonant_doubling_rule = consonant_doubling()

    new_rule = k_insertion_rule.union(e_insertion_rule).union(general_rule).union(e_deletion_rule).union(ch_sh_e_insertion_rule).union(y_replacement_rule).union(consonant_doubling_rule)
    de_oov = fst.compose(morphotactics_rule.arcsort(sort_type="olabel"), new_rule.arcsort(sort_type="ilabel"))
    de_oov_rule = fst.compose(de_oov.arcsort(sort_type="olabel"), del_sharp_rule.arcsort(sort_type="ilabel"))
    
    oov_rule = de_oov_rule.copy().invert()
    # The final rules for lemmatizer
    rule = rule.union(oov_rule)
    # The final rules for delemmatizer
    de_rule = de_iv_rule.union(de_oov_rule)

    def lemmatize(self, in_str):
        
        out_set = set()
        for i in fststr.apply(in_str, self.rule):
            out_set.add(i)
        if in_str[-3:] == 'ing' or in_str[-2:] == 'ed' or in_str[-2:] == 'en' or (in_str[-1] == 's' and in_str[-2] != 's'):
            out_set.remove(in_str+'+Guess')
        
        return out_set

    def delemmatize(self, in_str):
        out_set = set()
        for i in fststr.apply(in_str, self.de_rule):
            out_set.add(i)
        return out_set