def is_valid_time(segment_info, observed_info):
    for i in range(7):
        if segment_info[i] == '1' and observed_info[i] == '0':
            return False
    return True

def get_possible_times(segment_info, observed_list):
    possible_times = []
    
    for h in range(24):
        for m in range(60):
            hour_str = str(h).zfill(2)
            minute_str = str(m).zfill(2)
            
            time_str = hour_str + minute_str
            time_info = []
            
            for digit in time_str:
                if digit == '0':
                    time_info.append('1111110')
                elif digit == '1':
                    time_info.append('0110000')
                elif digit == '2':
                    time_info.append('1101101')
                elif digit == '3':
                    time_info.append('1111001')
                elif digit == '4':
                    time_info.append('0110011')
                elif digit == '5':
                    time_info.append('1011011')
                elif digit == '6':
                    time_info.append('1011111')
                elif digit == '7':
                    time_info.append('1110000')
                elif digit == '8':
                    time_info.append('1111111')
                elif digit == '9':
                    time_info.append('1111011')
            
            valid = True
            for observed in observed_list:
                if not is_valid_time(segment_info, observed) or not is_valid_time(time_info, observed):
                    valid = False
                    break
            if valid:
                possible_times.append(time_str)
    
    return possible_times

# 입력 처리
segment_info = input().split()
T = int(input())

observed_list = []
for _ in range(T):
    observed_info = input().split()
    observed_list.append(observed_info)

# 가능한 시각 계산
possible_times = get_possible_times(segment_info, observed_list)

# 출력
print(len(possible_times))
for time in possible_times:
    print(time)
