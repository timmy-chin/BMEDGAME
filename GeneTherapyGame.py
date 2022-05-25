import time
from Protein_Translation import protein_translation


def choice(c1, c2, c3):
    global list_of_choice
    list_of_choice = [c1, c2, c3]
    print(f'[1] {c1}\n[2] {c2}\n[3] {c3}\n')

def p(text):
    print(f'\n{text}\n')
    ztime()

def minusE():
    global energy, i
    energy -= i
    print(f'Energy Lost: -{i}')
    print(f'Energy Level: {energy}')

def ztime():
    time.sleep(2)

def transition():
    ztime()
    minusE()
    ztime()

def introduction():
    ztime()
    print(f'\nUh Oh!! Turns out {name} has diabetes and {p1} is experiencing a lot of symptoms\n')
    ztime()

def valid_num(list = range(1,4)):
    num = input('Enter Number: ')
    valid = False
    while not valid:
        try:
            int(num)
            valid = True
        except:
            num = input('Must be a Number: ')
    while int(num) not in list:
        print('\nInvalid Choice, Try Again\n')
        num = input('Enter Number: ')
    return int(num)

def daily_activity():
    print(f'It is 10 am in the morning. {name} just woke up.\n')
    print('Energy Level: 100')
    ztime()
    print(f'\nWhere do you want {name} to go today?')
    ztime()
    choice('Grocery Store', 'Park', 'Beach')
    num = valid_num()
    if num == 1:
        place = 'Grocery Store'
        print(f'\n{name} hopped onto{p3}car and arrived at the {place}\n')
        transition()
        print(f'\n{name} is at the front of the grocery store. What should {name} get?')
        choice('Cart', 'Basket', 'Tote Bag')
        num = valid_num()
        if num == 1:
            item = 'Cart'
        elif num == 2:
            item = 'Basket'
        elif num == 3:
            item = 'Tote Bag'

        print(f'\n{name} went to the entrance of the grocery store and took a {item}\n')
        transition()
        print(f'\n{name} entered the grocery store. What should {name} look for?')
        choice('Bread', 'Chicken', 'Ice Cream')
        num = valid_num()
        if num == 1:
            food = 'Bread'
        elif num == 2:
            food = 'Chicken'
        elif num == 3:
            food = 'Ice Cream'
        print(f'\n{name} went to the {food} aisle and got a lot of {food}\n')
        transition()
        print(f'\n{name} is ready to leave. What do you want {name} to do?')
        choice('Go to Food Court', 'Check Out and Leave', 'Just Leave')
        num = valid_num()
        if num == 1:
            print(f'\n{name} checked out and went to the food court to get a hot dog and churros and left\n')
        elif num == 2:
            print(f'\n{name} checked out and left\n')
        elif num == 3:
            print(f'\n{name} left all {p3} groceries behind and left\n')
        ztime()
        minusE()

    elif num == 2:
        place = 'Park'
        print(f'\n{name} hopped onto {p3} car and arrived at the {place}\n')
        transition()
        print(f'\nWhat sport do you want {name} to play?')
        choice('Basketball', 'Badminton', 'Volleyball')
        num = valid_num()
        if num == 1:
            sport = 'Basketball'
            print(f'\n{name} went to the {sport} court with {p3} {sport}\n')
            transition()
            print(f'\nWhat moves do you want {name} to perform?')
            choice('Dunk', 'Shoot', 'Lay Up')
            num = valid_num()
            move = list_of_choice[num - 1]
            print(f'\n{name} did a {move} and scored a point for {p3} team\n')

        elif num == 2:
            sport = 'Badminton'
            print(f'\n{name} went to the {sport} court with {p3} {sport} racquet.\n')
            transition()
            print(f'\nWhat moves do you want {name} to perform?')
            choice('Clear', 'Smash', 'Drop')
            num = valid_num()
            move = list_of_choice[num]
            print(f'\n{name} did a {move} and {p3} opponent failed to return it\n')
        elif num == 3:
            sport = 'Volleyball'
            print(f'\n{name} went to the {sport} court with {p3} {sport}\n')
            transition()
            print(f'\nWhat moves do you want {name} to perform?')
            choice('Pass', 'Serve', 'Spike')
            num = valid_num()
            move = list_of_choice[num]
            print(f'\n{name} did a {move} and {p3} opponent failed to return it\n')

        transition()
        print(f'\n{name} is ready to leave. What do you want {name} to do?')
        choice('Drink Water and Leave', 'Drink Coke and Leave', 'Just Leave')
        num = valid_num()
        if num == 1:
            print(f'\n{name} bought water from a vending machine and left\n')
        elif num == 2:
            print(f'\n{name} bought coke from a vending machine and left\n')
        elif num == 3:
            print(f'\n{name} just left\n')
        transition()

    elif num == 3:
        place = 'Beach'
        print(f'\n{name} hopped onto {p3} car and arrived at the {place}\n')
        transition()
        print(f'\nWhat activity do you want {name} to do at the beach?')
        choice('Beach Volleyball', 'Swimming', 'Build Sandcastle')
        num = valid_num()
        if num == 1:
            print(f'\n{name} went to the beach volleyball court with {p3} volleyball\n')
            transition()
            print(f'\nWhat move do you want {name} to perform?')
            choice('Pass', 'Spike', 'Serve')
            num = valid_num()
            move = list_of_choice[num - 1]
            print(f'\n{name} performed a {move} and {p3} opponent fail to return it\n')

        elif num == 2:
            print(f'\n{name} wore {p3} swimsuit and went to the ocean\n')
            transition()
            print(f'\nWhat stroke do you want {name} to swim?')
            choice('Freestyle', 'Breaststroke', 'Butterfly')
            num = valid_num()
            stroke = list_of_choice[num - 1]
            print(f'\n{name} swam {stroke} all around the ocean for an hour\n')

        elif num == 3:
            print(f'\n{name} got {p3} shovel and bucket and went to the sand\n')
            transition()
            print(f'\nWhat structure do you want {name} to build?')
            choice('Tower', 'Wall', 'Gate')
            num = valid_num()
            structure = list_of_choice[num - 1]
            print(f'\n{name} took a big pile of sand and built a big {structure}\n')

        transition()
        print(f'\n{name} is ready to go home, what do you want {p2} to do?')
        choice('Pack Mat', 'Pack Beach Ball', 'Take a Shower')
        num = valid_num()
        if num == 1:
            print(f'\n{name} packed the mat to {p3} car and drove home\n')
        elif num == 2:
            print(f'\n{name} packed {p3} beach balls to {p3} car and drove home\n')
        elif num == 3:
            print(f'\n{name} took a shower and went back home in {p3} car\n')
        transition()

