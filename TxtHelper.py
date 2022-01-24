from Signal import Signal

def readSignalFromTxt(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
    f.close
    
    file_length = len(lines)

    header = lines[file_length - 1]
    header = header.split(' ')

    lines.remove(lines[file_length - 1])
    
    samples = list(map(float, lines))
    name = header[1]
    measurmentTime = header[4]
    
    if len(header) > 6:
        warning = "(Podczas badania odpięto elektrodę! sygnał może być niepełny)"
    else:
        warning = ""

    signal = Signal(name, measurmentTime, warning, samples)
    return signal
        
