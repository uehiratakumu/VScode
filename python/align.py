import numpy as np

def is_inside_existing_spheres(point, centers, radius):
    """指定された点が既存の球の中にあるかを確認する関数"""
    for center in centers:
        distance = np.linalg.norm(np.array(center) - np.array(point))
        if distance < 2 * radius:
            return True
    return False

def find_maximum_spheres(cube_size, radius, max_iterations=10000):
    """指定された立方体の中に最大数の球を配置する関数"""
    sphere_centers = []
    
    for _ in range(max_iterations):
        # 立方体の中にランダムに点を配置
        random_point = (np.random.randint(radius, cube_size - radius),
                        np.random.randint(radius, cube_size - radius),
                        np.random.randint(radius, cube_size - radius))
        
        # その点が既存の球の中にない場合、新しい球の中心として追加
        if not is_inside_existing_spheres(random_point, sphere_centers, radius):
            sphere_centers.append(random_point)
    
    return sphere_centers

# 10回繰り返して、配置可能な球の数が最大のものを選択
mesh =50
r =8
N = 50
num_centers = []
best_centers = []
best_count = 0
for _ in range(N):
    current_centers = find_maximum_spheres(mesh,r)
    if len(current_centers) > best_count:
        best_count = len(current_centers)
        best_centers = current_centers
    num_centers.append(len(best_centers))
print(len(best_centers))
print(best_centers)
