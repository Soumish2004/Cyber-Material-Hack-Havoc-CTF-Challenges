## Dear Trithemius
### Category: CRYPTO
### Points: 60
### Description
The encryption method used in this cipher is a variation of the Caesar cipher, but with a twist. Each letter in the plaintext is shifted by a different amount depending on its position in the string. Non-alphabetic characters remain unchanged. To decrypt, reverse this shifting process.

Flag: Enclosed string with CM{....}

### Approach
Going through the given code, we can figure out few things, like the `_` are not affected and all characters are affected based on their position, basically every character in the flag is replaced by next ith character in english alphabet, where i is the pos of the character, in case if it exceeds the range of A-Z, it starts back at A

The encrypted text is taken from the given .txt file.

#### Flag: CM{LOVE_U_TRITHEMIUS}

