# Extended Essay Fractals

For my International Baccalaureate Diploma Programme Extended Essay, I chose to write about how fractals are formed through iterated function systems and measured through the similarity and the Minkowski-Bouligand dimension methods. This repo will contain some of the fractals studied, which were generated through Python.

## Koch Curve

The Koch Curve is formed by taking four copies of the unit horizontal line segment, each scaled by 1/3.
Then, the 2nd of the 4 segments (from left to right) is rotated 60°mcounter-clockwise while the 3rd of the 4 segments is
rotated 60° clockwise. With more iterations towards the Koch Curve, the length of this curve increases. Hence, it is a fractal with infinite length. 

## Koch Snowflake

Some fractals can have the characteristic of being self-contacting, meaning that even when
more iterations occur, the fractal will not exceed a boundary that is intrinsic to the fractal and its conditions. This is closely tied to the special properties of most self-similar fractals: finite area and infinite
perimeter. An example of a fractal that clearly displays these properties is the Koch Snowflake, an enclosed figure
by three identical sides with the structure identical to that of Koch Curve’s. 

## Binary Tree

The Simple (Symmetric) Binary Tree is a more flexible type of fractal as it works for any angle θ where
0° < θ < 180° and any scaling factor S where 0 < S < 1. To generate the simplest version of this fractal, a vertical
line segment of length 1, or also called trunk, will split into two branches at the top that form an angle of θ with the
linear extension of the trunk (Riddler, 2022). For the first branches, each has length S. Following that, each of these
two branches split into two more branches (also called the second branches) with length S2. From this, a subtree is
formed at every branch.
<details>
<summary>
```
def tree(trunk, scaling, angle)
```
</summary>
```
branch = trunk * scaling
```

```
tree(branch, scaling, angle)
```
</details>
## Real (Randomized) Binary Tree

The IFS of the Binary Tree yields an image of a tree that does not look natural or realistic due to the consistency of the
values of the branch length, scaling factor S, and angle θ throughout the iterations. We can introduce variation by
inducing a random characteristic to each of these variables such as by adding or multiplying a random value to each
of the variables. As such, we may define the tree with another variable: randomness.
<details>

<summary>
```
def tree(trunk, scaling, angle, randomness)
```
</summary>

```
if randomness > 0:
    # adds variation to the length of the branch
    branch *= random.uniform(0.9, 1.1)
    # adds variation to angle by adding a random value in a set with mean = 0 and
standard dev = randomness
```
```
angle_left = angle + random.gauss(0, randomness)

angle_right = angle + random.gauss(0, randomness)
```
```
tree(branch, scaling, angle, randomness)
```
</details>