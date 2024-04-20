import numpy as np

def distance_point_to_line(point_a, point_b, point_c):
    # Mengonversi titik ke vektor
    a = np.array(point_a)
    b = np.array(point_b)
    c = np.array(point_c)
    
    # Vektor AC dan AB
    ac = c - a
    ab = b - a
    
    # Proyeksi vektor AC ke vektor AB
    projection = np.dot(ac, ab) / np.dot(ab, ab) * ab
    
    # Vektor normal ke vektor AB
    normal_vector = ac - projection
    
    # Panjang vektor normal
    normal_length = np.linalg.norm(normal_vector)
    
    # Jarak minimum
    distance = normal_length
    
    return distance

# Contoh penggunaan
point_a = (1, 1, 1)
point_b = (2, 2, 2)
point_c = (6, 6, 6)

distance = distance_point_to_line(point_a, point_b, point_c)
print("Jarak minimum dari titik C ke garis AB adalah:", distance)
