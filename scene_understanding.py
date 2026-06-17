objects = []

with open("objects.txt", "r") as f:
    objects = [line.strip() for line in f]

scene = []

for obj in objects:

    if obj == "square":
        scene.append("house")

    elif obj == "unknown":
        scene.append("tree")

print("Scene:", scene)

with open("scene.txt", "w") as f:
    for item in scene:
        f.write(item + "\n")
        