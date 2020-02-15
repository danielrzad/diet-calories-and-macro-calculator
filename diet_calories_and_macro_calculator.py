#ver 1.2 final

#calorie and macro calculator:)


def bmr(gender, weight, height, age):
    if gender == "male":
        return (9.99 * weight) + (6.25 * height) - (4.92 * age) + 5
    elif gender == "female":
        return (9.99 * weight) + (6.25 * height) - (4.92 * age) - 161


def strengh_tea(
    strengh_trainings_per_week,
    average_strengh_training_duration,
    strengh_training_intensity,
    bmr,
):
    if strengh_training_intensity == "low":
        intensity_factor = 7
        epoc_factor = 4
    elif strengh_training_intensity == "moderate":
        intensity_factor = 8
        epoc_factor = 5.5
    elif strengh_training_intensity == "high":
        intensity_factor = 9
        epoc_factor = 7
    return (
        average_strengh_training_duration *
        strengh_trainings_per_week *
        intensity_factor +
        (strengh_trainings_per_week * (epoc_factor / 100 * bmr))
	) / 7
        

def cardio_tea(
    cardio_trainings_per_week,
    average_cardio_training_duration,
    cardio_training_intensity,
):
    if cardio_training_intensity == "low":
        intensity_factor = 5
        epoc_factor = 5
    elif cardio_training_intensity == "moderate":
        intensity_factor = 7.5
        epoc_factor = 35
    elif cardio_training_intensity == "high":
        intensity_factor = 10
        epoc_factor = 180
    return (
        average_cardio_training_duration *
        cardio_trainings_per_week *
        intensity_factor +
        epoc_factor 
	) / 7
    

def neat(body_type, daily_activity_level):
    if body_type == "endomorph" and daily_activity_level == "low":
        return 200
    elif body_type == "endomorph" and daily_activity_level == "moderate":
        return 300
    elif body_type == "endomorph" and daily_activity_level == "high":
        return 400
    elif body_type == "mesomorph" and daily_activity_level == "low":
        return 400
    elif body_type == "mesomorph" and daily_activity_level == "moderate":
        return 450
    elif body_type == "mesomorph" and daily_activity_level == "high":
        return 500
    elif body_type == "ectomorph" and daily_activity_level == "low":
        return 700
    elif body_type == "ectomorph" and daily_activity_level == "moderate":
        return 800
    elif body_type == "ectomorph" and daily_activity_level == "high":
        return 900


def tef(bmr, tea, neat, body_type):
    if body_type == "ectomorph":
        factor = 10
    elif body_type == "mesomorph":
        factor = 8
    elif body_type == "endomorph":
        factor = 6
    return factor / 100 * (bmr + tea + neat)


def bmi(weight, height):
    return weight / ((height / 100) ** 2)


def calorie_calc(bmr, tea, neat, tef):
    calc = bmr + tea + neat + tef
    return int(calc)


def str_check(input_text, available_options_lst):
    while True:
        to_check = input(input_text)
        if to_check in available_options_lst:
            return to_check


def float_check(input_text, available_options_lst, negative_input):
    while True:
        to_check = input(input_text)
        try:
            if float(to_check) in available_options_lst:
                return float(to_check)
            else:
                print(negative_input)
        except ValueError:
            print("Please enter use numbers like '21', '140', etc.")


def macro_calc(gender, daily_calories, weight):
    if gender == "male":
        p_per_kg = float_check(
            "Please enter how many proteins do You want to eat per 1kg body "
            "weight. Usually it's around '2'. : ", 
            [x * 0.1 for x in range(0, 100)], 
            "Please use valid number. Typicaly its in range 1.5 - 3.",
		)
        proteins = weight * p_per_kg
        f_per_kg = float_check(
            "Please enter how many fats do You want to eat per 1kg body "
            "weight. Usually its around '1.5'. : ",
            [x * 0.1 for x in range(0, 100)], 
            "Please use valid number. Typicaly its in range 1 - 3.",
		)
        fats = weight * f_per_kg
        carbs = (daily_calories - ((proteins * 4) + (fats * 9))) / 4
        return {
            "proteins": int(proteins), 
            "fats": int(fats), 
            "carbs": int(carbs),
		}
    elif gender == "female":
        p_per_kg = float_check(
            "Please enter how many proteins do You want to eat per 1kg body "
            "weight. Usually its around '1.6'. : ", 
            [x * 0.1 for x in range(0, 100)], 
            "Please use valid number. Typicaly its in range 1.5 - 3.",
		)
        proteins = weight * p_per_kg
        f_per_kg = float_check(
            "Please enter how many fats do You want to eat per 1kg body "
            "weight. Usually its around '1.6'. : ",
            [x * 0.1 for x in range(0, 100)],
            "Please use valid number. Typicaly its in range 1 - 3.",
		)
        fats = weight * f_per_kg
        carbs = (daily_calories - ((proteins * 4) + (fats * 9))) / 4
        return {
            "*proteins": int(proteins), 
            "*fats": int(fats), 
            "*carbs": int(carbs),
		}


