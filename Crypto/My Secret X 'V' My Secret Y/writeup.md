
## My Secret X 'V' My Secret Y
### Category: CRYPTO
### Points: 80
### Description
A message from the cheeky code gremlins: Our secrets are hidden in plain sight, like a magician’s trick. Your task? Play peekaboo with bytes to reveal what’s concealed. Remember, it’s not about where they're hiding but who’s hiding!"

Hide: 6866507f43181e1874531b79741f59187448791f517256
&
Seek: ??????????????

### Approach
As we are not provided with anything except that hex and flag format, the first thing we can think of is xoring with a key
in order to figure the key we xor the first char with 'C', the second one with 'M', seeing the answers we can guess the key is 43.
Thereby xoring every character with 43 gives us the flag.

#### Flag: CM{Th353_x0R_4r3_cR4zY}

