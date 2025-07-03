def car_fleet(position, speed, target):
    # Sort cars by position (descending)
    cars = sorted(zip(position, speed), reverse=True)
    time_to_target = []
    for pos, sp in cars:
        time_to_target.append((target-pos)/sp)
    
    prev_time= 0
    fleets= 0

    for time in time_to_target:
        if time > prev_time: #fleet is only formed if a previous car can not catchup 
            fleets +=1
            prev_time = time
        
    return fleets










def read_test_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        target = int(lines[0].split('=')[1].strip())
        position = eval(lines[1].split('=')[1].strip())
        speed = eval(lines[2].split('=')[1].strip())
    return position, speed, target

if __name__ == "__main__":
    position, speed, target = read_test_input('test1.txt')
    fleets= car_fleet(position, speed, target)
    print(fleets)
