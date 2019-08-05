# persian.txts

This project uses machine learning to treat Persian texts.

### Main objective

Given [two parallel lists](https://github.com/skaivolas/ft.lines), of Persian words written with two defective graphic systems (Perso-Arabic, Cyrillic), produce a procedure transforming pure Perso-Arabic or pure Cyrillic texts into full phonemic form. 

Perso-Arabic graphic system throws away several vowels, confounds vowels with consonants, but distinguishes etymologically different  consonants, even if they are pronounced in the same way.

Cyrillic system holds the vowels (though in a deformed manner), but fails to conserve etymological difference of the consonants.

### Example

Given the variants “پری گرفته” [translit. pry-grfth]  and “паригирифта” [translit. parigirifta], reconstitute “pari-gerefte”.

### Approximative mathematical model

Given two projections of a high-dimensional sequentive object with correlations between dimensions, describe the complete object.

## 1 Cleaning the data

The data available in [1](https://github.com/skaivolas/ft.lines) is contained in vector pdf files with extractable text. Nevertheless, the nontrivial 4-column layout and RTL-LTR toggles produce a randomly ordered text. One solution to that is to manually slice down the pdf files to enforce the order. File `OCR-fragmentation.py` slices columns into line structures.

Using bitmap approximation of the files, we calculate for every column (folder `columns`): positions and sizes of the blanks between lines, merge too narrow ones (otherwise they dismember verticalwise discontinuous letters) and produce a bash file with instructions  to slice *vector* pdfs. THus we obtain ~48000 files (folder `lines`) with only one line in each, with extractable text.
