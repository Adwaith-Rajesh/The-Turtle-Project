# The Turtle Project

   Our school project

____

## Table of contents

- [Description](#description)
- [Usage](#usage)
- [External Packages](#third-party-packages)
- [License](#license)

____
____

## Description

The project is a part a school project with the theme art in programming (Literally). Where we are supposed make visual representation with coding

## Usage

To use the package all you have to do is to run the main file with the command.

```bash
python main.py
```

This will provide with a range of option that you can choose from.

## Using .cord file

The software supports a custom file type called the cord file(It does not use x, y co-ordinate system), with which you can draw figures and shapes.

The supports only these commands:

```text
f -> forward
b -> backward
r -> turn right
l -> turn left
u -> stop drawing(does all the commands shown above but does not draw)
d -> start draw
```

____

- ### Usage in file

```text

f=500
d=100
r=50
f=20
u=0
f=50
```

- ### Working

f=500 means move forward 500 pixels, d=100 means move backward 500 pixels, r=50 means turn right 50 degrees, u can have any value but it will stop drawing, since here the next command is to move forward 50, it will move forward 50 pixels but it will not draw on the screen. To start drawing again you need to use <b>d=0</b>.

## Third party packages

The project currently does not use any third party packages or libraries.

## License

[MIT](LICENSE)

## Authors

The entire project is done by:

- [Adwaith Rajesh](https://github.com/Adwaith-Rajesh)
- [Devadathan](https://github.com/Devadathan13)
