def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    is_left_of_center=params['is_left_of_center']
    abs_steering=params['steering_angle']
    steps=params['steps']
    speed = params['speed']
    progress=params['progress']

    
    temp_reward=0
    is_steering_penalty=0
    is_speed_penalty=0
    is_wheels_penalty=0
    is_max_speed_penalty=0

    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.5 * track_width
    marker_3 = 0.25 * track_width
    
    TOTAL_NUM_STEPS = 120
    P_STEERING_THRESHOLD = 20
    N_STEERING_THRESHOLD = -20
    MIN_SPEED_THRESHOLD = 1.4
    MAX_SPEED_THRESHOLD36 = 1.8

    def off_track():
        if all_wheels_on_track == False:
            is_wheels_penalty=1
        else:
            is_wheels_penalty=0
    
    def step_reward():
        if (steps % 40) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
            return 4.0
        else: 
            return 1e-3
    
    def left_side():
        if is_left_of_center == True:
            if distance_from_center <= marker_3:
                return 2.0
            else:
                return 1e-3
        else:
            return 1e-2
    
    def center_side():
        if distance_from_center <= marker_1:
            return 2.5
        else:
            return 1e-2
    
    def right_side():
        if is_left_of_center == False:
            if distance_from_center <= marker_3:
                return 2.5
            else:
                return 1e-2
        else:
            return 1e-2
    
    def speed_min():
        if speed <= MIN_SPEED_THRESHOLD:
            is_speed_penalty=1
        else:
            is_speed_penalty=0

    def speed_max():
        if speed >= MAX_SPEED_THRESHOLD36:
            is_max_speed_penalty=1
        else:
            is_max_speed_penalty=0
    
    def steering_penalty():
        if abs_steering > P_STEERING_THRESHOLD:
            is_steering_penalty=1
        elif abs_steering < N_STEERING_THRESHOLD:
            is_steering_penalty=1
        else:
            is_steering_penalty=0

    if progress <= 27:
        temp_reward = center_side()
        speed_min()
        steering_penalty()
        off_track()
        if is_speed_penalty==1:
           temp_reward = temp_reward*0.7
        if is_steering_penalty==1:
           temp_reward =temp_reward*0.6
        if is_wheels_penalty==1:
            temp_reward=temp_reward*0.5
        if is_wheels_penalty==0:
            temp_reward=temp_reward+1    
        return float(temp_reward)

    if progress <= 49:
        temp_reward = left_side()
        speed_min()
        speed_max()
        steering_penalty()
        off_track()
        temp_reward = temp_reward + step_reward()
        if is_speed_penalty==1:
           temp_reward = temp_reward*0.9
        if is_max_speed_penalty==1:
           temp_reward = temp_reward*0.8
        if is_steering_penalty==1:
           temp_reward =temp_reward*0.7
        if is_wheels_penalty==1:
           temp_reward =temp_reward*0.5
        if is_wheels_penalty==0:
           temp_reward =temp_reward+2.0
        return float(temp_reward)
       
    
    if progress <= 53:
        temp_reward = center_side()
        temp_reward = temp_reward + step_reward()
        speed_min()
        steering_penalty()
        off_track()
        if is_speed_penalty==1:
           temp_reward = temp_reward*0.9
        if is_steering_penalty==1:
           temp_reward =temp_reward*0.7
        if is_wheels_penalty==1:
           temp_reward =temp_reward*0.5
        if is_wheels_penalty==0:
           temp_reward =temp_reward+1
        return float(temp_reward)
    
    if progress <= 65:
        temp_reward = center_side()
        temp_reward = temp_reward + step_reward()
        speed_min()
        steering_penalty()
        off_track()
        if is_speed_penalty==1:
           temp_reward = temp_reward*0.9
        if is_steering_penalty==1:
           temp_reward =temp_reward*0.7
        if is_wheels_penalty==1:
           temp_reward =temp_reward*0.5
        if is_wheels_penalty==0:
           temp_reward =temp_reward+1
        return float(temp_reward)
    
    if progress <=100:
        temp_reward = left_side()
        temp_reward = temp_reward + step_reward()
        speed_min()
        steering_penalty()
        off_track()
        if is_speed_penalty==1:
           temp_reward = temp_reward*0.9
        if is_steering_penalty==1:
           temp_reward =temp_reward*0.7
        if is_wheels_penalty==1:
           temp_reward =temp_reward*0.5
        if is_wheels_penalty==0:
           temp_reward =temp_reward+1
        return float(temp_reward)
    
    temp_reward = 1e-3
    return float(temp_reward)
