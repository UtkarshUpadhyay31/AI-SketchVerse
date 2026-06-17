with open("scene.txt", "r") as f:
    objects = [line.strip() for line in f]

prompt = ""

if "house" in objects:
    prompt += "a beautiful countryside house, "

if "tree" in objects:
    prompt += "large green trees, "

prompt += """
photorealistic,
ultra detailed,
cinematic lighting,
high quality,
8k
"""

print(prompt)

with open("prompt.txt", "w") as f:
    f.write(prompt)