

class knap:
    def dp():
        weightLimit = 20
        weights = [8,7,6,5,4]
        values = [1500, 1600, 1700,  1800, 3000]
        solution = [0] * (weightLimit+1)

        for item in range(len(weights)):
            weight = weights[item]
            value = values[item]
            for index in range(weightLimit, weight-1, -1):
                solution[index] = max(value+solution[index-weight], solution[index])
            print(solution)

        return solution 


if __name__ == "__main__":
    knap.dp()