def diabetes_daily_activity(intro = False):
    print(f'It is 10 am in the morning. {name} just woke up.\n')
    print('Energy Level: 100')
    ztime()
    print(f'\nWhere do you want {name} to go today?')
    ztime()
    choice('Grocery Store', 'Park', 'Beach')
    num = valid_num()
    if num == 1:
        place = 'Grocery Store'
        if intro:
            introduction()
        print(f'\n{name}\'s numb legs caused {p2} to fall while getting into {p2} car to go to the {place}\n')
        transition()
        print(f'\n{name} is at the front of the grocery store. What should {name} get?')
        choice('Cart', 'Basket', 'Tote Bag')
        num = valid_num()
        if num == 1:
            item = 'Cart'
        elif num == 2:
            item = 'Basket'
        elif num == 3:
            item = 'Tote Bag'

        print(f'\n{name}\'s blurry vision caused {p2} to bump into people and trip over a dog while {p1} was going to take a {item}\n')
        transition()
        print(f'\n{name} entered the grocery store. What should {name} look for?')
        choice('Bread', 'Chicken', 'Ice Cream')
        num = valid_num()
        if num == 1:
            food = 'Bread'
        elif num == 2:
            food = 'Chicken'
        elif num == 3:
            food = 'Ice Cream'
        print(f'\n{name}\'s numb feet gave {p2} a very hard time to get to the {food} department\n')
        transition()
        print(f'\n{name} is ready to leave. What do you want {name} to do?')
        choice('Go to Food Court', 'Check Out and Leave', 'Just Leave')
        num = valid_num()
        if num == 1:
            print(f'\n{name}\'s uncontrollable urination caused {p2} to urinate in {p3} pants while {p1} was going to the food court\n')
        elif num == 2:
            print(f'\n{name}\'s uncontrollable urination caused {p2} to urinate in {p3} pants while {p1} was checking out and leaving\n')
        elif num == 3:
            print(f'\n{name}\'s uncontrollable urination caused {p2} to urinate in {p3} pants while {p1} was leaving\n')
        ztime()
        minusE()

    elif num == 2:
        place = 'Park'
        if intro:
            introduction()
        print(f'\n{name}\'s numb legs caused {p2} to fall while getting into {p2} car to go to the {place}\n')
        transition()
        print(f'\nWhat sport do you want {name} to play?')
        choice('Basketball', 'Badminton', 'Volleyball')
        num = valid_num()
        if num == 1:
            sport = 'Basketball'
            print(f'\nWhile {name} is going to the {sport} court with {p3} {sport}, {p3} blurry vision caused {p2} to bump into a tree. But, he made it to the court alive\n')
            transition()
            print(f'\nWhat moves do you want {name} to perform?')
            choice('Dunk', 'Shoot', 'Lay Up')
            num = valid_num()
            move = list_of_choice[num - 1]
            print(f'\n{name}\'s numb feet caused {p2} to fall when {p1} was doing a {move}, and {p1} failed to scored a point for {p3} team\n')

        elif num == 2:
            sport = 'Badminton'
            print(f'\nWhile {name} is going to the {sport} court with {p3} {sport} racquet, {p3} blurry vision caused {p2} to bump into a tree. But, {p1} made it to the court alive\n')
            transition()
            print(f'\nWhat moves do you want {name} to perform?')
            choice('Clear', 'Smash', 'Drop')
            num = valid_num()
            move = list_of_choice[num]
            print(f'\n{name}\'s numb feet caused {p2} to fall when {p1} was doing a {move}, and {p1} failed to scored a point for {p3} team\n')
        elif num == 3:
            sport = 'Volleyball'
            print(f'\nWhile {name} is going to the {sport} court with {p3} {sport}, {p3} blurry vision caused {p2} to bump into a tree. But, {p1} made it to the court alive\n')
            transition()
            print(f'\nWhat moves do you want {name} to perform?')
            choice('Pass', 'Serve', 'Spike')
            num = valid_num()
            move = list_of_choice[num]
            print(f'\n{name}\'s numb feet caused {p2} to fall when {p1} was doing a {move}, and {p1} failed to scored a point for {p3} team\n')

        transition()
        print(f'\n{name} is ready to leave. What do you want {name} to do?')
        choice('Drink Water and Leave', 'Drink Coke and Leave', 'Just Leave')
        num = valid_num()
        if num == 1:
            print(f'\nAfter {name} drank water, {p3} uncontrollable urination caused {p2} to urinate in {p3} pants\n')
        elif num == 2:
            print(f'\nAfter {name} drank coke, {p3} uncontrollable urination caused {p2} to urinate in {p3} pants\n')
        elif num == 3:
            print(f'\nWhile {name} was leaving, {p3} uncontrollable urination caused {p2} to urinate in {p3} pants\n')
        transition()

    elif num == 3:
        place = 'Beach'
        if intro:
            introduction()
        print(f'\n{name}\'s numb legs caused {p2} to fall while getting into {p2} car to go to the {place}\n')
        transition()
        print(f'\nWhat activity do you want {name} to do at the beach?')
        choice('Beach Volleyball', 'Swimming', 'Build Sandcastle')
        num = valid_num()
        if num == 1:
            print(f'\nWhile {name} was going to the beach volleyball court with {p3} volleyball, {p3} blurry vision caused {p2} to bump into a tree. But, {p1} made it there alive\n')
            transition()
            print(f'\nWhat move do you want {name} to perform?')
            choice('Pass', 'Spike', 'Serve')
            num = valid_num()
            move = list_of_choice[num - 1]
            print(f'\n{name}\'s numb legs caused {p2} to fall while performing a {move} and {p1} fails to score a point\n')

        elif num == 2:
            print(f'\nWhile {name} was going to the ocean with {p3} swimsuit, {p3} blurry vision caused {p2} to bump into a tree. But, {p1} made it there alive\n')
            transition()
            print(f'\nWhat stroke do you want {name} to swim?')
            choice('Freestyle', 'Breaststroke', 'Butterfly')
            num = valid_num()
            stroke = list_of_choice[num - 1]
            print(f'\n{name}\'s numb legs caused {p2} to almost drown when {p1} was swimming {stroke}\n')

        elif num == 3:
            print(f'\nWhile {name} was going to a sandy spot with {p3} volleyball, {p3} blurry vision caused {p2} to bump into a tree. But, {p1} made it there alive\n')
            transition()
            print(f'\nWhat structure do you want {name} to build?')
            choice('Tower', 'Wall', 'Gate')
            num = valid_num()
            structure = list_of_choice[num - 1]
            print(f'\n{name}\'s numb hands prevented {p2} from building a stable {structure}\n')

        transition()
        print(f'\n{name} is ready to go home, what do you want {p2} to do?')
        choice('Pack Mat', 'Pack Beach Ball', 'Take a Shower')
        num = valid_num()
        if num == 1:
            print(f'\n{name}\'s uncontrollable urination caused {p2} to urinate in {p3} pants while {p1} was packing the mat and driving home\n')
        elif num == 2:
            print(f'\n{name}\'s uncontrollable urination caused {p2} to urinate in {p3} pants while {p1} was packing the beach balls and driving home\n')
        elif num == 3:
            print(f'\n{name}\'s uncontrollable urination caused {p2} to urinate in {p3} pants while {p1} was showering and driving home\n')
        transition()

