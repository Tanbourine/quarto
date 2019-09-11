
# Quarto Board Game

# To Do List
- [x] combine next piece
- [ ] error handling for when you type wrong number
- [ ] set player names
- [x] create piece definitions
- [ ] GUI app - kivy


# Piece definitions

|Property | True | False |
|------|-------|------|
|Color | White | Black|
|Shape | Circle | Square|
|Indent | Yes | None|
|Texture | Hatch | Smooth|

| Index | Binary | Shape | Color | Indent | Texture |
|----|------|--------|-------|------|--------|
| 0  | 0000 | Square | Black | None | Smooth |
| 1  | 0001 | Square | Black | None | Texture |
| 2  | 0010 | Square | Black | Yes | Smooth |
| 3  | 0011 | Square | Black | Yes | Texture |
| 4  | 0100 | Square | White |  None | Smooth |
| 5  | 0101 | Square | White |  None | Texture |
| 6  | 0110 | Square | White |  Yes | Smooth |
| 7  | 0111 | Square | White |  Yes | Texture |
| 8  | 1000 | Circle | Black | None | Smooth |
| 9  | 1001 | Circle | Black | None | Texture |
| 10 | 1010 | Circle | Black | Yes | Smooth |
| 11 | 1011 | Circle | Black | Yes | Texture |
| 12 | 1100 | Circle | White |  None | Smooth |
| 13 | 1101 | Circle | White |  None | Texture |
| 14 | 1110 | Circle | White |  Yes | Smooth |
| 15 | 1111 | Circle | White |  Yes | Texture |

