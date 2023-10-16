from A_V_calc import area_of_rectangle, volume_of_cylinder, area_of_triangle, volume_of_sphere, volume_of_cone

def test_area_of_rectangle():
    assert area_of_rectangle(2, 3) == (6, "m²")
    assert area_of_rectangle(5, 10) == (50, "m²")
    assert area_of_rectangle(7.5, 4.2) == (31.5, "m²")
    assert area_of_rectangle(-2, 3) == ("Invalid Input", "")
    assert area_of_rectangle(2, 0) == ("Invalid Input", "")

def test_volume_of_cylinder():
    assert volume_of_cylinder(1, 1) == (3.14, "m³")
    assert volume_of_cylinder(2, 3) == (37.70, "m³")
    assert volume_of_cylinder(3.5, 4.5) == (173.18, "m³")
    assert volume_of_cylinder(-1, 1) == ("Invalid Input", "")
    assert volume_of_cylinder(2, 0) == ("Invalid Input", "")


def test_area_of_triangle():
    assert area_of_triangle(2, 3) == (3, "m²")
    assert area_of_triangle(5, 10) == (25, "m²")
    assert area_of_triangle(7.5, 4.2) == (15.75, "m²")
    assert area_of_triangle(-2, 3) == ("Invalid Input", "")
    assert area_of_triangle(2, 0) == ("Invalid Input", "")

def test_volume_of_sphere():
    assert volume_of_sphere(1) == (4.19, "m³")
    assert volume_of_sphere(2) == (33.51, "m³")
    assert volume_of_sphere(3.5) == (179.59, "m³")
    assert volume_of_sphere(-1) == ("Invalid Input", "")
    assert volume_of_sphere(0) == ("Invalid Input", "")

def test_volume_of_cone():
    assert volume_of_cone(1, 1) == (1.05, "m³")
    assert volume_of_cone(2, 3) == (12.57, "m³")
    assert volume_of_cone(3.5, 4.5) == (57.73, "m³")
    assert volume_of_cone(-1, 1) == ("Invalid Input", "")
    assert volume_of_cone(2, 0) == ("Invalid Input", "")
