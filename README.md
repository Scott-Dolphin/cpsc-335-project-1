# Project 1

|**About**  |                               |
|-----------|-------------------------------|
|Name       |Nathan                         |
|Email      |nathan-chen@csu.fullerton.edu  |

## Algorithm 1: Connecting Pairs of Persons
- While the algorithm uses a nested loop, it picks up from where the previous loop stops, so in effect, only one loop is occuring at any time.
- Therefore, this is considered one loop and falls within O(n) time complexity
    - Everything else is considered one step

### Pseudocode
```

Function min_swaps(row[]) {
    int swaps = 0
    for each couple (i, i + 1) from 0 to row.length() with 2 step increments {
        if floor(row[i] / 2) != floor(row[i + 1] / 2) {
            find j where floor(row[j] / 2) == floor(row[i] / 2)
            swap row[i + 1] with row[j]
            swaps++
        }
    }
    return swaps
}
```
### How to run: 
`~$ python3 algorithm-1.py`

## Algorithm 2: Greedy Approach to Hamilton Problem


### Pseudocode

```
Function find_starting_city(city_distances, fuel, mpg):
    total_gas = 0
    total_distance = 0
    start_city = 0
    
    For i from 0 to len(city_distances) - 1:
        total_gas += fuel[i]
        total_distance += city_distances[i]
        
        If total_gas * mpg < total_distance:
            start_city = i + 1
            total_gas = 0
            total_distance = 0
            
    Return start_city % len(city_distances)

```
### How to run: 
`~$ python3 algorithm-2.py`
