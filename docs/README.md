
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

## How functions work in files
### Circle
In the file circle.py there are 2 functions: The first area - it takes the radius of the circle and returns its area. The second perimeter - it takes the radius of the circle and returns its perimeter.
> Example of a call: radius = 1, pass it as an argument to the function, the result is area(1) => 3.14

### Square
In the file square.py There are 2 functions: The first area - it takes the sides of the shape and returns its area. The second perimeter - it takes the sides of the shape and returns its perimeter.
> Example of a call: there is a side a = 3, we pass it as an argument to the function, the result is a perimeter(3) => 12

### Triangle
In the file  triangle.py There are 2 functions: The first area - it takes the sides of the shape and return its area. The second perimeter - it takes the sides of the shape and return its perimeter.
>Example of a call: there is a side a = 3, b=4, c=5, we pass it as an argument to the function, the result is a perimeter(3,4,5) => 12

### How work Calculate
Example:
1. Enter figure name, avaliable are ['circle', 'square']: circle
2. Enter function name, avaliable are ['perimeter', 'area']: area
3. Input figure sizes separated by space, 1 for circle and square: 
**result - 78.53981633974483** 

### Project modification history
- 69980067b0e308e7b968a9f303a09d668cc5a519 - add info calculate.py
- 178d6f627d911fce2471969c1d28cacef4bd5fa1 - added info triangle.py
- d4615e286405326bb4756a6a48af5774cf15f79 - added info squaere.py
- addfd492b7438372abb280fc6c18eb7961b5586e - added info circle.py