from Levenshtein import distance
from constants import TRUSTED_DOMAINS

def run():
    # Ask for user data
    data = input('Which domains would you like to check?: ')
    distance = input('What distance is risky?: ')

    try:
        # Format user provided data
        domains = data.strip().split(',')
        risky_distances = list(range(1, int(distance) +  1))
    except Exception as e:
        # Catch any formatting errors
        return print(e)

    check_domains(domains, risky_distances)


def check_domains(domains, risky_distances):
    # evaluate each domain against trusted domain
    for domain in domains:
        matches = [
            trusted for trusted in TRUSTED_DOMAINS 
            if check_distance(trusted, domain)[1] in risky_distances
        ]
        # notify user that provided domain is potentially risky
        if matches:
            print('============')
            [
                print(
                    f'risky_domain: {domain}\nsimilar: {check_distance(risk, domain)[0]}\ndistance: {check_distance(risk, domain)[1]}'
                ) for risk in matches
            ]

def check_distance(str1, str2):
    return str1, distance(str1, str2)


run()