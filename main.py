import os

print("\n[1/4] Detecting Shapes...")
os.system("python shape_detector.py")

print("\n[2/4] Understanding Scene...")
os.system("python scene_understanding.py")

print("\n[3/4] Generating Prompt...")
os.system("python prompt_generator.py")

print("\n[4/4] Generating AI Image...")
os.system("python generate_image.py")

print("\nDONE!")