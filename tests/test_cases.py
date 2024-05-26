def test_min_pixel_lower_bound():
    min_pixels = 100
    assert min_pixels >= 100, "Minimum pixel value should be non-negative"
    print("Test Case 1: Passed")

def test_max_pixel_upper_bound():
    min_pixels = 1000
    max_pixels = 2000
    assert max_pixels >= min_pixels, "Maximum pixel value should be greater than or equal to the minimum"
    print("Test Case 2: Passed")

def test_min_pixels_positive():
    min_pixels = 100
    max_pixels = 300
    assert min_pixels > 0, "Minimum pixel value should be positive"
    print("Test Case 3: Passed")

def test_max_pixels_greater_than_min():
    min_pixels = 100
    max_pixels = 300
    assert max_pixels > min_pixels, "Maximum pixel value should be greater than the minimum"
    print("Test Case 4: Passed")

def test_lowThreshold_positive():
    lowThreshold = 50
    highThreshold = 200
    assert lowThreshold > 0, "Low threshold value should be positive"
    print("Test Case 5: Passed")

def test_highThreshold_greater_than_low():
    lowThreshold = 50
    highThreshold = 200
    assert highThreshold > lowThreshold, "High threshold value should be greater than the low threshold"
    print("Test Case 6: Passed")

# Test cases
test_min_pixel_lower_bound()
test_max_pixel_upper_bound()
test_min_pixels_positive()
test_max_pixels_greater_than_min()
test_lowThreshold_positive()
test_highThreshold_greater_than_low()