def calorie_and_macro_calculator():
    #personal_data
    print(
        "Hello and welcome in calorie and macro calculator ver. 1.0. We will "
        "try to help You starting a diet :). First we need to get to know "
        "some facts about You.",
	)
    name = input(
        "Please enter Your name here and we will get Your fit journey "
        "started :). : ",
	)
    gender = str_check(
        "Please enter Your gender. Only 'male' or 'female' "
        "accepted ^_^. : ", ["male", "female"],
	)
    age = float_check(
        "Please enter Your age. Use digits please, for e.g. '24'. : ", 
        range(150),
        "Please use only positive integers.",
	)
    height = float_check(
        "Please enter Your height in centimeters. Use digits please, for e.g. "
        "'181'. : ",
        range(300),
        "Please enter valid height.",
	)
    weight = float_check(
        "Please enter Your height in kilos. Use digits please, for e.g. '84'. "
        ": ",
        range(300), 
        "Please enter valid weight. Remember Your weight cannot be negative "
        "number",
	)
    body_type = str_check(
        "Please enter Your bodytype. Please choose between: 'endomorph', "
        "'ectomorph', 'mesomorph'. : ",
        ["ectomorph", "mesomorph", "endomorph"],
	)
    if body_type == "endomorph":
        daily_activity_level = str_check(
            "So You are a person characterized by heavy body build, extensive "
            "and thick skeleton, slow metabolism, and therefore a large mass "
            "of both muscle and fat, with a tendency to gain weight. Please "
            "choose Your daily activity level: 'low', 'moderate', 'high'. : ",
            ["low", "moderate", "high"],
		)
    elif body_type == "mesomorph":
        daily_activity_level = str_check(
            "So You are a person with body features and metabolism between "
            "the ectomorphic and endomorphic, with a proportional structure, "
            "an average metabolic rate and a tendency to easily increase "
            "muscle mass. Please choose Your daily activity level: 'low', "
            "'moderate', 'high'. : ", 
            ["low", "moderate", "high"],
		)
    elif body_type == "ectomorph":
        daily_activity_level = str_check(
            "So You are a person characterized by a very lean body build "
            "(thin neck, frail chest), a little spreading and slightly built "
            "skeleton, lack of fatness and rapid metabolism. Please choose "
            "Your daily activity level: 'low', 'moderate', 'high'. : ", 
            ["low", "moderate", "high"],
		)
    #training_data
    bmr_f = bmr(gender, weight, height, age)
    print("Now we need to get informations about your traing style.")
    strengh_question = str_check(
        "Are you doing strengh trainings? Please answer 'yes' or 'no'. : ",
        ["yes", "no"],
	)
    if strengh_question == "yes":
        strengh_trainings_per_week = float_check(
            "Please eneter how many times per week You are doing strengh "
            "trainings, for e.g. '4'. : ", 
            range(30),
            "Aren't Your training a negative number, or aren't You "
            "overtrained?",
		)
        average_strengh_training_duration = float_check(
            "Please eneter how much time Your single session lasts. Use "
            "minutes please. for e.g. '60' for 1 hour session. : ", 
            range(600),
            "Aren't Your entering a negative number, or aren't You entering "
            "time in seconds?",
		)
        strengh_training_intensity = str_check(
            "Please eneter how intense Your training sessions are. Please "
            "choose between: 'low', 'moderate', 'high'. : ", 
            ["low", "moderate", "high"],
		)
        str_tea_f = strengh_tea(
            strengh_trainings_per_week, 
            average_strengh_training_duration, 
            strengh_training_intensity, 
            bmr_f,
		)
    elif strengh_question == "no":
        print("Please consider doing it. It can improve losing fat")
        str_tea_f = 0
    cardio_question = str_check(
        "Are you doing cardio trainings? Please answer 'yes' or 'no'. : ", 
        ["yes", "no"],
	)
    if cardio_question == "yes":
        cardio_trainings_per_week = float_check(
            "Please eneter how many times per week You are doing cardio "
            "trainings, for e.g. '4'. : ", 
            range(30),
            "Aren't Your training a negative number, or aren't You "
            "overtrainged XD ",
		)
        average_cardio_training_duration = float_check(
            "Please eneter how much time Your single session lasts. Use "
            "minutes please. for e.g. '60' for 1 hour session. : ", 
            range(600), 
            "Aren't Your entering a negative number, or aren't You entering "
            "time in seconds?",
		)
        cardio_training_intensity = str_check(
            "Please eneter how intense Your training sessions are. Please "
            "choose between: 'low', 'moderate', 'high'. : ", 
            ["low", "moderate", "high"],
		)
        car_tea_f = cardio_tea(
            cardio_trainings_per_week, 
            average_cardio_training_duration, 
            cardio_training_intensity,
		)
    elif cardio_question == "no":
        print("Please consider doing it. It can improve losing fat.")
        car_tea_f = 0
    tea_f = str_tea_f + car_tea_f
    neat_f = neat(body_type, daily_activity_level)
    tef_f = tef(bmr_f, tea_f, neat_f, body_type)
    bmi_f = bmi(weight, height)
    daily_calories_f = calorie_calc(bmr_f, tea_f, neat_f, tef_f)
    macro_f = macro_calc(gender, daily_calories_f, weight)
    str_macro_f = '\n'.join(k + ': ' + str(v) for k, v in macro_f.items())
    print(
        "Okay, " + name + ". Everything is ready for You. If you want to "
        "start your diet adventure You should use the following values: \n* "
        "Your calories should be around: " + str(daily_calories_f) + "\n* "
        "Your macros should be around:\n" + str_macro_f + "\nPlease note that "
        "these are only illustrative values. You should start around them and "
        "observe how Your body reacts. Fell free to add or decrease these "
        "values. \nThanks for using my program. Improve Your fitness. <3 \n"
        "     Daniel R.")


if __name__ == '__main__':
	calorie_and_macro_calculator()
