class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # if your position is 4, you have 6 remaining. You travel at 2, so you take 3h to reach 10.
        # if your position is 1, you hav 9 remaining, you travel at 3, so you take 3h to reach 10
        # so what we need to calculate is the amount of time you take to hit 10. We can store that in an array. The number of fleets is the number of unique elements 
        previous_fleet_time = 0
        fleet = 0
        time = [0] * len(position)
        posxspeed = list(zip(position,speed))
        posxspeed.sort(reverse=True)
        for i in range(len(position)):
            pos = posxspeed[i][0]
            dist = target - pos 
            spe = posxspeed[i][1]
            ti = dist/spe
            time[i] = ti
        for t in time:
            if t > previous_fleet_time:
                previous_fleet_time = t
                fleet += 1
        
        return fleet
        