def go_hospital():
    p(f'\n\nWhile going home, {name} passed out and got sent to the hospital\n')
    p('You are the doctor now and you are trying to treat him')
    print('\nChoose an action to perform:\n')
    print(f'[1] Do a Screening on {name}\n[2] Send {name} home without any treatment\n')
    num = valid_num(range(1,3))
    if num == 2:
        p(f'You released {name} without any treatment. Now {name} is going to continue {p3} daily life')
        return False
    elif num == 1:
        p(f'\nScreening: {name} is showing symptoms of numb legs, urinating very often, fatigue, and blurry vision. \n{name} has a wound on {p3} leg and it is not healing due to low blood flow; \nif left untreated, it could lead to infections that would cause complication')

    print(f'\nAs the doctor, which manual would you refer to to treat {name}?')
    choice('Cause and Treatment for Headache', 'Cause and Treatment for Diabetes', 'Cause and Treatment for Sore Throat')
    num = valid_num()
    while num != 2:
        print(f'\n{name} does not show any related symptoms to the manual you chose, please choose again')
        choice('Cause and Treatment for Headache', 'Cause and Treatment for Diabetes','Cause and Treatment for Sore Throat')
        num = valid_num()

    p(f'\nDiabetes Manual: Diabetes is caused when the immune system destroys insulins produced by beta cells that are '
      f'\nused to regulate the blood sugar level of a human’s body')
    p('Treatment includes gene therapy that could introduce proteins that would reprogram alpha cells into beta cells '
      '\nthat produce insulins that are resistant to immune attacks; this way the wound in the leg would be healed from '
      '\nregular blood flow. Alternative would be to amputate the patient’s leg so that no complication would arise from '
      '\nthe untreated wound on the leg')
    print(f'\nWhat treatment would you choose to perform on {name}:')
    choice('Gene Therapy', 'Install Prosthetic', 'Amputation')
    num = valid_num()
    if num == 2:
        p(f'You amputated {name}\'s leg and installed a prosthetic leg for him. {name} is then released from the '
          f'\nhospital to continue {p3} daily life.')
        return False
    elif num == 3:
        p(f'You amputated {name}\'s leg and released {p2} from the hospital. {name} then continues {p3} daily life.')
        return False
    elif num == 1:
        p(f'With Gene Therapy, you injected two protein into {name}\'s body that would reprogram {p3} alpha cells into '
          f'\nbeta cells that produces insulin that are resistant to immune attacks')
        valid_DNA = False
        while not valid_DNA:
            p(f'You are trying to re-program a small portion of {name}\'s alpha cell DNA sequence for insulin to this:')
            rightDNA = ['C','C','T','C','A','T','G','C','T']
            p(f'{"".join(rightDNA[0:3])} {"".join(rightDNA[3:6])} {"".join(rightDNA[6:9])}')
            p('To Get a small portion of Resistant Insulin with this protein sequence:')
            p(f'{protein_translation("".join(rightDNA))}')
            p(f'{name}\'s Current Alpha Cell DNA sequence:')
            DNA = ['C','C','T','C','T','T','G','C','T']
            print_DNA = f'{"".join(DNA[0:3])} {"".join(DNA[3:6])} {"".join(DNA[6:9])}'
            p(f"{print_DNA}\n123 456 789")
            print('Which index of the DNA sequence should be substituted?')
            num = valid_num(range(1, len(DNA)+1))
            print('Which Letter Should you substitute it with? (A/T/C/G): ')
            letter = input('Enter Letter: ')
            while letter.upper() not in 'ATCG':
                print('Invalid Letter, Try Again\n')
                letter = input('Enter Letter: ')
            DNA[num-1] = letter.upper()
            p(f'Your re-programmed alpha cell:')
            p(f'{"".join(DNA[0:3])} {"".join(DNA[3:6])} {"".join(DNA[6:9])}')
            p(f'Portion of insulin produced:')
            insulin = protein_translation("".join(DNA))
            p(f'{insulin}')

            if "".join(DNA) == "".join(rightDNA):
                p(f'Yay! {name}’s beta cells are producing insulin that are resistant to immune attack. Now {p3} blood '
                  f'\nsugar is being regulated with sufficient insulin circulating in {p3} body, and {p3} leg is being '
                  f'\nhealed.')
                p(f'Phew! With gene therapy, {name} would not have needed an amputation, which further emphasizes the '
                  f'\nimportance and societal impact of the creation of gene therapy in bioengineering')
                p(f'Now {name} can be released from the hospital to continue doing {p3} daily activities!\n')
                valid_DNA = True
                return True
            else:
                p('The insulin produced is not resistant to immune attack, try to substitute again.')
                valid_DNA = False











print(f'Welcome to the Biomedical Engineering Game! \n')
ztime()
print(f'You task is to treat a patient suffering with Diabetes with the right bioengineering system and design\n\n')
enter = input('Press Enter to Play ')
print('\n')
name = input('Enter Character Name: ')
p1 = input('Enter Pronouns (he/she/they): ')
p2 = input('Enter Pronouns (him/her/them): ')
p3 = input('Enter Pronouns (his/hers/their) ')
print('\n\n')
list_of_choice = []

energy = 100
intro = True
i = 25
diabetes_daily_activity(intro)
treated = go_hospital()

while not treated:
    energy = 100
    i = 25
    diabetes_daily_activity()
    treated = go_hospital()

energy = 100
i = 1
daily_activity()

p(f'\n{name} continues to live happily and healthily ever after!')
p(f'Congratulations, you treated {name} and won the game!')
