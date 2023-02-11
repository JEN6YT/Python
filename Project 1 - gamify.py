def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration

    global last_finished
    global bored_with_stars

    #points
    cur_hedons = 0
    cur_health = 0

    #stars
    cur_star = None
    global cur_star_activity
    cur_star_activity = None
    global star
    star = False
    global num_of_stars
    bored_with_stars = False

    #activity
    last_activity = None
    last_activity_duration = 0

    #time
    cur_time = 0

    last_finished = -1000


def tired():
  '''Check if the user is tired or not'''
  global last_activity, last_activity_duration
  if (last_activity == "resting" and last_activity_duration >= 120) or last_activity == None:
    return False
  else:
    return True

def star_can_be_taken(activity):
  '''
  Determine if the stars can be taken
  If the user is not bored with starts and a star is given and the current star activity is the current activity
  '''
  global cur_star_activity
  if bored_with_stars == False and star == True and cur_star_activity == activity:
    return True
  else:
    return False

def offer_star(activity):
  '''Offer stars to the user'''
  global cur_time, bored_with_stars
  global num_of_stars, star, a, cur_star_activity
  num_of_stars= 0
  # if the user does not have a star, we record the time the star is first given and add 1 to the number of starts
  if num_of_stars == 0:
    first_star_time = cur_time
    num_of_stars += 1
  # if the user is already given a star, then we increase the number of starts by 1
  else:
    num_of_stars += 1

  # if the number of stars exceeds three and the time duration between the current time and the time a star is first given, then the user is bored with stars and stars will not be given
  if num_of_stars >= 3 and cur_time - first_star_time <= 120:
    bored_with_stars = True
    star = False

  # if the user is offered a star, a star is given to the user
  star = True

  a = activity

  # the current star activity is equal to the current activity
  cur_star_activity = activity


def get_cur_hedons():

  return cur_hedons

def get_cur_health():

  return cur_health

def most_fun_activity_minute():
  '''Return the most_fun_activity'''
  global a,d
  # if a star is given, the most fun activity is the star activity
  if star == True:
    most_fun_activity = a
  # if a star is not given, the most fun activity is either running or resting
  if star == False:
    if (a == "running" and d<= 10) and tired() == False:
      most_fun_activity = "running"
    else:
      most_fun_activity = "resting"
  return most_fun_activity


def perform_activity(activity, duration):

  global a
  global d
  global cur_time
  a = activity
  d = duration
  cur_time += d

  #health pts
  global cur_health, last_activity, last_activity_duration
  global last_activity
  global last_activity_duration
  global cur_hedons, num_of_stars, bored_with_stars, star, cur_star_activity

  #health pts for running
  if a == "running":
    if last_activity != "running":
      if d <= 180:
        cur_health += 3 * d
      else:
        cur_health += 1 * (d-180) + (3 * 180)
    if last_activity == "running":
      cur_health += 3 * (180 - last_activity_duration) + 1 * (d + last_activity_duration - 180)
  #health pts for textbook
  elif a == "textbooks":
    cur_health += 2 * (d)

  #hedons
  if a == "resting":
    cur_hedons = cur_hedons
  else:
    if tired() == False :
      if a == 'resting':
        cur_hedons += 0
      elif a == "running":
        if d <= 10:
          cur_hedons += 2 * d
        else:
          cur_hedons += 2 * 10 -2 * (d - 10)
      elif a == "textbooks":
        if d <= 20:
          cur_hedons += 1 * d
        else:
          cur_hedons += 20 - (1 * (d - 20))
    else:
      cur_hedons += -2 * d

  # if the current star activity is the current activity and a start is given and the user is not bored with stars, then the user will get extra hedons
  if cur_star_activity == a and star == True and bored_with_stars == False:
    if d <= 10:
      cur_hedons += 3 * d
    else:
      cur_hedons += 30

  star = False


  last_activity = a
  last_activity_duration = d



################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass

def get_effective_minutes_left_health(activity):
    pass

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass


def estimate_health_delta(activity, duration):
    pass

################################################################################


if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10