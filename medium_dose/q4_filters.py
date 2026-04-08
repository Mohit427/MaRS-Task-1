def read_data(file_path):#Function to read and understanding the data from a given file path
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(float(line))
    return data

def muchiko_filter(data, window_size):#Muchiko Filter is the filter that means up the data for a given window size and stores it...
    result = []
    for i in range(len(data) - window_size + 1):
        window = data[i : i + window_size]
        mean = sum(window) / window_size
        result.append(round(mean, 2))
    return result

def sanchiko_filter(data, window_size):#Sanchiko Filter is the filter that finds the median of data for a given window size and stores it...
    result = []
    for i in range(len(data) - window_size + 1):
        window = sorted(data[i : i + window_size])
        mid = window_size // 2
        if window_size % 2 == 1:
            median = window[mid]
        else:
            median = (window[mid - 1] + window[mid]) / 2
        result.append(median)
    return result

def hybrid_filter(data, window_size):#Hybrid filter uses both the given filters to achive the said task
    after_sanchiko = sanchiko_filter(data, window_size)
    after_muchiko  = muchiko_filter(after_sanchiko, window_size)
    return after_muchiko

def conclude(original, muchiko, sanchiko, hybrid):#Concluding Which of the filters has the best variance(lower the better)
    def variance(data):
        mean = sum(data) / len(data)
        return sum((x - mean) ** 2 for x in data) / len(data)

    v_original = variance(original)
    v_muchiko  = variance(muchiko)
    v_sanchiko = variance(sanchiko)
    v_hybrid   = variance(hybrid)

    print("\n── Variance Comparison (lower = more stable) ──")
    print(f"Original  : {v_original:.2f}")
    print(f"Muchiko   : {v_muchiko:.2f}")
    print(f"Sanchiko  : {v_sanchiko:.2f}")
    print(f"Hybrid    : {v_hybrid:.2f}")

    best = min(v_muchiko, v_sanchiko, v_hybrid)
    if best == v_hybrid:
        print("\nConclusion: Hybrid filter performs best!")
    elif best == v_sanchiko:
        print("\nConclusion: Sanchiko filter performs best!")
    else:
        print("\nConclusion: Muchiko filter performs best!")

if __name__ == "__main__":
    file_path   = "log.txt"#Assuming that the Data is stored in log.txt in the parent directory itself
    window_size = int (input("Enter Window Size"))

    data = read_data(file_path)#Calling all the required functions
    print(f"Original data   : {data}")

    muchiko  = muchiko_filter(data, window_size)
    sanchiko = sanchiko_filter(data, window_size)
    hybrid   = hybrid_filter(data, window_size)

    print(f"\nMuchiko  output : {muchiko}")
    print(f"Sanchiko output : {sanchiko}")
    print(f"Hybrid   output : {hybrid}")

    conclude(data, muchiko, sanchiko, hybrid)